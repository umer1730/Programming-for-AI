from datetime import datetime

def save_activity(message: str):
    with open("app.log",'a') as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"{time} - {message}")