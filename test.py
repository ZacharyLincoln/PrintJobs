from File import File
from PrintJob import PrintJob
from Printer import Printer

#TODO When uploading a file makes sure that the file is uploaded to every printer........

octoprint_ip = "http://10.0.0.210"
api_key = "1DB7593530564EE690098DA09A3FC1CD"
nozzle_size = 0.4
color = "black"
printer = Printer(octoprint_ip, api_key, nozzle_size=nozzle_size, color=color)
#printer.upload()

octoprint_ip = "http://10.0.0.151"
api_key = "A5F0A5AEBE594DC3B9E0CD7DB8BA3E16"
nozzle_size = 0.4
color = "black"
printer = Printer(octoprint_ip, api_key, nozzle_size=nozzle_size, color=color)
#printer.upload()



nozzle_size = 0.4
color = "black"
beep_file = File(nozzle_size, color, local_path="C:\\Users\\Zach\\Documents\\3D_Printing\\3D_Printing_Production_Files\\beep.gcode")
beep_file.upload_to_octoprint(printer)

job = PrintJob(beep_file)
job.upload()

printer = Printer(octoprint_ip,api_key,nozzle_size,color)
beep_file = File(nozzle_size, color, local_path="C:\\Users\\Zach\\Documents\\3D_Printing\\3D_Printing_Production_Files\\beep.gcode")
beep_file.upload_to_octoprint(printer)

job = PrintJob(beep_file)
job.upload()
