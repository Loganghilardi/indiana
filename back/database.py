import pandas as pd
import debugTools as debug
import loadData as data

results = []
def getetudiants():

    getMovies(5000, 20)

    # #test 1
    # titleBasics = data.getTitleBasics()
    # titleCrew = data.getTitleCrew()
    # pTitleBasics = titleBasics.loc[0:19, ["tconst", "primaryTitle", "originalTitle", "titleType", "genres"]]
    # fTitleBasics = pd.merge(pTitleBasics, titleCrew, how='left', on='tconst')

    # test 2
    # titleCrew = data.getTitleCrew()
    # processedCrew = titleCrew[titleCrew["directors"].str.contains(",")].reset_index().loc[1:50]
    # processedCrew["directors"] = processedCrew["directors"].str.split(",")
    # processedCrew["writers"] = processedCrew["writers"].str.split(",")
    # # calc = processedCrew[processedCrew["writers"].str.contains("\\N")]
    # debug.timelog("Count:" + str(processedCrew.count()))

    # test 3
    # df = pd.DataFrame({
    #     "a": [1,2,3,4,5],
    #     "b": ["hello", "there", ["hehe", "haha"], "welcome", "bonjour"]
    # })
    # print(df)
    # print(df.dtypes)
    # print(df.loc[2, "b"][1])

    item = {
        "id_etudiant": 1,
        "matricule": 2,
        "prenom": "hello",
        "nom": "there"
    }

    del results[:]
    results.append(item)

    return results

def getMovies(start, perPage):
    debug.timelog("getMovies start")
    titleBasics = data.getTitleBasics()
    debug.timelog("getTitleBasics()")
    titleCrew = data.getTitleCrew()
    debug.timelog("getTitleCrew()")

    pTitleBasics = titleBasics[titleBasics["titleType"].str.contains("movie")].reset_index().loc[
        start:start + perPage,
        ["tconst", "primaryTitle", "originalTitle", "titleType", "genres"]
        ]
    debug.timelog("pTitleBasics")
    
    fTitleBasics = pd.merge(pTitleBasics, titleCrew, how='left', on='tconst')
    debug.timelog("fTitleBasics")

    fTitleBasics["directors"] = fTitleBasics["directors"].str.split(",")
    fTitleBasics["writers"] = fTitleBasics["writers"].str.split(",")
    fTitleBasics["genres"] = fTitleBasics["genres"].str.split(",")
    debug.timelog("formatting")

    debug.timelog("fTitleBasics:")
    print(fTitleBasics)

