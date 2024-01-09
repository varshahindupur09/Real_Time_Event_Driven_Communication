# Real_Time_Event_Driven_Communication
Demonstration of a real time event driven communication system for 2 applications: main app and admin app. Admin app can post products and main app which is for users can like the product.

# Start Using Project
django-admin startproject admin
cd admin
python3 manage.py runserver
python -m venv .venv
source .venv/bin/activate
conda deactivate
pip install -r requirements.txt
docker-compose up
mysql -u adminuser -p -h 127.0.0.1 -P 33066


# RabbitMQ functioning:
![image](https://github.com/user-attachments/assets/47a1ad1c-8209-4c91-b714-8c218dfc9e4a)

# This is the Admin app where admins can make the products
![image](https://github.com/user-attachments/assets/49bda236-7e28-4738-9857-c0bcfab65d8f)

# This is the Main app where users can like the products
![image](https://github.com/user-attachments/assets/f73904e3-9e3a-49d5-8784-047c94f50d08)


This is how 2 apps real-time event driven communication is established.
