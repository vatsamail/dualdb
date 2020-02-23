# dualdb
A method to develop Django based web apps with more than one database. And one of the databases being NoSQL!

## Installation:
- Install Python 3.7.x
- Create Virtual Environment
- pip install -r requirements.txt
- Copy djongo folder from C:\my\ml\virtualenv\dualdb\env\Lib\site-packages\djongo to env\Lib\site-packages\django\db\backends\djongo

## Projects
This repository contains two projects. Viz., Portal and Prj.

#### Portal
- Uses djongo (MongoDB nosql), both in native form and through mongo-Atlas. For mongo connection, one has to create the account and update the username and password accordingly in the portal.settings file (hint: Replace: xxx)
- Contains blog app
- Supports admin

#### Prj
- Developed to use multiple databases simultaneously.
- For larger and non-transactional content, it uses NoSQL (mongoDB)
- For transactional content, it uses SQLite

## Current Status:
Only Djongo native form works. - 2020-02-23
