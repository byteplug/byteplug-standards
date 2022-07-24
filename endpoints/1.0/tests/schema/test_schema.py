import textwrap
import json
import yaml
from yaml import CLoader as Loader
from jsonschema import RefResolver, Validator
from jsonschema import Draft7Validator
from jsonschema.exceptions import ValidationError
import pytest

VALID_NAMES = [
    "foobar",
    "foo-bar"
]

INVALID_NAMES = [
    "Foobar",
    "foo_bar",
    "-foobar",
    "barfoo-",
    "foo--bar"
]

SIMPLE_DOCUMENT_SPECS = """\
type: flag
"""

COMPLEX_DOCUMENT_SPECS = """\
type: map
fields:
  foo:
    type: flag
  bar:
    type: integer
  quz:
    type: string
"""

INVALID_DOCUMENT_SPECS = """\
type: foo
"""

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
        base_uri = "https://www.byteplug.io/standards/endpoints/1.0/schema.json",
        referrer = schema,
        handlers=handlers
    )

    validator = Draft7Validator(schema, resolver=resolver)
    return validator.validate(document)

def field_boolean_type_test(document, name):

    validate_document(document.replace("{value}", "true"))
    validate_document(document.replace("{value}", "false"))

    with pytest.raises(ValidationError) as e_info:
        validate_document(document.replace("{value}", "42"))
    # assert e_info.value.json_path == f"$.{name}"
    # assert e_info.value.message == "42 is not of type 'boolean'"

    with pytest.raises(ValidationError) as e_info:
        validate_document(document.replace("{value}", '"Hello world!"'))
    # assert e_info.value.json_path == f"$.{name}"
    # assert e_info.value.message == "'Hello world!' is not of type 'boolean'"

def field_string_type_test(document, name):
    validate_document(document.replace("{value}", '"Hello world!"'))

    with pytest.raises(ValidationError) as e_info:
        validate_document(document.replace("{value}", "false"))
    # assert e_info.value.json_path == f"$.{name}"
    # assert e_info.value.message == "False is not of type 'string'"

    with pytest.raises(ValidationError) as e_info:
        validate_document(document.replace("{value}", "true"))
    # assert e_info.value.json_path == f"$.{name}"
    # assert e_info.value.message == "True is not of type 'string'"

    with pytest.raises(ValidationError) as e_info:
        validate_document(document.replace("{value}", "42"))
    # assert e_info.value.json_path == f"$.{name}"
    # assert e_info.value.message == "42 is not of type 'string'"

def test_canonical_specs():
    """ Test a basic canonical specs. """

    # TODO; Make use of records in specs after final design decisions are made.

    document = """\
standard: foo

title: My Title
summary: My Summary
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
  my-endpoint:
    name: My Endpoint
    description: This is the description of 'My Endpoint'.
    request:
      type: string
      length:
        maximum: 42
      pattern: "Hello world!"
    response:
      type: flag
    errors:
      foo:
        name: Foo
        description: This is the description of 'Foo' error.
        value:
          type: flag
      bar:
        name: Bar
        description: This is the description of 'Bar' error.
        value:
          type: integer
      quz:
        name: quz
        description: This is the description of 'Quz' error.
        value:
          type: string

collections:
  my-collection:
    name: My Collection
    description: This is the description of 'My Collection'.
    endpoints:
      my-item-endpoint:
        name: My Item Endpoint
        description: This is the description of 'My Item Endpoint'.
        operate: item
        request:
          type: flag
        response:
          type: flag
      my-collection-endpoint:
        name: My Collection Endpoint
        description: This is the description of 'My Collection Endpoint'.
        operate: collection
        request:
        request:
          type: flag
        response:
          type: flag
"""

    validate_document(document)

def test_metadata():
    """ Test the metadata-related properties. """

    # TODO; Extend the tests after more design decisions are made.

    # test the 'title' and 'summary' properties
    document = """\
title: My Title
summary: My Summary
"""

    validate_document(document)

    # test the 'contact' property
    document = """\
contact:
  name: My Company
  url: https://www.my-company.com/
  email: contact@my-company.com
"""

    validate_document(document)

    # test the 'license' property
    document = """\
license:
  name: "The Open Software License 3.0"
  url: https://opensource.org/licenses/OSL-3.0
"""
    validate_document(document)

    document = """\
license:
  name: "The Open Software License 3.0"
  identifier: OSL-3.0
"""
    validate_document(document)

    # test the 'version' property
    document = """\
version: 0.0.1
"""
    validate_document(document)

