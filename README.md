# Graphide
Online graph plotting system part of Investigatory project for class 12 Computer science student. Using the concept Django requests ,JS rendering , Matplotlib etc.

[Demo Video](https://github.com/Theskyspace/Graphide/blob/main/VID_20190920_215011.mp4)

# What it does?
It takes complex mathematical equations and visualizes them in the form of graphs for visual learning.

## Install dependencies ?
Dependances that you need to install for this build is as follows.
You need to have pip [install](https://pip.pypa.io/en/stable/installing/) in your system.

After pip is succesfully installed you can install the modules required with the following commands\
`pip install matplotlib`\
`pip install django`\
`pip install mpld3`

and you are good to go.

## Build the Project
To build the project cd into the main directory and pass in the following command.

`python manage.py runserver`

The project will be hosted in your local host.

## More about the project.
So basically how this project works is it fetches the input using GET commands computes it in the python backend using matplotlib and reders it using mpld3 JS redering module.
