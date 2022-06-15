import json
import yaml
from yaml import CLoader as Loader
from jsonschema import RefResolver, Validator
from jsonschema import Draft7Validator
import pytest

schema = json.load(open("../../schema.json"))
document_validator_schema = json.load(open("../../../../document-validator/1.0/schema.json"))

Validator.check_schema(schema)
Validator.check_schema(document_validator_schema)

def validate_document(document):
    document = yaml.load(document, Loader=Loader)

    def uri_loader(uri):
        if uri == "https://www.byteplug.io/standards/document-validator/1.0/schema.json":
            return document_validator_schema

    handlers = {
        "https": uri_loader
    }
    resolver = RefResolver(
        base_uri = "https://www.byteplug.io/standards/easy-endpoints/1.0/schema.json",
        referrer = schema,
        handlers=handlers
    )

    validator = Draft7Validator(schema, resolver=resolver)
    return validator.validate(document)

def test_schema():
    document = """\
standard: foo

title: My Title
summary: My Summary
description: My Description.
contact:
  name: My Company
  url: https://www.my-company.com/
  email: contact@my-company.com
license:
  name: "The Open Software License 3.0"
  url: https://opensource.org/licenses/OSL-3.0
version: 0.0.1

records:
  user:
    name: User
    description: To be written.
    value:
      type: map
      fields:
        foo:
          type: flag
        bar:
          type: integer
        quz:
          type: string

endpoints:
  foo:
    request:
      type: string
      length:
        maximum: 42
      pattern: "Hello world!"
    response:
      type: flag
"""

    validate_document(document)
