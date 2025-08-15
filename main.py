from flask import Flask, render_template, send_from_directory, jsonify, request
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///scores.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class HighScore(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

# Create tables
with app.app_context():
    db.create_all()

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = 'static/uploads'
MORE_MEMORIES_FOLDER = 'static/more_memories'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(MORE_MEMORIES_FOLDER):
    os.makedirs(MORE_MEMORIES_FOLDER)

# Customizable messages for couples - Edit these in main.py
IMAGE_MESSAGES = {
    'DSCN4176.JPG': 'Insert your customized message here in main.py - IMAGE_MESSAGES dictionary',
    'IMG_0035.JPG': 'Insert your customized message here in main.py - IMAGE_MESSAGES dictionary',
    'IMG_0470.jpeg': 'Insert your customized message here in main.py - IMAGE_MESSAGES dictionary'
}

# Customizable messages for more memories - Edit these in main.py
MORE_MEMORIES_MESSAGES = {
    'IMG_3396.jpeg': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_9942.JPG': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_0293.jpeg': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_5105.JPG': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'DSCN3928.JPG': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_7441.jpeg': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_5842.JPG': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_5080.jpeg': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_9891.JPG': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_8574.JPG': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_7426.JPG': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary',
    'IMG_0073.JPG': 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary'
}

# Generic couple trivia questions - Edit these in main.py
TRIVIA_QUESTIONS = [
    {
        'question': 'What was your first date?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    },
    {
        'question': 'What is your favorite dinner date spot?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    },
    {
        'question': 'What is your favorite activity together?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    },
    {
        'question': 'When did you first realize you were falling in love?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    },
    {
        'question': 'What is your favorite movie?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    },
    {
        'question': 'What is your favorite part about your partner?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    },
    {
        'question': 'What is your favorite dessert?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    },
    {
        'question': 'What is the song that reminds you of your partner?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    },
    {
        'question': 'Who does your pet love most?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    },
    {
        'question': 'How much do you love your partner?',
        'options': ['Choice 1', 'Choice 2', 'Choice 3', 'Choice 4'],
        'correct': 'Choice 1'
    }
]

@app.route('/')
def home():
    # Get all images and their corresponding messages
    images = [f for f in os.listdir(UPLOAD_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    image_data = [(img, IMAGE_MESSAGES.get(img, 'Insert your customized message here in main.py - IMAGE_MESSAGES dictionary')) for img in images]
    return render_template('index.html', image_data=image_data)

@app.route('/more-memories')
def more_memories():
    # Get all images and their corresponding messages from the more_memories folder
    images = [f for f in os.listdir(MORE_MEMORIES_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    image_data = [(img, MORE_MEMORIES_MESSAGES.get(img, 'Insert your customized message here in main.py - MORE_MEMORIES_MESSAGES dictionary')) for img in images]
    return render_template('more_memories.html', image_data=image_data)

@app.route('/trivia')
def trivia():
    try:
        # Prepare questions with indices
        questions_with_indices = []
        for i, q in enumerate(TRIVIA_QUESTIONS):
            question = q.copy()
            question['index'] = i
            questions_with_indices.append(question)
        return render_template('trivia.html', questions=questions_with_indices)
    except Exception as e:
        print(f"Error in trivia route: {str(e)}")
        return "An error occurred. Please try again later.", 500

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/more-memories/<filename>')
def more_memories_file(filename):
    return send_from_directory(MORE_MEMORIES_FOLDER, filename)

@app.route('/check-date')
def check_date():
    # Make birthday feature accessible year-round
    return jsonify({'is_birthday': True})

@app.route('/birthday')
def birthday():
    return render_template('birthday.html')

@app.route('/birthday-game')
def birthday_game():
    return render_template('birthday_game.html')

@app.route('/birthday-card')
def birthday_card():
    return render_template('birthday_card.html')

@app.route('/api/scores', methods=['GET'])
def get_scores():
    scores = HighScore.query.order_by(HighScore.score.desc()).limit(3).all()
    return jsonify([{
        'name': score.name,
        'score': score.score,
        'date': score.date.strftime('%Y-%m-%d %H:%M:%S')
    } for score in scores])

@app.route('/api/scores', methods=['POST'])
def add_score():
    data = request.get_json()
    if not data or 'name' not in data or 'score' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    
    new_score = HighScore(
        name=data['name'],
        score=data['score']
    )
    db.session.add(new_score)
    db.session.commit()
    
    return jsonify({'message': 'Score added successfully'}), 201

if __name__ == '__main__':
    app.run(debug=False)
