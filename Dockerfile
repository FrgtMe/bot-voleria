FROM python:3.9
WORKDIR /WORK
COPY . /WORK
RUN pip install -r requirements.txt
RUN python -m http.server &
ENTRYPOINT ["python", "smsc.py"]
