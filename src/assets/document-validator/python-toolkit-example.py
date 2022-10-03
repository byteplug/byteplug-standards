import json
from byteplug.document import validate_document, ValidationError

specs = {
    'type': 'object',
    'key': 'string',
    'value': {
        'type': 'number'
    },
    'length': 2
}

json = open('document.json').read()
document = json.loads(json)

try:
    validate_document(document, specs)
except ValidationError:
    print("The document is not valid")
