from fastapi import FastAPI

app  = FastAPI()

all_customers = [
    {"id":101, "name":"Ali","city":"Lahore","risk":"high"},
    {"id":102, "name":"Usama","city":"Islamabad","risk":"low"},
    {"id":103, "name":"Arham","city":"Lahore","risk":"high"},
    {"id":104, "name":"Zain","city":"Multan","risk":"medium"},
    {"id":105, "name":"Zahid","city":"Quetta","risk":"medium"},
]

@app.get("/customers")
def get_customers(city:str, risk:str):
    filtered = [
        c for c in all_customers
        if c["city"] == city and c["risk"] == risk
    ]

    return{
        "City":city,
        "Risk":risk,
        "Count":len(filtered),
        "Results":filtered
    }