def save_log(name:str,email:str):
    with open("users.log","a") as file:
        file.write(
            f"User registered: {name} - {email}\n"
        )

def send_welcome_email(email:str):
    print(f"Welcome email sent to {email}")

def create_notification(name:str):
    print(f"Notification created for {name}")