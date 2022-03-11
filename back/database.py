import pandas as pd
import debugTools as debug
import loadData as data
import json

results = []

def getMoviesByRating(start, perPage):
    debug.timelog("getMoviesByRating start")
    df = data.getTitleSortByRatings()
    df = df.loc[start:start + perPage - 1]

    print(df)
    df.to_json(r'test.json', orient="records")

    json_file_path = "test.json"

    with open(json_file_path, 'r') as j:
        contents = json.loads(j.read())

    del results[:]
    results.append(contents)

    debug.timelog("getMovies end")
    return results


