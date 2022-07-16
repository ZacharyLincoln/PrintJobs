import os

import requests


class File:
    octoprint_path = "/local/filename"
    local_path = ""
    file_name = ""
    nozzle_size = ""
    color = ""


    def __init__(self, nozzle_size, color, local_path=None, file_name=None, octoprint_path=None):
        self.octoprint_path = octoprint_path
        self.local_path = local_path
        self.file_name = file_name
        self.nozzle_size = nozzle_size
        self.color = color

        if self.file_name is None:
            self.file_name = str(local_path).split("\\")[len(str(local_path).split("\\"))-1]

    def is_uploaded(self, printer):
        # Checks to see if the file is uploaded
        headers = {
            "X_Api_Key": printer.api_key
        }

        response = requests.get(printer.ip + "/api/files/local/" + str(self.file_name), headers=headers)
        print(response.url)

        if response.status_code == 404:
            print("Print is not uploaded!!!")
            return False
        elif response.status_code == 200:

            print("Print is uploaded!!!")
            return True

    def upload_to_octoprint(self, printer):
        local_path = self.local_path

        size = os.path.getsize(local_path)
        headers = {
            "X_Api_Key": printer.api_key,
            "Content-Length": str(size),
        }

        data = {
            "name": "file",
            "filename": self.file_name
        }

        file_to_upload = open(local_path, "rb")
        # Content-Disposition: form-data; name="file"; filename="CE3PRO_Funky Krunk.gcode"
        response = requests.post(printer.ip + "/api/files/local", files={'file': file_to_upload},
                                 headers=headers, data=data)
        #print(response.text)

        self.octoprint_path = "local/" + self.file_name

    def print(self, printer):
        params = {"command": "select", "print": True}
        print(printer.ip + "/api/files/"+self.octoprint_path)
        response = requests.post(headers={"X_Api_Key": printer.api_key},
                                 url=printer.ip + "/api/files/"+self.octoprint_path, json=params)
        print(response.status_code)


