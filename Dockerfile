FROM python:3.9
WORKDIR /WORK
COPY . /WORK
RUN pip install -r requirements.txt
ENTRYPOINT ["bash", "run.sh"]
