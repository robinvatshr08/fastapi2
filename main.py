from fastapi import FastAPI,Request
from pydantic import BaseModel
from dtos import ProductDTO
from mockData import products


class User(BaseModel):
    name: str
    age: int
    email: str

app=FastAPI()

@app.get("/")
def  read():
    return {"message": "Hello, World!"}

@app.get("/aboutUs")
def contact():
    return "contact us on 9992936348"

@app.get("/products")
def get_products():
    return products

@app.get("/hello/{name}")
def get_name(name:str):
    return {"message" : f"hello mr {name}" }


## path params

@app.get("/product/{product_id}")
def get_product(product_id:int):

    ## if products avalable with the id return product else return reeor message
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct


    return {"error": "product not found for this id"}

@app.get("/greet")
def greet(request:Request):
    query_params=dict(request.query_params)
    return {
        "greet":f"hows are you {query_params.get("name")} age is {query_params.get("age")}"
    }


@app.get("/details")
def getDetails(request:Request):
    query_params=dict(request.query_params)
    return {
        "details":f" name of product is {query_params.get("name")} and price is {query_params.get("price")}"
    }

@app.post("/users")
def createUser(user : User):
    return {
        "message": f" name of user is {user.name}",
        "user_details" : "user"
    }







## GET Method
@app.get("/product/{product_id}")
def get_product(product_id:int):

    ## if products avalable with the id return product else return reeor message
    for oneProduct in products:
        if oneProduct.get("id") == product_id:
            return oneProduct


    return {"error": "product not found for this id"}

## POST method

@app.post("/createproduct")
def createProduct(product_data:ProductDTO):
    product_data=product_data.model_dump()
    print(product_data)
    products.append(product_data)
    return {
        "status":"successfully created new products",
        "data":products
    }


## PUT methode
@app.put("/updateProduct/{product_id}")
def updateProduct(product_data:ProductDTO, product_id:int):
    for index , oneproduct in enumerate(products):
        if oneproduct.get("id") == product_id :
            products[index] = product_data.model_dump()
            return { "status":"product update successfully",
                    "product":product_data}
        print(oneproduct)
      
    return {
        "error":"product not found with this id",
        
    }



@app.post("/adddata")
def create_product(product_data:ProductDTO):
    product_data=product_data.model_dump()
    products.append(product_data)
    print(product_data)

    return {
        "status":"data  created successfully ",
        "data":products
    }

@app.put("/update/{product_id}")
def updata_product(product_data:ProductDTO,product_id:int):
    product_data=product_data.model_dump()
    for index , oneproduct in enumerate(products):
        if oneproduct.get("id") == product_id:
            products[index]=product_data
            return { "status":"product update successfully",
                    "product":product_data}
        print(oneproduct)
    
    return {
        "error":"product not found with this id"
    }
    
