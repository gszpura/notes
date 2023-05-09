# App Details

## notes
This is a React app created with:

> npx create-react-app notes

`npx` is a part of `npm` toolset that comes with node.
To install node run:

> sudo apt-get install -y nodejs

To run locally:
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
