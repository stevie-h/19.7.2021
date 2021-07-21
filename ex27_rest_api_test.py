
import pytest
import requests
import json


class RestObject:
    def __init__(self, d):
        self.__dict__ = d

    def __str__(self):
        result = ""
        for k, v in self.__dict__.items():
            result += k
            result += " : "
            result += str(v)
            result += '\n'
        return result


def test_rest_api_get_product():
    resp = requests.get("http://127.0.0.1:5000/product/1")
    d = json.loads(resp.content)
    t = RestObject(d)
    assert t.id == 1
    assert t.name == 'prod1'
    assert t.price == 1.11
    assert t.quantity == 1


def test_rest_api_post_product():
    resp = requests.post("http://127.0.0.1:5000/product/",
                         data='{"name": "prod4", "price": 4.44, "quantity": 4}',
                         headers={"Content-type": "application/json"})
    print(f'Status code = {resp.status_code}')
    assert resp.status_code == 200
    resp_ = requests.get("http://127.0.0.1:5000/product/4")
    d = json.loads(resp_.content)
    t = RestObject(d)
    assert t.id == 4
    assert t.name == 'prod4'
    assert t.price == 4.44
    assert t.quantity == 4


def test_rest_api_update_product():
    resp = requests.put("http://127.0.0.1:5000/product/4",
                        data='{"name": "prod4type2", "price": 44.444, "quantity": 444}',
                        headers={"Content-type": "application/json"})
    print(f'Status code = {resp.status_code}')
    assert resp.status_code == 200
    resp_ = requests.get("http://127.0.0.1:5000/product/4")
    d = json.loads(resp_.content)
    t = RestObject(d)
    assert t.id == 4
    assert t.name == 'prod4type2'
    assert t.price == 44.444
    assert t.quantity == 444


def test_rest_api_delete_product():
    resp = requests.delete("http://127.0.0.1:5000/product/4")
    print(f'Status code = {resp.status_code}')
    assert resp.status_code == 200
    resp_ = requests.get("http://127.0.0.1:5000/product/4")
    assert resp_.status_code == 500


