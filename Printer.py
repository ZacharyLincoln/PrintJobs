import json
from json import JSONDecodeError

import certifi
import pymongo
import requests
from requests import ConnectTimeout

import database

client = pymongo.MongoClient(
        "mongodb+srv://admin:aKG8TWpv51JZJoZD@cluster0.anvlh.mongodb.net/?retryWrites=true&w=majority",
        tlsCAFile=certifi.where())
db = client.data
printer_collection = db.printers


class Printer:

    removed = False

    def __init__(self, ip, api_key, nozzle_size, color):
        self.ip = ip
        self.api_key = api_key
        self.nozzle_size = nozzle_size
        self.color = color

    def get_bed_temp(self):
        try:
            response = requests.get(url=self.ip + "/api/printer?apikey=" + self.api_key)
            data = json.loads(response.text)
        except KeyError:
            print(self.ip + " is not responding")
            return "Error"
        except JSONDecodeError:
            print("Cannot connect to octoprint")
            return "Error"
        except ConnectTimeout:
            print("Cannot connect to octoprint")
            return "Error"
        try:
            return data['temperature']['bed']['actual']
        except KeyError:
            return "Error"

    def is_printing(self):
        try:
            response = requests.get(url=self.ip + "/api/printer?apikey=" + self.api_key)
            data = json.loads(response.text)
            is_printing = data['state']['flags']['printing']
        except KeyError:
            print(self.ip + " is not responding")
            return "Error"
        except JSONDecodeError:
            print("Cannot connect to octoprint")
            return "Error"
        except ConnectTimeout:
            print("Cannot connect to octoprint")
            return "Error"

        return is_printing

    def is_ready(self):
        try:
            response = requests.get(url=self.ip + "/api/printer?apikey=" + self.api_key)
            data = json.loads(response.text)
            is_ready = data['state']['flags']['ready']
        except KeyError:
            print(self.ip + " is not responding")
            return False
        except ConnectTimeout:
            print("Cannot connect to octoprint")
            return "Error"

        return is_ready

    def upload(self):
        global printer_collection

        printer = {
            "ip": self.ip,
            "api_key": self.api_key,
            "nozzle_size": self.nozzle_size,
            "color": self.color
        }
        printer_collection.insert_one(printer)

        pass


    @staticmethod
    def download_all():
        client = pymongo.MongoClient(database.database_string, tlsCAFile=certifi.where())
        db = client.data
        printer_collection = db.printers
        printer_documents = printer_collection.find()

        printers = []
        for printer_document in printer_documents:
            printer = Printer(nozzle_size=printer_document['nozzle_size'], color=printer_document['color'], ip=printer_document['ip'], api_key=printer_document['api_key'])
            printers.append(printer)
        return printers


    def remove_from_database(self):
        printer = {
            "ip": self.ip,
            "api_key": self.api_key,
            "nozzle_size": self.nozzle_size,
            "color": self.color
        }
        printer_collection.delete_one(printer)

    @staticmethod
    def remove_from_database(ip, nozzle, color):
        printer = {
            "ip": "http://"+ip,
            "nozzle_size": float(nozzle),
            "color": color
        }
        print(printer)
        printer_collection.delete_one(printer)
