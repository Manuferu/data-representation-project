# data-representation-project
Repo with the material for data representation project.

## Cars database

In this project, it has been created a car registration in a database. this database is displayed in an html file thanks to the server.
The user will be able to create update and delete car registration.

## How to use it

In order to execute it in your localhost, you need to clone the repo. Then you need to execute the server file in your terminal "**python server.py**".
Once the server is running, you need to copy paste the url coming out from your terminal in your browser.

If everything goes well, you will be able to successfully use the web portal.

## Contents of the folder.

- **Staticpages**
    - ***index.html*** : html file where the user will find the structure of the web site to interact and populate the database.
    - **Images** :  Folder with images used in the html file

- **carsDAO.py** : file where it is written the API designed with all functions to iteract with the content (how to create, delete, update content...).

- **testcarsDAO.py** : file where to try the API functionalities.

- **server.py** : server file written using flask. Needed to sync database and web site

- **config.py** :  Configuration file

- **specifications.txt** : file containing a copy of the environment used in my laptop to develop the project. In case you want to replicate the environment, please open copy this environment in your laptop.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
