FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY requirementsfastapi.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install cryptography
COPY . /app

# CMD python main.py
# CMD ["gunicorn", "-b", "0.0.0.0:5000", "main:app"]
# CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "-b", "0.0.0.0:5000", "mainfastapi:app"]