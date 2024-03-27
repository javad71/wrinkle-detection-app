import os
import datetime
import random
import string
import json
import logging
from flask import Flask, render_template, request, send_file, redirect, flash, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from ultralytics import YOLO

# Load config information from JSON file if available
try:
    with open('config.json') as f:
        config = json.load(f)
except Exception as e:
    logging.error(f"Error loading config: {e}")
    config = {}

app = Flask(__name__)
app.secret_key = config['secret_key']
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}
upload_folder = config['upload_folder']

# Load the model once during application startup
model = YOLO('./models/wd-yolov8-small.pt')  # load a custom model


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def generate_random_filename():
    current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return f"{current_time}_{random_string}"


# Endpoint for main dashboard
@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'GET':
        try:
            # Load existing data
            json_filename = './result.json'
            with open(json_filename, 'r') as json_file:
                response_message = json.load(json_file)
        except:
            response_message = {}

        return render_template('index.html', result_data=response_message)

    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # If the user does not select a file, browser also submits an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            try:
                # Save the uploaded file
                filename = secure_filename(file.filename)
                file_path = os.path.join(str(upload_folder), filename)
                file.save(file_path)

                # Perform your image processing here
                response_message = process_image(file_path)

                return render_template('index.html', result_data=response_message)

            except Exception as e:
                logging.error(f"Error processing image: {e}")
                response_message = {'status': 'error', 'message': 'Error processing image.'}
                return render_template('index.html', result_data=response_message)

    return render_template('index.html')


def process_image(input_path):
    try:
        # Predict with the model
        results = model(input_path, conf=0.5, imgsz=640)  # predict on an image

        # Process results list
        result_data = []
        for result in results:
            filename = f'./uploads/{generate_random_filename()}.jpg'
            result.save(filename=filename)  # save to disk

            labels = []
            for box in result.boxes:
                label = result.names[int(box.cls)]  # Get the class label
                labels.append(label)

            result_info = {
                'tags': labels,
                'path': filename
            }
            result_data.append(result_info)

        # JSON file path
        json_filename = './result.json'

        # Check if the JSON file exists
        if os.path.exists(json_filename):
            # Load existing data
            with open(json_filename, 'r') as json_file:
                existing_data = json.load(json_file)
            # Append new data to the existing list
            existing_data.extend(result_data)
        else:
            # If the file doesn't exist, use the new data
            existing_data = result_data

        # Save the updated results in the JSON file
        with open(json_filename, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)

        return existing_data
    except Exception as e:
        logging.error(f"Error processing image: {e}")
        return None


# Endpoint for show image from uploads
@app.route('/uploads/<filename>')
def result_image(filename):
    return send_from_directory(str(upload_folder), filename)


@app.route('/get_updated_results', methods=['GET'])
def get_updated_results():
    try:
        # Load existing data
        json_filename = './result.json'
        with open(json_filename, 'r') as json_file:
            response_message = json.load(json_file)
    except Exception as e:
        logging.error(f"Error loading updated results: {e}")
        response_message = {}

    return jsonify(response_message)


if __name__ == '__main__':
    app.run(debug=True)
