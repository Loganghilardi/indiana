import debugTools as debug
import pandas as pd

debug.timelog("'title.akas.tsv' loading")
dataTitleAkas = pd.read_csv(
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

isTypesNull = dataTitleAkas.loc[dataTitleAkas["types"] == "\\N", "titleId"]
debug.timelog("'isTypesNull' OK")
isAttributesNull = dataTitleAkas.loc[dataTitleAkas["attributes"] == "\\N", "titleId"]
debug.timelog("'isAttributesNull' OK")
isOriginalTitleNull = dataTitleAkas.loc[dataTitleAkas["isOriginalTitle"] == "\\N", "titleId"]
debug.timelog("'isOriginalTitleNull' OK")


def getTitleAkas():
  return dataTitleAkas

def getIsTypesNull():
  return isTypesNull

def getIsAttributesNull():
  return isAttributesNull

def getIsOriginalTitleNull():
  return isOriginalTitleNull
