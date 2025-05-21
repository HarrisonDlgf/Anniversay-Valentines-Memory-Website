# Anniversary Website

A sweet and simple website to celebrate your time spent with your partner. Flippable image cards with captions, a customizable quiz, and a fun little hidden message behind a trick button with CSS animations and styling for the background

## Setup Instructions

1. Install the required packages:
```bash
pip install -r requirements.txt
```

2. Create a folder called `static/uploads` in the project directory (it will be created automatically when you run the app)

3. Add your images to the `static/uploads` folder. Supported formats: .jpg, .jpeg, .png, .gif

4. For the more memories, add images to a folder inside of static labeled `more_memories`. Again same supported formats.

4. Run the application:
```bash
python main.py
```

5. Open your web browser and go to `http://localhost:5000`

6. If the local host isn't working, it is being hosted on your IP. Check your console to see where

## Features

- Romantic theme
- Interactive buttons with sweet messages
- Image gallery displaying your uploaded photos
- Responsive design that works on all devices

## Customization

You can customize the messages in the `templates/index.html` file by editing the text inside the message divs.

To add more images, simply place them in the `static/uploads` folder. 