def test_endpoints():
    """ Test non-collection endpoints. """

    minimal_document = """\
endpoints:
  foo:
    name: Foo
  bar:
    name: Bar
"""
    validate_document(minimal_document)

    document = """\
endpoints:
  {value}:
    name: Name
"""

    for name in VALID_NAMES:
        validate_document(document.replace("{value}", name))

    for name in INVALID_NAMES:
        with pytest.raises(ValidationError) as e_info:
            validate_document(document.replace("{value}", name))
        assert "does not match '^[a-z]+(-[a-z]+)*$'" in e_info.value.message

    # test the 'name' and 'description' properties
    document = """\
endpoints:
  my-endpoint:
    name: {value}
"""

    field_string_type_test(document, None)

    document = """\
endpoints:
  my-endpoint:
    description: {value}
"""

    field_string_type_test(document, None)

    # test the 'request' and 'response' properties
    document = """\
endpoints:
  my-endpoint:
    request:
"""

    validate_document(document + textwrap.indent(SIMPLE_DOCUMENT_SPECS, ' ' * 6))
    validate_document(document + textwrap.indent(COMPLEX_DOCUMENT_SPECS, ' ' * 6))
    with pytest.raises(ValidationError) as e_info:
        validate_document(document + textwrap.indent(INVALID_DOCUMENT_SPECS, ' ' * 6))
    assert "'foo' is not one of" in e_info.value.message

    document = """\
endpoints:
  my-endpoint:
    response:
"""

    validate_document(document + textwrap.indent(SIMPLE_DOCUMENT_SPECS, ' ' * 6))
    validate_document(document + textwrap.indent(COMPLEX_DOCUMENT_SPECS, ' ' * 6))
    with pytest.raises(ValidationError) as e_info:
        validate_document(document + textwrap.indent(INVALID_DOCUMENT_SPECS, ' ' * 6))
    assert "'foo' is not one of" in e_info.value.message

    # test the 'errors' properties
    document = """\
endpoints:
  my-endpoint:
    errors:
      {value}:
        value:
          type: flag
"""

    for name in VALID_NAMES:
        validate_document(document.replace("{value}", name))

    for name in INVALID_NAMES:
        with pytest.raises(ValidationError) as e_info:
            validate_document(document.replace("{value}", name))
        assert "does not match '^[a-z]+(-[a-z]+)*$'" in e_info.value.message

    document = """\
endpoints:
  my-endpoint:
    errors:
      foo:
        value:
"""

    validate_document(document + textwrap.indent(SIMPLE_DOCUMENT_SPECS, ' ' * 10))
    validate_document(document + textwrap.indent(COMPLEX_DOCUMENT_SPECS, ' ' * 10))
    with pytest.raises(ValidationError) as e_info:
        validate_document(document + textwrap.indent(INVALID_DOCUMENT_SPECS, ' ' * 10))
    assert "'foo' is not one of" in e_info.value.message

    # test the 'authentication" property
    document = """\
endpoints:
  my-endpoint:
    authentication: {value}
"""

    field_boolean_type_test(document, None)

    # test additional properties
    document = """\
endpoints:
  my-endpoint:
    name: My Endpoint
    foo: bar
"""

    with pytest.raises(ValidationError) as e_info:
        validate_document(document)
    assert e_info.value.message == "Additional properties are not allowed ('foo' was unexpected)"

def test_collections():
    """ Test collection endpoints. """

    minimal_document = """\
collections:
  foo:
    endpoints:
      bar:
        name: Bar
      quz:
        name: Quz
"""
    validate_document(minimal_document)

    # test the 'endpoints' property
    document = """\
collections:
  foo:
    name: Foo
"""

    with pytest.raises(ValidationError) as e_info:
        validate_document(document)
    assert e_info.value.message == "'endpoints' is a required property"

    # test collection name restrictions
    document = """\
collections:
  {value}:
    endpoints:
      foo:
        name: Foo
"""

    for name in VALID_NAMES:
        validate_document(document.replace("{value}", name))

    for name in INVALID_NAMES:
        with pytest.raises(ValidationError) as e_info:
            validate_document(document.replace("{value}", name))
        assert "does not match '^[a-z]+(-[a-z]+)*$'" in e_info.value.message

    # test the 'name' and 'description' properties
    document = """\
collections:
  my-collection:
    name: {value}
    endpoints:
      foo:
        name: Foo
"""

    field_string_type_test(document, None)

    document = """\
collections:
  my-collection:
    description: {value}
    endpoints:
      foo:
        name: Foo
"""

    field_string_type_test(document, None)

    # test the 'operate' property (note that the other endpoint related tests
    # are already done in test_endpoints())
    document = """\
collections:
  foo:
    endpoints:
      bar:
        operate: {value}
"""
    validate_document(document.replace("{value}", "item"))
    validate_document(document.replace("{value}", "collection"))

    with pytest.raises(ValidationError) as e_info:
        validate_document(document.replace("{value}", "foo"))
    assert e_info.value.message == "'foo' is not one of ['item', 'collection']"

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
