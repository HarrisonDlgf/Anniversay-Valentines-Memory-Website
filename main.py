from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

# Create uploads directory if it doesn't exist
UPLOAD_FOLDER = 'static/uploads'
MORE_MEMORIES_FOLDER = 'static/more_memories'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(MORE_MEMORIES_FOLDER):
    os.makedirs(MORE_MEMORIES_FOLDER)

# map file names to messages
IMAGE_MESSAGES = {
    'DSCN4176.JPG': 'The weekend we got to play house to the max. I loved being at BPG with you and your friends, soaking up the sun, and just spending time with my favorite girls.',
    'IMG_0035.JPG': 'It was a dream come true getting to be a knight for a day with my favorite princess. Just know that I would joust and kick some major ass for you.',
    'IMG_0470.jpeg': 'Some of my favorite memories are when we decide to take an adventure together. Also, I love that you are so clearly lactose intolerant yet are always down to get some friendlies cups, pizza, or my new favorite, mozarella sticks.'
}

# Dictionary for more memories messages (to be filled later)
MORE_MEMORIES_MESSAGES = {
    'IMG_3396.jpeg': 'A photo I had to take even though we had just met. I fell for you so hard that night and with a little liquid courage, even held your hand. I didnt care where I ended up that night as long as it was with you. Forever star gazing with you <3',
    'IMG_9942.JPG': 'We finally got out for a hike in the Blue Hills since you were ever so curious about Milton and its beautiful landscape. You make everything so special',
    'IMG_0293.jpeg': 'This food fucking hit. But for dessert, I got to stare across the table at my crush. Even when we dont have plans, our nights always end perfectly and sometimes even end up with gas food. Run it back soon?',
    'IMG_5105.JPG': 'I finally got to take a gorgeous girl, who by the way was wearing the hell out of that dress, to my semi-formal. This is where my friends also fell for you, overwhelmingly so. I couldnt find photos but this made me think of that time we had wine night with them and we snuck off to study! Study in my room!',
    'DSCN3928.JPG': 'All the way to actual formal. Pink eye from the water park aside this was a perfect day and a perfect weekend. Being in the cape with you was absolutely splendid, from great foods, to foam soap, to arcading where you won me my first ever Claw machine win!',
    'IMG_7441.jpeg': 'Dinners and drinks with Paulinas family. We are such a perfect pairing Mia, I cant believe a pretty girl like you wants to sip ciders and cocktails with me.',
    'IMG_5842.JPG': 'Our Salem day was the perfect send off. The best Christmas gift I couldve ever asked for. You kicked my butt in that buck shooting game, I demand a rematch. And yes we should probably stay far away from real witches',
    'IMG_5080.jpeg': 'I cant believe I had to meet your mom basically 2 days into being your boyfriend. What a daunting task that turns out to have been really easy. I love Falls Church and all of your family friends, everyone is so kind and accepting. Also this was one of the first times I got to hear you sing, and your voice is so heavenly. I sat with Linneas friend and kept beaming with pride on how you were my girlfriend and how talented you are.',
    'IMG_9891.JPG': 'Tama and our disastrous fish cake. Yet, I still loved this date night. Plus, you look so radiant in this photo I cant help but include this. I love just eating good food, splitting appetizers and loving you. Talking the night away is just so easy when its with you.',
    'IMG_8574.JPG': 'Our cape night before formal we got this blizzards which were admittably a little too big for us but Ill always supersize our ice creams in case we ever need it. We got to walk to the beach, explore downtown, and I got to show you all of the places I cant wait to be with you this summer when the weather is perfect',
    'IMG_7426.JPG': 'My weekend at the Mayers! God I really do love your family, they are so nice and accepting of me it feels like a second home. Cuddling on the couch with you watching Friends, driving to your gas station where high school you went to get drinks, and going to sports games, whether its DC United, the Capitals (of which I am a big fan now), or your brothers indoor soccer league, I love being with you. Thank you for giving me a second home Mia.',
    'IMG_0073.JPG': 'Our first family trip together to West Virginia and man did it crush my expectations. I was devastated when I first went to Baltimore and I remember when you called me with the news, I almost cried tears of excitement. The skiing, the lost phone, the delicious waffle cabin trips and hanging out with everyone for game nights, mid day snack breaks or XO Kitty watch sessions really made me feel like I belonged. I love you so much Mia.'
}

# Trivia questions
TRIVIA_QUESTIONS = [
    {
        'question': 'What was our first date?',
        'options': ['Coffee at Starbucks', 'Dinner at Olive Garden', 'Thrifting at Goodwill', 'Movie night'],
        'correct': 'Coffee at Starbucks'
    },
    {
        'question': 'What is my favorite dinner date (for the food)?',
        'options': ['Chinese in Quincy', 'Chilis', 'Franks Pizza and Pasta', 'North End Pasta Dish'],
        'correct': 'Chinese in Quincy'
    },
    {
        'question': 'What is my favorite activity together?',
        'options': ['Watching White Lotus', 'Camping', 'Hiking', 'Jamming to music while driving'],
        'correct': 'Jamming to music while driving'
    },
    {
        'question': 'When did I fall for you?',
        'options': ['At Olivias', 'Through DMs', 'Holding your hand after FIJI', 'Brocolli Cheddar Soup incident'],
        'correct': 'At Olivias'
    },
    {
        'question': 'What is my favorite movie?',
        'options': ['Fantastic Mr. Fox', 'Titanic', 'La La Land', 'Manchester by the Sea'],
        'correct': 'Fantastic Mr. Fox'
    },
    {
        'question': 'What is my favorite part about you?',
        'options': ['Your never ending work ethic', 'Your beautiful smile', 'Your sense of humor', 'All of the above, how you light up a room'],
        'correct': 'All of the above, how you light up a room'
    },
    {
        'question': 'What is my favorite dessert?',
        'options': ['Fudgepops', 'Boston Cream Donuts', 'Your brown sugar cookies', 'Friendlies Ice Cream Cake Cups'],
        'correct': 'Friendlies Ice Cream Cake Cups'
    },
    {
        'question': 'What is the song that reminds me of you?',
        'options': ['I Wish I Was - The Avett Brothers', 'Maine - Noah Kahan', 'Shake The Frost - Tyler Childers', 'Im Yours'],
        'correct': 'Shake The Frost - Tyler Childers'
    },
    {
        'question': 'Who does Cleo love most?',
        'options': ['Me', 'Mia Mayer', 'My mom', 'Pup Cups'],
        'correct': 'Mia Mayer'
    },
    {
        'question': 'How much do I love you?',
        'options': ['Infinitely', 'Beyond human comprehension', 'A little', 'So much it makes my heart hurt'],
        'correct': 'So much it makes my heart hurt'
    }
]

@app.route('/')
def home():
    # Get all images and their corresponding messages
    images = [f for f in os.listdir(UPLOAD_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    image_data = [(img, IMAGE_MESSAGES.get(img, 'This is a special memory!')) for img in images]
    return render_template('index.html', image_data=image_data)

@app.route('/more-memories')
def more_memories():
    # Get all images and their corresponding messages from the more_memories folder
    images = [f for f in os.listdir(MORE_MEMORIES_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    image_data = [(img, MORE_MEMORIES_MESSAGES.get(img, 'This is a special memory!')) for img in images]
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

if __name__ == '__main__':
    app.run(debug=False)
