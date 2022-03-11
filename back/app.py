import warnings

from flask import Flask, jsonify, request, abort
from flask_cors import CORS
import pandas as pd

import debugTools as debug
import database


warnings.filterwarnings("ignore")

app = Flask(__name__)
cors = CORS(app)


items = []

@app.route('/api/v1.0/movies', methods=['GET'])
def get_movies():

    result = database.getMoviesByRating(51, 20, "movie")
    return jsonify({'item': result}), 201


# @app.route('/api/v1.0/etudiant', methods=['POST'])
# def create_etudiant():
#     database.createetudiant(request.json)

#     return jsonify({'item': 'etudiant cree'}), 201


if __name__ == '__main__':
    app.run(debug=True)
