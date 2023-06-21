# CRUD_App_Full_Stack
CRUD Full Stack Application

## Requirement
-- Python

-- FastApi

-- React

-- Typescript

-- Tailwindcss

-- Pytest

-- postgres

## Environment Variables
DATABASE_URL=

## Development
Clone a copy of the repository.

Then execute the following lines in two separate terminals

```commandline
$ cd CRUD_App_Full_Stack
$ python3 -m venv env 
$ source env/bin/activate && pip install -r ./requirements.txt
$ uvicorn app:app --reload

```
This can be run in another terminal

```
$ cd ./frontent 
$ npm install
$ npm run develop
```
Once  web server is running API docs can be found on http://localhost:8000/docs

Frontend application can be found on http://localhost:5173

## Author
- **Daniel K. Okyere**
