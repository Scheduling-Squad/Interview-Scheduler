# start by pulling the python image
FROM python:3.10-slim-bullseye
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
EXPOSE 5000
ENV PYTHONPATH /code
CMD ["python","/code/application/run.py","--host", "0.0.0.0"]