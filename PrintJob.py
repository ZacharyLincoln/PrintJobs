# Username: Admin
# Password: aKG8TWpv51JZJoZD
import certifi
import pymongo

import database
from File import File
from Printer import Printer

client = pymongo.MongoClient(database.database_string, tlsCAFile=certifi.where())
db = client.data
job_collection = db.jobs

class PrintJob:

    printer = ""
    file = ""

    @staticmethod
    def download_all():
        db = client.data
        job_collection = db.jobs
        jobs = job_collection.find()
        print_jobs = []
        for job in jobs:
            file = File(nozzle_size=job['nozzle_size'], color=job['color'], octoprint_path=job['octoprint_path'])
            print_jobs.append(PrintJob(file))
        return print_jobs

    def __init__(self, file: File):
        self.file = file

    def upload(self):
        job = {
            "octoprint_path": self.file.octoprint_path,
            "nozzle_size": float(self.file.nozzle_size),
            "color": self.file.color
        }

        job_collection.insert_one(job)

        pass

    def remove_from_database(self):
        print("Hiuhuihuihui")
        job = {
            "octoprint_path": self.file.octoprint_path,
            "nozzle_size": float(self.file.nozzle_size),
            "color": self.file.color
        }
        print(job)
        job_collection.delete_one(job)
