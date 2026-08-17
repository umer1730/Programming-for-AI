import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker


load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit = False,Day 12 — Complete Blog API with PostgreSQL

Aaj hum ek complete Blog API banayenge using:

FastAPI
Pydantic
SQLAlchemy
PostgreSQL
Alembic
One-to-Many Relationship
Foreign Key
CRUD operations
Dependency Injection

Tumhare Day 9–11 ke concepts ab ek real project mein combine honge.

🎯 Project kya banayenge?

Hum ek Blog API banayenge:

User
 │
 ├── Post 1
 ├── Post 2
 └── Post 3

Ek user multiple posts create kar sakta hai.

Database:

users
----------------
id
name
email
age


posts
----------------
id
title
content
published
owner_id

owner_id foreign key hoga:

posts.owner_id
       ↓
users.id
1. Project Structure

Tumhara project:

post_data/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── .env
├── alembic.ini
│
└── alembic/
    ├── env.py
    └── versions/
2. Database

Tumhare paas already PostgreSQL database hai:

fastapi_db

Ismein hum do tables banayenge:

users
posts
    autoflush = False,
    bind = engine
)

Base = declarative_base()

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()