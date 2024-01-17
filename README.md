# Real_Time_Event_Driven_Communication
Demonstration of a real time event driven communication system for 2 applications: main app and admin app. Admin app can post products and main app which is for users can like the product.

# Start Using Project
django-admin startproject admin
cd admin
python3 manage.py runserver
python -m venv .venv
source .venv/bin/activate
conda deactivate
pip install --upgrade pi
pip install -r requirements.txt
docker-compose up
mysql -u adminuser -p -h 127.0.0.1 -P 33066

docker-compose exec backend sh


# main app usage
cd main
python3.12 -m venv .venv
source .venv/bin/activate
conda deactivate
pip install --upgrade pip
pip install -r requirements.txt
docker compose build backend
docker compose down
docker compose up
docker compose up --build -d
docker compose exec db /bin/bash
echo $MYSQL_USER

docker compose exec backend sh => python manager.py db init => python manager.py db migrate => python manager.py db upgrade

docker-compose exec backend sh => export FLASK_APP=main.py => flask db init => flask db migrate -m "Initial migration" => flask db upgrade

docker compose exec db mysql -u root -p
use main;
show tables;
mysql> show tables;
+-----------------+
| Tables_in_main  |
+-----------------+
| alembic_version |
| product         |
| product_user    |
+-----------------+
3 rows in set (0.00 sec)

docker compose down -v
docker compose build

# Frontend:
npm install -g @angular/cli@latest
ng new admin-frontend
cd admin-frontend
ng generate component components/product-list
ng generate component components/product-card
ng add @angular/material
npm install bootstrap
ng generate service services/product  => Create a service to handle HTTP requests to your backend


# RabbitMQ functioning:
![image](https://github.com/user-attachments/assets/47a1ad1c-8209-4c91-b714-8c218dfc9e4a)

# This is the Admin app where admins can make the products
![image](https://github.com/user-attachments/assets/49bda236-7e28-4738-9857-c0bcfab65d8f)

# This is the Main app where users can like the products
![image](https://github.com/user-attachments/assets/f73904e3-9e3a-49d5-8784-047c94f50d08)


This is how 2 apps real-time event driven communication is established.
