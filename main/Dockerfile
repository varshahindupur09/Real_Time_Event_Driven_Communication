FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y default-mysql-client
RUN pip install -r requirements.txt
COPY . /app

# CMD python main.py
CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]