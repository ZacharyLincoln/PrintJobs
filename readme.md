
<h1 align="center">
  <br>
  <img id="logo" src="readme_assets/logo.png" alt="Logo" width="200">
  <br>
  Print Jobs
  <br>
</h1>

<h4 align="center", id="desc">A 3D printer automation solution for high production print farms.</h4>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#">Server Setup</a> •
  <a href="#">Printer Setup</a> •
  <a href="#">Client Setup</a> •
  <a href="#license">License</a>
</p>

![screenshot](./readme_assets/printjobs.gif)

## Key Features

* GUI Application for ease of use
* Cross-platform
  - Windows, macOS and Linux ready
* Lights out operation for 3d print farms
* Increase print production
* 24hr operation
* Easy to use
* Cheaper than other alternatives
* Distributed print jobs
* Print job balancing

## GUI

![screenshot](./readme_assets/rp/RP-1.png)

## Database Setup

<details>
<summary>How to set up the database</summary>

Step 0: Create an account and login to [MongoDB](https://www.mongodb.com/)


Step 1: Click "New Project"

![screenshot](./readme_assets/db/DB-1.png)

Step 2: Enter the project name. This can be anything.

![screenshot](./readme_assets/db/DB-2.png)

Step 3: Click "Build a Database"

![screenshot](./readme_assets/db/DB-3.png)

Step 4: Click "Create Project"

![screenshot](./readme_assets/db/DB-4.png)

Step 5: Click "Create". Make sure you select the free forever plan as shown

![screenshot](./readme_assets/db/DB-5.png)

Step 6: Click "Create Cluster"

![screenshot](./readme_assets/db/DB-6.png)

Step 7: Create an admin username and password. You will need this for later.

![screenshot](./readme_assets/db/DB-7.png)

Step 8: Click "Add My Current IP Address" to add your current IP address to the allowed Address list.

![screenshot](./readme_assets/db/DB-8.png)

Step 9: Click "Go to Database"

![screenshot](./readme_assets/db/DB-9.png)

Step 10: Wait for the cluster to be created.

![screenshot](./readme_assets/db/DB-10.png)

Step 11: Click "Browse Collections"

![screenshot](./readme_assets/db/DB-11.png)

Step 12: Click "Add My Own Data"

![screenshot](./readme_assets/db/DB-12.png)

Step 13: Enter "data" for the Database name and "jobs" for the collection name and click "Create"

![screenshot](./readme_assets/db/DB-13.png)

Step 14: Click the plus icon over the database name "data"

![screenshot](./readme_assets/db/DB-14.png)

![screenshot](./readme_assets/db/DB-15.png)

Step 15: Enter "printers" in the collection name and click "Create".

![screenshot](./readme_assets/db/DB-16.png)

![screenshot](./readme_assets/db/DB-17.png)

Congratulations you have finished the database set up!



</details>

## Server Setup

Please follow the following instructions to set up [Remote Python](https://github.com/ZacharyLincoln/RemotePython) on your server and client.

[Remote Python - Server Setup](https://github.com/ZacharyLincoln/RemotePython#how-to-set-up-remote-python-server)

[Remote Python - Client Setup](https://github.com/ZacharyLincoln/RemotePython#run-any-python-script-with-external-requirements)

## Printer Setup
<details>
<summary>How to setup a printer</summary>

### Printer setup that has been tested and working

[Ender 3 V2](https://www.creality3dofficial.com/products/ender-3-v2-3d-printer)

This is the 3D printer that this project was tested on... any printer with a heated bed should work.

[CR Touch](https://www.amazon.com/dp/B09DVYZSYJ?psc=1&ref=ppx_yo2ov_dt_b_product_details)

The CR Touch ensures that the bed is level and that the print is constantly a certain distance away from the bed allowing it to delaminates from the bed when it cools.

[Spring Steel Build Plate](https://www.amazon.com/dp/B088841XH9?ref=ppx_yo2ov_dt_b_product_details&th=1)

Allows for adhesion while the build plate is heated and delaminates when the build plate is cool.

[Octoprint](https://octoprint.org/)

Allows for the printer to be controlled remotely by this program.


### All you need to set up a printer for automation is to download and setup octoprint on the printer.

In order to download and setup octoprint follow directions on [octoprint.org](https://octoprint.org/download/) to download and setup octoprint.
</details>


## Client Setup

### Add printer
<details>
<summary>How to add a printer</summary>
Step 1: Click "Add Printer"

![screenshot](./readme_assets/cp/CP-1.png)

![screenshot](./readme_assets/cp/CP-2.png)

Step 2: Add the ip, octoprint api key nozzle size and color of filament that is on the printer.

![screenshot](./readme_assets/cp/CP-3.png)

Step 3: Click "Create printer"

![screenshot](./readme_assets/cp/CP-4.png)

Step 4: Click "Refresh" on the bottom right to reload the printers.

![screenshot](./readme_assets/cp/CP-1.png)

![screenshot](./readme_assets/cp/CP-6.png)
</details>

### Remove printer
<details>
<summary>How to remove a printer</summary>
Step 1: Click Highlight the printer you want to delete.

![screenshot](./readme_assets/dp/DP-1.png)

![screenshot](./readme_assets/dp/DP-2.png)

Step 2: Click "Remove Printer"

![screenshot](./readme_assets/dp/DP-3.png)

Step 3: Click "Refresh" on the bottom right to reload the printers.

![screenshot](./readme_assets/dp/DP-4.png)

</details>

### Remove print script
![screenshot](./readme_assets/remove.gif)

### Add print job

<details>
<summary>How to Add a print job</summary>

Step 1: Click on the file you wish to print

![screenshot](./readme_assets/ap/AP-1.png)

Step 2: Enter the quantity you wish to print

![screenshot](./readme_assets/ap/AP-2.png)

Step 3: Select the color you want the print to be printed in, and the correct nozzle size for the file.

![screenshot](./readme_assets/ap/AP-4.png)

Step 4: Click "Add --->"

![screenshot](./readme_assets/ap/AP-5.png)

![screenshot](./readme_assets/ap/AP-6.png)

</details>

### Remove print job
<details>
<summary>How to Remove a print job</summary>

Step 1: Click the job you wish to remove

![screenshot](./readme_assets/rp/RP-2.png)

Step 2: Click "<--- Remove"

![screenshot](./readme_assets/rp/RP-3.png)

</details>

## License

MIT

---
> [zlincoln.dev](https://www.zlincoln.dev) &nbsp;&middot;&nbsp;
> GitHub [@ZacharyLincoln](https://github.com/ZacharyLincoln)

