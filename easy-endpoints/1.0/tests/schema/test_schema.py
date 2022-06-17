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

# Test-related code that used to be in the Document Validator standard.

# def test_records_type():
#     # test minimal document
#     with pytest.raises(ValidationError) as e_info:
#         validate_document("type: record")
#     # assert e_info.value.message == "'record' is a required property"

#     validate_document("type: record\nrecord: foo")

#     # test validity of the record value
#     document = """\
# type: record
# record: {value}
# """

#     for name in VALID_NAMES:
#         validate_document(document.replace("{value}", name))

#     for name in INVALID_NAMES:
#         with pytest.raises(ValidationError) as e_info:
#             validate_document(document.replace("{value}", name))
#         # assert e_info.value.message == ""

#     # test additional fields
#     with pytest.raises(ValidationError) as e_info:
#         validate_document("type: record\nrecord: foo\nfoo: bar")
#     assert e_info.value.message == "Unevaluated properties are not allowed ('foo' was unexpected)"

# def test_records_without_root():
#     document = """\
# records:
#   foo:
#     value:
#       type: string
# """

#     with pytest.raises(ValidationError) as e_info:
#         validate_document(document)

# def test_records():
#     document = """\
# records:
#   foo:
#     value:
#       type: string
#       length:
#         maximum: 42
#       pattern: "Hello world!"

# type: record
# record: foo
# """

#     validate_document(document)

#     # test 3 fields of records
#     document = """\
# records:
#   foo:
#     name: Foo
#     description: "This is the description of the 'Foo' record."
#     value:
#       type: string
#       length:
#         maximum: 42
#       pattern: "Hello world!"

# type: record
# record: foo
# """
#     validate_document(document)

#     document = """\
# records:
#   foo:
#     name: Foo
#     description: "This is the description of the 'Foo' record."

# type: record
# record: foo
# """

#     with pytest.raises(ValidationError) as e_info:
#         validate_document(document)
#     # assert e_info.value.message == ""

#     # test validity of the records name
#     document = """\
# records:
#   {value}:
#     value:
#       type: string

# type: record
# record: foo
# """

#     for name in VALID_NAMES:
#         validate_document(document.replace("{value}", name))

#     for name in INVALID_NAMES:
#         with pytest.raises(ValidationError) as e_info:
#             validate_document(document.replace("{value}", name))
#         # assert e_info.value.message == ""

#     # test validity of the records value
#     document = """\
# records:
#   fll:
#     value:
#       bar: quz

# type: record
# record: foo
# """

#     with pytest.raises(ValidationError) as e_info:
#         validate_document(document)

# def test_some_records_example():
#     document = """\
# records:
#   a-flag:
#     name: A flag
#     description: This is a basic flag.
#     value:
#       type: flag
#   a-integer:
#     name: An integer
#     description: This is a basic integer.
#     value:
#       type: integer
#   a-string:
#     name: A string
#     description: This is a basic string.
#     value:
#       type: string

# type: map
# fields:
#   foo:
#     type: record
#     record: a-flag
#   bar:
#     type: record
#     record: a-integer
#   quz:
#     type: record
#     record: a-string
# option: true
# """

#     validate_document(document)
