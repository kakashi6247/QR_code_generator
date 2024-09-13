# QR Code Generator with Flask

This Flask web application allows users to generate QR codes from a provided URL and download the resulting QR code image.

## Features:
- **QR Code Generation**: The application generates a QR code from a user-inputted URL.
- **Input Validation**: The application ensures that the input is a valid URL using the `validators` module.
- **Dynamic Download**: The generated QR code can be downloaded directly by the user as a PNG image. The filename includes the current date and time for uniqueness.
- **In-memory Image Processing**: The QR code is processed in memory without saving the image to disk, ensuring efficiency and reducing storage overhead.

## How It Works:
1. User enters a valid URL in the provided input field.
2. The application checks if the entered URL is valid.
   - If invalid, an error message will be displayed prompting the user to enter a valid URL.
3. If the URL is valid, a QR code is generated for that URL.
4. The generated QR code is offered as a downloadable PNG file with a unique timestamp-based filename.

## Key Components:
- **Flask**: A lightweight web framework used to handle HTTP requests and responses.
- **qrcode**: A Python library used to generate QR code images.
- **validators**: A module used to verify that the user input is a valid URL.
- **datetime**: Used to generate a timestamp for naming the QR code file.
- **BytesIO**: Used to store the QR code image in memory, allowing for easy download without writing to the disk.

## Requirements:
- Flask
- qrcode
- validators

## Running the Application:
1. Clone or download the repository.
2. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
3. Run the application:
   ```
   python main.py
   ```
4. Access the application by navigating to `http://localhost:5000` in your browser.
