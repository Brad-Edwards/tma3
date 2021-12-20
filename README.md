COMP482 TMA3
============
Assignment 3
============

Requirements
------------

The project can be run on Ubuntu or similar distributions, whether natively, in a VM or through the Windows
Subsystem for Linux 2. If you are using Windows and have not already installed WSL2 and Ubuntu, please follow the
directions at the following link:

https://docs.microsoft.com/en-us/windows/wsl/install

Docker and Docker-Compose

Docker and Docker-Compose are required to run the project. Follow the instructions at the following two links if you
do not have these already installed (they are not installed in Ubuntu by default):

https://docs.docker.com/engine/install/ubuntu/
https://docs.docker.com/compose/install/

Git

If you wish to download the project using git, you will need to have git installed. Just run the following in your
Ubuntu command line (in Windows, open a normal terminal and enter 'ubuntu' to start WSL2):

sudo apt-get install git

unzip

sudo apt-get install unzip

Installation
------------

Open a Ubuntu terminal (in Windows, open a normal terminal and enter 'ubuntu' to start WSL2).

1. Get project

If you want to clone the project using git, create and navigate to your target directory and use the following command:

git clone https://github.com/Brad-Edwards/tma3.git

Zip

You can download a zip file of the project from the Ubuntu command line. Create and navigate to a target directory.
Then use the following command:

wget https://github.com/Brad-Edwards/tma3/archive/refs/heads/main.zip

You can then unzip the project with the following command:

unzip main.zip

If you would rather download the project as a .zip file in a browser, it is available at
https://github.com/Brad-Edwards/tma3/archive/refs/heads/main.zip. Unzip the file in a target location.

2. Build project

If you cloned the project from GitHub, navigate into the tma3/comp482_tma3 folder of the project. If you used the
 zip file, navigate to tma3_main/comp482_tma3.

Build the project with the following command:

docker-compose -f local.yml build

The build process will take some time, however all dependencies will be downloaded other than the requirements
mentioned previously. You do not even need to worry about your Python version.

3. Run project

Wait for the project to finish building. If you cloned the project from GitHub, navigate into (or stay in)
the tma3/comp482_tma3 folder of the project. If you downloaded the zip file navigate to (or stay in)
tma3_main/comp482_tma3.

docker-compose -f local.yml up

You are ready to mark the prototype once django reports the server is running at http://0.0.0.0:8000/

The staff tasks (1, 4-6) are available at:

localhost:8000/roots/landing

The parent tasks (2-3) are available at:

localhost:8000/roots/parent_landing
