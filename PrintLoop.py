from Printer import Printer


try:
    from RemotePython import RemotePython
    RemotePython.run(path_to_requirements= "C:\\Users\\Zach\\Documents\\Development\\Python\\PrintJobs\\requirements.txt", required_files=["C:\\Users\\Zach\\Documents\\Development\\Python\\PrintJobs\\File.py", "C:\\Users\\Zach\\Documents\\Development\\Python\\PrintJobs\\Printer.py", "C:\\Users\\Zach\\Documents\\Development\\Python\\PrintJobs\\PrintJob.py", "C:\\Users\\Zach\\Documents\\Development\\Python\\PrintJobs\\database.py"], output=True)
except ImportError:
    pass


from File import File
from PrintJob import PrintJob
from time import sleep


class PrintLoop:

    print_jobs = {}
    printers = {}

    def __init__(self):
        self.print_jobs = self._get_jobs()
        self.printers = self._get_printers()
        pass

    def _get_jobs(self):
        print_jobs = PrintJob.download_all()
        return print_jobs

    def _get_printers(self):
        printers = Printer.download_all()
        return printers

    def _get_job(self, printer: Printer):
        self.print_jobs = self._get_jobs()

        for job in self.print_jobs:
            if (str(job.file.color).upper() == "ANY" or job.file.color == printer.color) and job.file.nozzle_size == printer.nozzle_size:
                return job

        print("Could not find job for", printer.ip)

    def start(self, remove_print_file: File):

        while True:
            print(self.printers)


            if self.printers == []:
                # Check database for any printers
                self.printers = self._get_printers()
                print("No Printers")

            for printer in self.printers:

                if printer.removed and not printer.is_printing() and printer.is_ready():

                    # Getting job for printer
                    job = self._get_job(printer)

                    if job:
                        job.file.print(printer)
                        print("\nStarting to print " + job.file.octoprint_path)
                        job.remove_from_database()
                        self.print_jobs.remove(job)
                        printer.removed = False
                    else:
                        # NO jobs for printer
                        # check database for more jobs
                        self.print_jobs = self._get_jobs()

                if printer.removed and printer.is_printing():
                    print("\nCurrently Printing Something... Setting removed to false")
                    printer.removed = False

                if printer.is_ready() and not printer.is_printing() and printer.get_bed_temp() < 35 and not printer.removed:
                    print("\nTrying to remove print")
                    remove_print_file.print(printer)
                    printer.removed = True
            # Sleep for 60 or more seconds.
            sleep(60)


loop = PrintLoop()
loop.start(File(octoprint_path="/local/remove.gcode", nozzle_size="ANY", color="ANY"))

