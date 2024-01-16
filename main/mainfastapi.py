from typing import List
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import requests

# Database URL
DATABASE_URL = "mysql+pymysql://mainuser:root@db:3306/main"

# SQLAlchemy setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI setup
app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class ProductBase(BaseModel):
    id: int
    title: str
    image: str

class ProductCreate(ProductBase):
    pass

class ProductUserBase(BaseModel):
    user_id: int
    product_id: int

# Database models
class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True, autoincrement=False)
    title = Column(String(200))
    image = Column(String(200))

class ProductUser(Base):
    __tablename__ = "product_user"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    product_id = Column(Integer)

    __table_args__ = (UniqueConstraint('user_id', 'product_id', name='user_product_unique'),)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/api/products", response_model=List[ProductBase])
def read_products(db: Session = Depends(get_db)):
    return db.query(Product).all()

@app.post("/api/products/{id}/like", response_model=dict)
def like_product(id: int, db: Session = Depends(get_db)):
    response = requests.get("http://docker.for.mac.localhost:8000/api/user")
    json_data = response.json()

    product_user = ProductUser(user_id=json_data['id'], product_id=id)
    db.add(product_user)
    try:
        db.commit()
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="You already liked this product")

    return {"message": "success"}

# Run the server using Uvicorn
# This would replace `if __name__ == '__main__':` block in FastAPI
