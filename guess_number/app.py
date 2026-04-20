from flask import Flask, jsonify, render_template, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/game")
def game():
    return render_template("game.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

@app.route("/start")
def start_game():
    session["secret_number"] = random.randint(1, 50)
    session["attempts"] = 0
    return jsonify({"message": "Game started! Guess wisely 😎"})

@app.route("/guess/<int:num>")
def guess(num):
    if "secret_number" not in session:
        return jsonify({
            "message": "Start the game first!",
            "result": "error",
            "attempts": 0
        })

    session["attempts"] += 1
    secret_number = session["secret_number"]
    attempts = session["attempts"]

    if num < secret_number:
        return jsonify({"message": "Too low! Try higher 🔼", "result": "low", "attempts": attempts})
    elif num > secret_number:
        return jsonify({"message": "Too high! Try lower 🔽", "result": "high", "attempts": attempts})
    else:
        return jsonify({"message": f"🎉 You won in {attempts} attempts!", "result": "win", "attempts": attempts})

if __name__ == "__main__":
    app.run(debug=True)