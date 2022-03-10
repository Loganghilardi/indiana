import pandas as pd
import debugTools as debug

debug.timelog("'database.py' start")

# db = MySQLdb.connect("localhost", "root", "root", "bd_notes")

resultsExportEtudiants = []
def getetudiants(datadict):

    debug.timelog("isTypesNull count:" + str(datadict["isTypesNull"].count()))
    debug.timelog("isAttributesNull count:" + str(datadict["isAttributesNull"].count()))
    debug.timelog("isOriginalTitleNull count:" + str(datadict["isOriginalTitleNull"].count()))

    item = {
        "id_etudiant": 1,
        "matricule": 2,
        "prenom": "hello",
        "nom": "there"
    }

    del resultsExportEtudiants[:]
    resultsExportEtudiants.append(item)

    return resultsExportEtudiants

# cursor = db.cursor()
# global resultsExportEtudiants
# resultsExportEtudiants = []

# def getetudiants():
    
#     debug.timelog("isTypesNull count:" + str(isTypesNull.count()))
#     debug.timelog("isAttributesNull count:" + str(isAttributesNull.count()))
#     debug.timelog("isOriginalTitleNull count:" + str(isOriginalTitleNull.count()))

#     del resultsExportEtudiants[:]
#     sql = "SELECT * FROM t_etudiant"
#     try:
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         for row in results:
#             item = {
#                 "id_etudiant": row[0],
#                 "matricule": row[1],
#                 "prenom": row[2],
#                 "nom": row[3]
#             }
#             resultsExportEtudiants.append(item)
#     except MySQLdb.Error as e:
#         try:
#             print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
#             return None
#         except IndexError:
#             print ("MySQL Error: %s" % str(e))
#             return None
#         finally:
#             cursor.close()
#             db.close()


# def createetudiant(etudiant):
#     sql = "Insert into t_etudiant(matricule, nom, prenom) values('%s', '%s', '%s')" % (etudiant['matricule'], etudiant['nom'], etudiant['prenom'])
#     try:
#         cursor.execute(sql)
#         db.commit()
#     except MySQLdb.Error as e:
#         try:
#             print ("MySQL Error [%d]: %s" % (e.args[0], e.args[1]))
#             return None
#         except IndexError:
#             db.rollback()
#             print ("MySQL Error: %s" % str(e))
#             return None
#         finally:
#             cursor.close()
#             db.close()
