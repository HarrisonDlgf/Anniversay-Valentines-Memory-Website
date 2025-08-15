# Couple Memory Website ❤️

A beautiful, interactive website for couples to share their memories, play trivia, and celebrate special moments together. Features flippable image cards with captions, a customizable quiz, interactive animations, and a special birthday celebration feature.

## 🎯 Features

- **Interactive Memory Gallery**: Flip cards to reveal personalized messages
- **Couple Trivia Game**: Test how well you know each other
- **Birthday Celebration**: Special birthday features accessible year-round
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Beautiful Animations**: Hearts, confetti, and interactive elements
- **Romantic Theme**: Pink gradient backgrounds and floating hearts
- **Hidden Messages**: Interactive buttons with sweet surprises
- **Music Integration**: Customizable background music for special moments

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Add Your Photos
- **Main photos**: Add to `static/uploads/` folder
- **More memories**: Add to `static/more_memories/` folder
- **Supported formats**: .jpg, .jpeg, .png, .gif

### 3. Customize Content
- Edit messages in `main.py` (see customization guide below)
- Edit special message in `templates/index.html`
- Edit birthday card in `templates/birthday_card.html`
- Replace placeholder images with your own photos

### 4. Run the Application
```bash
python main.py
```

### 5. Access the Website
Open your browser and go to `http://localhost:5000`

## 🛠️ Customization Guide

### 1. Personal Messages

#### Main Page Messages
Edit messages in `main.py`:
```python
IMAGE_MESSAGES = {
    'your_photo.jpg': 'Your custom message here',
    'another_photo.jpg': 'Your custom message here',
    # ... add more as needed
}
```

#### More Memories Messages
Edit messages in `main.py`:
```python
MORE_MEMORIES_MESSAGES = {
    'memory_photo.jpg': 'Your custom message here',
    'special_moment.jpg': 'Your custom message here',
    # ... add more as needed
}
```

#### Special Click Message
Edit in `templates/index.html`:
```html
<div id="message1" class="message" style="display: none;">
   Your custom message here
</div>
```

### 2. Trivia Questions

Edit questions in `main.py`:
```python
TRIVIA_QUESTIONS = [
    {
        'question': 'Your question here?',
        'options': ['Option 1', 'Option 2', 'Option 3', 'Option 4'],
        'correct': 'Option 1'  # Must match one of the options exactly
    },
    # ... add more questions
]
```

### 3. Birthday Card Messages

Edit in `templates/birthday_card.html`:
```javascript
const pages = [
    {
        title: "Your Title",
        message: "Your message here"
    },
    // ... add more pages
];
```

### 4. Music Customization 🎵

#### Birthday Music
- Replace `static/music/birthday.mp3` with your own birthday song
- The music will play automatically on the birthday page
- Supports MP3 format

#### Trivia Game Music
- Replace `static/music/jeopardy.mp3` with your preferred background music
- Plays during the trivia game for added atmosphere
- Supports MP3 format

#### Adding New Music
1. Place your music files in the `static/music/` folder
2. Update the audio source in the HTML templates:
   ```html
   <source src="{{ url_for('static', filename='music/your_song.mp3') }}" type="audio/mpeg">
   ```

### 5. Your Own Photos

1. Replace placeholder images in `static/uploads/` with your own photos
2. Replace placeholder images in `static/more_memories/` with your own photos
3. Make sure to use the same filenames or update the message dictionaries accordingly

## 📁 File Structure

```
├── main.py                    # Main application file (edit messages here)
├── templates/
│   ├── index.html            # Main page (edit special message here)
│   ├── birthday_card.html    # Birthday card (edit messages here)
│   ├── trivia.html           # Trivia game
│   ├── more_memories.html    # More memories page
│   └── birthday.html         # Birthday page
├── static/
│   ├── uploads/              # Main photos (replace with your own)
│   ├── more_memories/        # More photos (replace with your own)
│   ├── music/                # Audio files (customize here!)
│   │   ├── birthday.mp3      # Birthday celebration music
│   │   └── jeopardy.mp3      # Trivia game music
│   ├── css/                  # Stylesheets
│   └── images/               # Images
└── requirements.txt          # Python dependencies
```

## 🎨 Customization Tips

- **Photos**: Use JPG, PNG, or JPEG format
- **Messages**: You can use HTML tags like `<br>` for line breaks
- **Trivia**: Make sure the 'correct' answer exactly matches one of the options
- **Birthday Card**: You can add more pages by adding to the `pages` array
- **Music**: Use MP3 format for best compatibility
- **File Names**: Keep track of your photo filenames to match them in the message dictionaries

## 💝 Perfect For

- Anniversaries
- Valentine's Day
- Birthdays
- Just because you love each other!
- Long-distance relationships
- Special celebrations

## 🔒 Privacy Note

This public version contains no personal information and is safe to share. All messages and content are customizable placeholders. Your personal photos and messages stay private on your local machine. I recommend branching off and utilizing the gitignore if using git for state management.

## 🎵 Music Recommendations

For the best experience, consider using:
- **Birthday music**: Upbeat, celebratory songs
- **Trivia music**: Light, fun background music
- **File size**: Keep music files under 5MB for faster loading
- **Duration**: 2-3 minute loops work well for background music

---

**Made with ❤️ for couples and partnerships everywhere**

*I made this website initially for an anniversary, I hope anyone who wishes to fork or clone can use it as a nice surprise for a special person*
