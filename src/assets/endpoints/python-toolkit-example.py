from byteplug.document import Node
from byteplug.endpoints import Endpoints
from byteplug.endpoints import endpoint, request, response

endpoints = Endpoints()

@request(Node('string', option=True))
@response(Node('string'))
@endpoint("hello")
def hello_someone(name):
    if name:
        return f"Hello {name}!"
    else:
        return "Hello world!"

endpoints.add_endpoint(hello_someone)
endpoints.run()
