import debugTools as debug
import pandas as pd

loadNameBasics = False
loadTitleAkas = False
loadTitleBasics = True
loadTitleCrew = True
loadTitleEpisode = False
loadTitlePrincipals = False
loadTitleRatings = False

# load sequence
# raw data
if loadNameBasics:
  debug.timelog("'name.basics.tsv' loading")
  nameBasics = pd.read_csv(
      "data/name.basics.tsv",
      sep="\t",
      dtype={
          "nconst": "object",
          "primaryName": "object",
          "birthYear": "object",
          "deathYear": "object",
          "primaryProfession": "object",
          "knownForTitles": "object",
          }
      )
  debug.timelog("'name.basics.tsv' OK")
else:
  nameBasics = pd.DataFrame()
  debug.timelog("'name.basics.tsv' created empty")


if loadTitleAkas:
  debug.timelog("'title.akas.tsv' loading")
  titleAkas = pd.read_csv(
      "data/title.akas.tsv",
      sep="\t",
      dtype={
          "titleId": "object",
          "ordering": "int64",
          "title": "object",
          "region": "object",
          "language": "object",
          "types": "object",
          "attributes": "object",
          "isOriginalTitle": "object"
          }
      )
  debug.timelog("'title.akas.tsv' loaded")
else:
  titleAkas = pd.DataFrame()
  debug.timelog("'title.akas.tsv' created empty")
  

if loadTitleBasics:
  debug.timelog("'title.basics.tsv' loading")
  titleBasics = pd.read_csv(
      "data/title.basics.tsv",
      sep="\t",
      dtype={
          "tconst": "object",
          "titleType": "object",
          "primaryTitle": "object",
          "originalTitle": "object",
          "isAdult": "object",
          "startYear": "object",
          "endYear": "object",
          "runtimeMinutes": "object",
          "genre": "object"
          }
      )
  debug.timelog("'title.basics.tsv' loaded")
else:
  titleBasics = pd.DataFrame()
  debug.timelog("'title.basics.tsv' created empty")
  

if loadTitleCrew:
  debug.timelog("'title.crew.tsv' loading")
  titleCrew = pd.read_csv(
      "data/title.crew.tsv",
      sep="\t",
      dtype={
          "tconst": "object",
          "directors": "object",
          "writers": "object",
          }
      )
  debug.timelog("'title.crew.tsv' loaded")
else:
  titleCrew = pd.DataFrame()
  debug.timelog("'title.crew.tsv' created empty")
  

if loadTitleEpisode:
  debug.timelog("'title.episode.tsv' loading")
  titleEpisode = pd.read_csv(
      "data/title.episode.tsv",
      sep="\t",
      dtype={
          "tconst": "object",
          "parentTconst": "object",
          "seasonNumber": "object",
          "episodeNumber": "object"
          }
      )
  debug.timelog("'title.episode.tsv' loaded")
else:
  titleEpisode = pd.DataFrame()
  debug.timelog("'title.episode.tsv' created empty")


if loadTitlePrincipals:
  debug.timelog("'title.principals.tsv' loading")
  titlePrincipals = pd.read_csv(
      "data/title.principals.tsv",
      sep="\t",
      dtype={
          "tconst": "object",
          "ordering": "int64",
          "nconst": "object",
          "category": "object",
          "job": "object",
          "characters": "object"
          }
      )
  debug.timelog("'title.principals.tsv' loaded")
else:
  titlePrincipals = pd.DataFrame()
  debug.timelog("'title.principals.tsv' created empty")


if loadTitleRatings:
  debug.timelog("'title.ratings.tsv' loading")
  titleRatings = pd.read_csv(
      "data/title.ratings.tsv",
      sep="\t",
      dtype={
          "tconst": "object",
          "averageRatings": "object",
          "numVotes": "object"
          }
      )
  debug.timelog("'title.ratings.tsv' loaded")
else:
  titleRatings = pd.DataFrame()
  debug.timelog("'title.ratings.tsv' created empty")


# getters
def getNameBasics():
  return nameBasics

def getTitleAkas():
  return titleAkas

def getTitleBasics():
  return titleBasics

def getTitleCrew():
  return titleCrew

def getTitleEpisode():
  return titleEpisode

def getTitlePrincipals():
  return titlePrincipals

def getTitleRatings():
  return titleRatings
