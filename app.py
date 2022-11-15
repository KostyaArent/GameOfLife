from flask import Flask, render_template, jsonify
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    game = GameOfLife()
    game.counter += 1
    return render_template('live.html', game=game)


@app.route('/api/v1.0/generation', methods=['GET'])
def get_next_generation():
    game = GameOfLife()
    game.form_new_generation()
    game.counter += 1
    return jsonify(world=game.world,
                   old_world=game.old_world,
                   counter=game.counter)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
