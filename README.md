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

Setup was done with:
> poetry new notes_backend

> poetry add fastapi uvicorn


Skeleton code was added for:

- db - sqlalchemy.ext.asyncio



## Run
> cd notes; npm start

> poetry shell; cd notes_backend; python main.py

Open localhost:3000.
