from datetime import datetime

def write_log(message):
    with open("app.log","a") as file:
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{time} - {message}\n")

def send_email(email):
    print(f"Sending email to {email}")

    # email sending ko stimulate kr rahe ha
    print(f"Email sent successfully to {email}")