FROM python:3.11

# Set the working directory
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy the 'pyproject.toml' and 'poetry.lock' files (if exists) to the working directory
COPY pyproject.toml ./
COPY poetry.lock ./

# Install the project dependencies using Poetry
RUN poetry config virtualenvs.create false

RUN poetry install --no-interaction --no-ansi --no-root

COPY . .

RUN poetry build
RUN pip install --no-cache-dir dist/notes_backend-*.tar.gz


CMD ["uvicorn", "notes_backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
