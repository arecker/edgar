FROM python:2.7
MAINTAINER Alex Recker <alex@reckerfamily.com>
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["run.py"]
