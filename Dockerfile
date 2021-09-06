FROM python:3.7.5
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000
#CMD ["ls"]
CMD ["python", "microblog_api/manage.py", "runserver", "0.0.0.0:8000"]

