#coding=utf-8
from csv import reader
import cyrtranslit
from flask_pymongo import MongoClient

# Instantiate mongo database
mongo = MongoClient()

# Create mongo database
db = mongo.datacentar

class ImportingManager(object):

    def __init__(self):
        pass

    def data_importer_of_municipality_pripolje(self):
        pass

    def data_importer_of_municipality_vranje(self):
        pass

    def data_importer_of_municipality_loznitsa(self):
        pass

    def data_importer_of_municipality_sombor(self):
        pass

    def data_importer_of_municipality_valjevo(self):
        pass

    def data_importer_of_municipality_indjija(self):
        pass

    def data_importer_of_municipality_cacak(self):
        print "cacak"

    def data_importer_of_municipality_krajlevo(self):
        pass

    def data_importer_of_municipality_zavezdara(self):
        pass

    def data_importer_of_municipality_novi_beograd(self):
        data = reader(open("data/novi_beograd.csv", "r"), delimiter=",")

        parent_handler = ''
        for index, row in enumerate(data):
            if index > 0:
                if len(row[1]) == 2:
                    parent_handler = row[2]

                if len(row[1]) > 2 and row[2] not in ["", " "]:
                    json_doc = self.build_mongo_document_structure("Нови Београд", parent_handler, row[1][0:2], row[1], row[2], row[3], row[4], row[5], row[6])
                    db.opstine.insert(json_doc)
                    print "Opstine: Нови Београд - Kategorija Roditelj: %s - Opis: %s" % (parent_handler, row[2])

    def build_mongo_document_structure(self, muncipality, kategorija_roditelj, roditelj_broj, class_number, opis, prihodi_vudzeta, sopstveni_prihodi, donacije, ostali):

        ukupno = prihodi_vudzeta + sopstveni_prihodi + donacije + ostali
        json_doc = {
            "opstina": {
                "cyrilic": muncipality,
                "latin": cyrtranslit.to_latin(muncipality, "sr")
            },
            "kategorijaRoditelj": {
                "opis": kategorija_roditelj,
                "broj": roditelj_broj
            },
            "klasifikacijaBroj": class_number,
            "opis": {
                "latin": cyrtranslit.to_latin(opis, "sr"),
                "cyrilic": opis.strip()
            },
            "prihodiVudzeta": prihodi_vudzeta,
            "sopstveniPrihodi": sopstveni_prihodi,
            "donacije": donacije,
            "ostali": ostali,
            "ukupno": ukupno
        }

        return json_doc