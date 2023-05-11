# App Details

## notes
This is a React app created with:

> npx create-react-app notes

`npx` is a part of `npm` toolset that comes with node. </br>
App runs on LTS node (18.16.0).</br>
To install correct node version run:

> sudo apt install -y nodejs
>
> sudo apt install npm
>
> sudo npm install -g nvm
>
> nvm install --lts

This should update npm to compatible version as well.</br>
To run `notes` app locally:
> npm install
> 
> npm start

For more details see notes/README.md

## notes_backend
This is a Fast-API (python) app.

Initial setup was done with:
> poetry new notes_backend
>
> poetry add fastapi uvicorn sqlalchemy asyncpg python-dotenv

NOTE: using `python-dotenv`, not `dotenv`, `dotenv` is not compatible with `pydantic`

In order to build project quickly run:
> poetry install

## Run
> cd notes; npm start
>
> poetry shell; cd notes_backend; python main.py

Open localhost:3000.



## Manual setup of DB
Run `psql` tool to enter db CLI:
> psql -h <postgres_container_ip:172.22.0.2> -p <port:5432> -U <username:app_user> -W -d <db_name:notes> 

Create tables:
> psql -h 172.22.0.2 -p 5432 -U app_user -W -d notes -f ./modules/note/db/tables.sql
