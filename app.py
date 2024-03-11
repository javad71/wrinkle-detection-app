import os
import json
from flask import Flask, render_template, request, send_file, redirect, flash
from werkzeug.utils import secure_filename
from ultralytics import YOLO

# Load config information from JSON file if available
try:
    with open('config.json') as f:
        config = json.load(f)
except:
    pass

app = Flask(__name__)
app.secret_key = config['secret_key']
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


# Endpoint for main dashboard
@app.route('/', methods=['GET', 'POST'])
def main():
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
            # Save the uploaded file
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Perform your image processing here
            processed_filename = process_image(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Send the processed image back to the page
            return send_file(processed_filename, as_attachment=True)

    return render_template('index.html')


def process_image(input_path):
    # Load a model
    model = YOLO('./models/wd-yolov8-small.pt')  # load a custom model

    # Predict with the model
    results = model(input_path, conf=0.5, imgsz=640)  # predict on an image

    # Process results list
    for result in results:
        result.save(filename='./uploads/result.jpg')  # save to disk

    return input_path


if __name__ == '__main__':
    app.run(debug=True)
