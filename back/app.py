import warnings

import loadData as data
import database

import pandas as pd
import debugTools as debug

from flask import Flask, jsonify, request, abort
from flask_cors import CORS


warnings.filterwarnings("ignore")

app = Flask(__name__)
cors = CORS(app)


items = []

@app.route('/api/v1.0/etudiant', methods=['GET'])
def get_etudiants():
    debug.timelog("calling get_etudiants")

    isAttributesNull = data.getIsAttributesNull()
    isOriginalTitleNull = data.getIsOriginalTitleNull()
    isTypesNull = data.getIsTypesNull()

    datadict = {
        "isAttributesNull": isAttributesNull,
        "isOriginalTitleNull": isOriginalTitleNull,
        "isTypesNull": isTypesNull
    }

    database.getetudiants(datadict)
    result = database.resultsExportEtudiants
    return jsonify({'item': result}), 201


@app.route('/api/v1.0/etudiant', methods=['POST'])
def create_etudiant():
    database.createetudiant(request.json)

    return jsonify({'item': 'etudiant cree'}), 201


if __name__ == '__main__':
    app.run(debug=True)
