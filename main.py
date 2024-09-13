from flask import Flask, render_template, request, url_for, send_file
import qrcode
import validators
from datetime import datetime
from io import BytesIO

app = Flask(__name__)

def generate_qr(link):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # Add data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code instance
    img = qr.make_image(fill='black', back_color='white')

    # Save the image to an in-memory bytes buffer
    img_io = BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return img_io

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        link1 = request.form.get('link1', '')

        # Validate URL
        if not validators.url(link1):
            error = "Please enter a valid URL."
            return render_template('qrGenerate.html', error=error)

        # Generate the QR code in memory
        qr_code_img = generate_qr(link1)

        # Send the image as a file download
        return send_file(qr_code_img, mimetype='image/png', as_attachment=True, download_name=f"qr_code_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")

    return render_template('qrGenerate.html')

if __name__ == '__main__':
    app.run(debug=True)
