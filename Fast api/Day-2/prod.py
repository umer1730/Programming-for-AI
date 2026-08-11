from fastapi import FastAPI,HTTPException

app  = FastAPI(title="Product System")

products = [
    {"id": 1,"name":"Laptop","price":10000},
    {"id": 2,"name":"Mouse","price":200},
    {"id": 3,"name":"Keyboard","price":9000},
    {"id": 4,"name":"Speaker","price":1500},
    {"id": 5,"name":"SSD","price":1000},
]

@app.get("/products")
def get_products():
    return products

@app.get("/products/{id}")
def get_product(id: int):
    for product in products:
        if product["id"] == id:
            return product

    raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

@app.post("/products")
def add_product(name: str, price:float):
    new_product = {
        "id":len(products)+1,
        "name":name,
        "price":price
    }
    products.append(new_product)

    return{
        "message":"Product added successfully",
        "product": new_product
    }     

@app.delete("/products/{id}")
def delete_product(id:int):
    for product in products:
        if product["id"] == id:
            products.remove(product)
            return{
                "message":"Product deleted successfully",
                
            }

    raise HTTPException(
        status_code=404,
        detail="Product not deleted"
    )