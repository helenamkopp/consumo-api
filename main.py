import requests
#lib que converte o conteúdo da resposta p/ dicionário
import json


def create_a_new_product(prod):
    url = "http://172.24.0.3:8000/product/"
    obj = {"name": "teste de prod", "description": "tests de descricao", "price": 186.55, "category": 3}
    post = requests.post(url, data=obj)
    status_code = post.status_code
    print(status_code)


def get_all_products():
    request = requests.get("http://172.24.0.3:8000/product/")
    products = json.loads(request.content)
    print(products)
    # print(products[0]['description'])
    # print(request.content)


def get_one_product_by_id(id):
    request = requests.get(f"http://172.24.0.3:8000/product/{id}")
    product = json.loads(request.content)
    print(product)


def update_one_product_by_id(id):
    url = f"http://172.24.0.3:8000/product/{id}/"
    obj = {"name": "teste de prod atualizado de novo", "description": "tests de descricao", "price": 250.55, "category": 3}
    put = requests.put(url, data=obj)
    status_code = put.status_code
    print(status_code)
    

def delete_one_product_by_id(id):
    request = requests.delete(f"http://172.24.0.3:8000/product/{id}")
    status_code = request.status_code
    if status_code == 204:
        print("Registro excluído com sucesso")
    else:
        print("Impossível excluir esse dado. Registro não encontrado.")

if __name__ == '__main__':
    # create_a_new_product(product.Product('teste de prod', 'tests de descricao', 186.55, 3))
    # get_all_products()
    # get_one_product_by_id("3")
    # update_one_product_by_id("12")
    # delete_one_product_by_id("5")

