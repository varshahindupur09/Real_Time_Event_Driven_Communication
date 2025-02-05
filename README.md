# Real_Time_Event_Driven_Communication
Demonstration of a real time event driven communication system for 2 applications: main app and admin app. Admin app can post products and main app which is for users can like the product.

# Start Using Project
django-admin startproject admin <br/>
cd admin <br/>
python3 manage.py runserver <br/>
python -m venv .venv <br/>
source .venv/bin/activate <br/>
conda deactivate <br/>
pip install --upgrade pip <br/>
pip install -r requirements.txt <br/>
docker-compose up <br/>
mysql -u adminuser -p -h 127.0.0.1 -P 33066 <br/>

docker-compose exec backend sh


# main app usage
cd main <br/>
python3.12 -m venv .venv <br/>
source .venv/bin/activate <br/>
conda deactivate <br/>
pip install --upgrade pip <br/>
pip install -r requirements.txt <br/>
docker compose build backend <br/>
docker compose down <br/>
docker compose up <br/>
docker compose up --build -d <br/>
docker compose exec db /bin/bash <br/>
echo $MYSQL_USER <br/>

docker compose exec backend sh => python manager.py db init => python manager.py db migrate => python manager.py db upgrade <br/>

docker-compose exec backend sh => export FLASK_APP=main.py => flask db init => flask db migrate -m "Initial migration" => flask db upgrade <br/>

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
