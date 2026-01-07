from fastapi import FastAPI,Request
from mockData import products
app=FastAPI()

@app.get('/home')
def home():
   return ("welcome to home page")

@app.get('/products')
def getproduct():
   return products


# path params......
@app.get('/product/{id}')
def get_one_product(id:int):
   for item in products:
      if(item.get("id")==id):
         return item
    
   return {
      'error':"item not found for this id"
   }
  

# query params ........
# @app.get('/greet')
# def greet(name:str,age:int):
#    return {
#       'greet':f'hello Mr. {name}, How are you your age is {age}'
#    }
 
# query params ........
@app.get('/greet')
def greet(request:Request):
   query_par=dict(request.query_params)
   return {
      'greet':f'hello Mr. {query_par.get('name')}, How are you your age is {query_par.get('age')}'
   }