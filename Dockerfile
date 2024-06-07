FROM python:3.8.10

WORKDIR /cicd-jenkins

COPY . /cicd-jenkins

RUN pip install -r requirements.txt --no-cache-dir
EXPOSE 8005
CMD python app.py
