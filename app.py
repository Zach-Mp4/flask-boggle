from boggle import Boggle
from flask import Flask, jsonify, render_template, session, request
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "yurr"

debug = DebugToolbarExtension(app)
boggle_game = Boggle()
board = boggle_game.make_board()

used_words = []
times_played = 0
high_score = 0

@app.route("/")
def main():
    session['board'] = board
    return render_template("base.html", board = board)

@app.route("/guess", methods=["POST"])
def guess():
    data = request.json
    g = data.get('g')
    print(g)
    if g in boggle_game.words:
        if boggle_game.check_valid_word(board, g) == "ok" and g not in used_words:
            result = {"result": "ok"}
            used_words.append(g)
            return jsonify(result)
        else:
            result = {"result": "not-on-board"}
            return jsonify(result)
    else:
        result = {"result": "not-a-word"}
        return jsonify(result)
    

@app.route("/scores", methods=['POST'])
def scores():
    global times_played
    global high_score
    data = request.json
    score = data.get('score')
    times_played += 1
    print(times_played)
    if score > high_score:
        high_score = score
    print(f"High Score: {high_score}")
    return jsonify({'output': 'success', 'highscore': high_score, 'timesplayed': times_played})

@app.route("/highscore")
def get_high_score():
    data = {'highscore': high_score}
    return jsonify(data)


    

            

