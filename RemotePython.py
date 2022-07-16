import inspect
import os
import socket

import paramiko
from scp import SCPClient
from time import sleep


class RemotePython:

    ssh = ""
    scp = ""



    @staticmethod
    def install_requirements(path_to_requirements, ssh, scp):
        scp.put(path_to_requirements, "~/serv/python-remote/" + path_to_requirements.split("\\")[len(path_to_requirements.split("\\")) - 1])

        print("Installing requirements")
        stdin, stdout, stderr = ssh.exec_command("pip install -r ~/serv/python-remote/requirements.txt", get_pty=True)

        for line in iter(lambda: stdout.readline(2048), ""):
            print(line, end="")

        exit_status = stdout.channel.recv_exit_status()
        if exit_status == 0:
            print("Requirements installed")
        else:
            print("Error", exit_status)

    @staticmethod
    def output_console(ssh, session_name, filename, ip):

        try:
            # Show output to user.....
            old_lines = []
            while True:
                stdin, stdout, stderr = ssh.exec_command("tmux capture-pane -pt " + session_name + " -S -")
                i = 0
                for line in stdout.readlines():
                    line = str(i) + " " + line
                    if line == str(i) + " \n" or line in old_lines:
                        pass
                    else:

                        print(line, end="")
                        old_lines.append(line)
                    i += 1

                sleep(1)
        except KeyboardInterrupt:
            # User has stopped script CNTL-C...
            print("Stopping output.....")

            while True:
                # Ask user if they want to keep the script running on the server.
                keep_running = input("Would you like to keep " + filename + " running on " + ip + "? Y/n: ")

                # User wants to keep the script running
                if keep_running.upper() == "Y":
                    print(filename + " is still running on " + ip)
                    ssh.close()
                    exit()

                # User wants to stop/kill the script currently running.
                elif keep_running.upper() == "N":
                    print("Killing " + filename + " on " + ip)
                    stdin, stdout, stderr = ssh.exec_command("tmux kill-session -t " + session_name)
                    exit_status = stdout.channel.recv_exit_status()
                    if exit_status == 0:
                        print("Killed " + filename + " on " + ip)
                    else:
                        print("Error", exit_status)

                    ssh.close()
                    exit()

    @staticmethod
    def run(server_hostname="python-runner", path_to_script="", path_to_requirements="", required_files="", output=False):

        # Check to see if user supplied a filename
        if path_to_script == "":
            # Get the filename of the script that called this function
            frame = inspect.stack()[1]
            module = inspect.getmodule(frame[0])
            path_to_script = module.__file__

        # Get the name of the file that contains the script.
        filename = path_to_script.split("\\")[len(path_to_script.split("\\")) - 1]

        # Get the username from the environmental variable PYTHON_SERVER_USER
        username = os.getenv('PYTHON_SERVER_USER')

        # Get the password from the environmental variable PYTHON_SERVER_PASS
        password = os.getenv('PYTHON_SERVER_PASS')

        # Get the ip on the server from the environmental variable PYTHON_SERVER_IP
        ip = os.getenv('PYTHON_SERVER_IP')

        # Get the hostname of the computer/server running this script.
        hostname = socket.gethostname()

        # Check to see if the hostname is the same as the hostname as the specified server
        if hostname == server_hostname:
            # Return and run the rest of the script
            return

        # Create an ssh and scp connection to the server.
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)
        scp = SCPClient(ssh.get_transport())

        # Make the directory ~/serv/python-remote if it has not been created already
        ssh.exec_command("mkdir serv")
        ssh.exec_command("mkdir serv/python-remote")

        # Install requirements
        if not path_to_requirements == "":
            RemotePython.install_requirements(path_to_requirements, ssh, scp)

        if not required_files == "":

            ssh.exec_command("mkdir serv/python-remote/" + filename.replace(".py", ""))

            for file in required_files:
                scp.put(file, "~/serv/python-remote/" + filename.replace(".py", "") + "/" + file.split("\\")[len(file.split("\\")) - 1])



            # C:\Users\Zach\Documents\Development\Python\RemotePython
            # C:\Users\Zach\Documents\Development\Python\RemotePython\main.remote.py
            filename = filename.replace(".py", "") + "/" + filename

            print("Uploaded")

            # Run script in parent folder


        # Transfer over the file that the user wants to run via scp.
        scp.put(path_to_script, "~/serv/python-remote/" + filename)

        # Generate a session name that will be used with tmux.
        session_name = path_to_script.split("\\")[len(path_to_script.split("\\")) - 1].replace(".py", "").replace(".", "_")

        # If there is a session with the same session name kill it and replace it with a new session.
        ssh.exec_command("tmux kill-session -t " + session_name)
        ssh.exec_command("tmux new-session -d -s " + session_name +" 'python3 ~/serv/python-remote/" + filename + "'")

        print("tmux new-session -d -s " + session_name +" 'python3 ~/serv/python-remote/" + filename + "'")
        # Let the user know that the script is running on the server.
        print("Running " + filename + " on " + ip)

        if output:
            print("Outputting console....")
            RemotePython.output_console(ssh, session_name, filename, ip)

        exit()

