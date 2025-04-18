from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

number = random.randint(1, 100)  # Random number between 1 and 100
count = 0  # Counter for number of guesses
name = None  # To store the player's name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    global number, count, name

    # Ensure that name is provided in the JSON request
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'message': 'Error: Name is required to start the game.'}), 400

    name = data.get('name')  # Get player name from the request
    number = random.randint(1, 100)  # Generate a new random number
    count = 0  # Reset guess count
    return jsonify({'message': f"Hello {name}! Let's play the game. Guess the number between 1 and 100!"})

@app.route('/submit_guess', methods=['POST'])
def submit_guess():
    global count, number, name

    # Ensure that guess is provided and is valid
    data = request.json
    if not data or 'guess' not in data:
        return jsonify({'message': 'Error: Guess is required.'}), 400
    
    try:
        guess = int(data.get('guess'))
    except ValueError:
        return jsonify({'message': 'Error: Guess must be an integer.'}), 400

    count += 1
    message = ""

    if guess > number:
        message = "Wrong! Your guess is too high."
    elif guess < number:
        message = "Wrong! Your guess is too low."
    else:
        message = f"Congratulations {name}! You guessed the number in {count} guesses."

    if count >= 6 and guess != number:
        message = f"Game over! You've used all guesses. The number was {number}."

    return jsonify({'message': message, 'count': count})

if __name__ == '__main__':
    app.run(debug=True)
