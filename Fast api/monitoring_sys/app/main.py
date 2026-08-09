from fastapi import FastAPI,BackgroundTasks,HTTPException
from fastapi.middleware.cors import CORSMiddleware

import json
from pydantic import BaseModel
from app.middleware import monitoring_middleware
from app.background import save_activity

app = FastAPI(title="API Monitoring System")

#CORS for react frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

#now every request will go from middleware
app.middleware("http")(monitoring_middleware)

#pydantic
class User(BaseModel):
    name: str
    email: str

#helper functions
# for read json file
def load_users():
    with open("app/data.json","r") as file:
        data = json.load(file)

    return data["users"]

#for save json file
def save_users(users):
    with open("app/data.json","w") as file:
        json.dump({"users": users},file,indent=4)

#get users
@app.get("/users")
def get_users():
    users = load_users()
    return users

#post
@app.post("/users")
def create_user(user: User,background_tasks: BackgroundTasks):

    users = load_users()
    new_id = len(users) + 1

    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)

    save_users(users)

    background_tasks.add_task(save_activity,f"User {new_id} created")
    return new_user


#get user
@app.get("/users/{user_id}")
def get_user(user_id: int):
    users= load_users()
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )

#delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int,background_tasks: BackgroundTasks):
    users = load_users()

    for user in users:
        if user["id"] == user_id:
            users.remove(user)

            save_users(users)
            background_tasks.add_task(
                save_activity,
                f"User {user_id} deleted")

            return {
                "message": "User deleted successfully"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )