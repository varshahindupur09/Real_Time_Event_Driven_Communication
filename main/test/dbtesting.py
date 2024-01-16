from sqlalchemy import create_engine

# Use your actual SQLALCHEMY_DATABASE_URI here
DATABASE_URI = 'mysql+pymysql://mainuser:root@db/main'

engine = create_engine(DATABASE_URI)
try:
    connection = engine.connect()
    print("Connection to the database is successful!")
    connection.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")