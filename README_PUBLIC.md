# Couple Memory Website - Public Version

A beautiful, interactive website for couples to share their memories, play trivia, and celebrate special moments together.

## 🎯 Features

- **Interactive Memory Gallery**: Flip cards to reveal personalized messages
- **Couple Trivia Game**: Test how well you know each other
- **Birthday Celebration**: Special birthday features accessible year-round
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Beautiful Animations**: Hearts, confetti, and interactive elements

## 🛠️ Customization Guide

### 1. Personal Messages

#### Main Page Messages
Edit messages in `main.py`:
```python
IMAGE_MESSAGES = {
    'DSCN4176.JPG': 'Your custom message here',
    'IMG_0035.JPG': 'Your custom message here',
    'IMG_0470.jpeg': 'Your custom message here'
}
```

#### More Memories Messages
Edit messages in `main.py`:
```python
MORE_MEMORIES_MESSAGES = {
    'IMG_3396.jpeg': 'Your custom message here',
    'IMG_9942.JPG': 'Your custom message here',
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

### 4. Your Own Photos

1. Replace placeholder images in `static/uploads/` with your own photos
2. Replace placeholder images in `static/more_memories/` with your own photos
3. Make sure to use the same filenames or update the message dictionaries accordingly

## 🚀 Getting Started

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Customize Content**:
   - Edit messages in `main.py`
   - Edit special message in `templates/index.html`
   - Edit birthday card in `templates/birthday_card.html`
   - Replace placeholder images with your own photos

3. **Run the Application**:
   ```bash
   python main.py
   ```

4. **Access the Website**:
   Open your browser and go to `http://localhost:5000`

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
│   ├── css/                  # Stylesheets
│   ├── music/                # Audio files
│   └── images/               # Images
└── requirements.txt          # Python dependencies
```

## 🎨 Customization Tips

- **Photos**: Use JPG, PNG, or JPEG format
- **Messages**: You can use HTML tags like `<br>` for line breaks
- **Trivia**: Make sure the 'correct' answer exactly matches one of the options
- **Birthday Card**: You can add more pages by adding to the `pages` array

## 💝 Perfect For

- Anniversaries
- Valentine's Day
- Birthdays
- Just because you love each other!

## 🔒 Privacy Note

This public version contains no personal information and is safe to share. All messages and content are customizable placeholders.

---

**Made with ❤️ for couples everywhere**
