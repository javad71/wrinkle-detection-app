# Wrinkle Detection Web App

The Wrinkle Detection Web App is a sophisticated tool powered by YOLOv8 deep learning techniques, designed to help users analyze and manage facial wrinkles effectively. Whether you're curious about your skin's condition or seeking ways to improve it, this app serves as a valuable asset in your skincare journey.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)

## Overview

In the realm of skincare and beauty, the quest for youthful skin drives innovation. Wrinkles, often seen as signs of aging, prompt the development of solutions like wrinkle detection apps. This overview explores the creation and functionality of such an app, particularly focusing on its ability to detect nine distinct types of wrinkles, catering to diverse user needs and concerns.

## Installation

To install and run the app locally, follow these steps:

1. **Install Python:** If you don't have Python installed, download and install it from the [official website](https://www.python.org/downloads/). Make sure to check the box that says "Add Python to PATH" during installation.

2. **Open a Command Prompt:** Press `Win + R`, type `cmd`, and press Enter to open a Command Prompt.

3. **Create a Virtual Environment:** Navigate to your project folder in the Command Prompt and run the following commands:
    ```
    cd wrinkle-detection-app
    python -m venv venv
    ```

4. **Activate the Virtual Environment:** In the Command Prompt, navigate to the project folder (if not already there) and activate the virtual environment:
    ```
    venv\Scripts\activate
    ```

5. **Install Requirements:** While the virtual environment is active, install Flask and ultralytics using the following commands:
    ```
    pip install Flask==3.0.2
    pip install ultralytics==8.1.26
    ```

6. **Set App Environment Variable:** In the Command Prompt, set the Flask app file as an environment variable. Your app file is named `app.py`.
    ```
    set FLASK_APP=app.py
    ```

7. **Run the App:** Finally, run the app with the following command:
    ```
    python app.py
    ```
   This will start the development server, and you should see output indicating that the server is running. By default, the app will be accessible at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or [http://localhost:5000/](http://localhost:5000/).

8. **Open the App in a Web Browser:** Open your web browser and navigate to the address where the app is running.

## Usage

The Wrinkle Detection Web App provides an intuitive interface for analyzing and managing facial wrinkles. Here's how you can make the most out of its functionalities:

- **Upload and Process Images:** Navigate to the "Upload Image" section of the web app. Choose an image containing facial features and wrinkles that you wish to analyze. Click on the "Process" button to initiate the analysis using the YOLOv8 trained model.

- **Detection and Storage:** Upon processing, the app will detect various types of wrinkles present in the uploaded image using the YOLOv8 model. The results are then stored in a NoSQL format and saved into a JSON file for easy retrieval and display.

- **View Results in Album Format:** Head to the "Results Album" section to view the detected wrinkles. The album presents the images along with their associated detected wrinkles in a visually appealing format. Users can switch between two layout options: "Day" and "Night", depending on their preference.

- **Extended Image Viewing and Deletion:** In the album, users can click on individual images to view them in an extended format for closer inspection. Additionally, users have the option to delete specific results if desired, allowing for personalized management of the detected wrinkles.

- **Contact Developer and About Us:** If you have any questions, feedback, or suggestions, feel free to reach out to the developer. Access the "About Us" section for more information about the app, its development team, and the technology behind it.

## Troubleshooting

Encountering issues while using the Wrinkle Detection Web App? Refer to this troubleshooting guide to resolve common problems and optimize your experience.

- **Image Upload Failure:** Ensure that the file format is supported (e.g., JPEG, PNG) and that the file size does not exceed the maximum limit set by the app. Check your internet connection and clear your browser cache if necessary.

- **Processing Errors:** Verify that the uploaded image contains clear and well-lit facial features. Ensure that the app server is running smoothly and try uploading a different image if the problem persists.

- **Result Display Issues:** Refresh the page to reload the data from the JSON file. Check for browser extensions or ad blockers that may interfere with the app's functionality. Ensure that JavaScript is enabled in your browser settings.

- **Layout Selection Problems:** Clear your browser cookies and cache. Make sure that your browser supports CSS styles and that there are no conflicts with other installed plugins or themes.

- **Contacting Developer:** Double-check the contact details provided and try alternative communication channels if the contact form is not working.

- **General Performance Issues:** Close unnecessary browser tabs or applications running in the background. Check your device's hardware specifications and consider upgrading if necessary.

By following these troubleshooting steps, you should be able to resolve common issues encountered while using the Wrinkle Detection Web App. If you continue to experience difficulties, don't hesitate to reach out to our support team for further assistance. We're here to help you make the most out of your skincare journey!


