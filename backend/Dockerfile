FROM python:3.11-slim

WORKDIR /app
RUN apt update && apt install -y make

COPY Pipfile Pipfile.lock /app/
RUN pip install pipenv && pipenv install --system --deploy

COPY ./backend/ /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
