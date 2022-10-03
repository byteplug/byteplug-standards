from flask import Flask
from byteplug.http_api import HttpAPI
from byteplug.http_api.fields import Text

@endpoint("/hello")
@input([
    Integer("numerator"),
    Integer("denominator", min=0)
])
@output([
    Integer("result")
])
def divide_number(numerator, denominator):
    return [numerator / denominator]

server = Flask("My HTTP API")

http_api = HttpAPI()
http_api.add_endpoint(divide_number)

http_api.implemented_by(server, options)
