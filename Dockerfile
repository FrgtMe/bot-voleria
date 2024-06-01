FROM python:3.9
WORKDIR /WORK
COPY . /WORK
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "-m", "http.server", "&", "python", "smsc.py"]
