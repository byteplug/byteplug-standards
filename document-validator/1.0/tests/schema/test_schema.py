import json
import yaml
from yaml import CLoader as Loader
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import pytest

# NOTES: Lot of assertions were commented out because when we're entering the
#        dynamic part of JSON Schema, the jsonschema is no longer able to
#        produce accurate error messages.

# TODOs:
# - For the decimal type, add more decimal-related properties after study.
# - For the minimum/maximum rules, can we restrict the maximum value to be
#   greater than the minimum value (if specified).
# - For the enum type, can we restrict the default value to be one in the
#   values list.

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

schema = json.load(open("../../schema.json"))

def validate_document(document):
    document = yaml.load(document, Loader=Loader)
    return validate(instance=document, schema=schema)

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

def field_number_type_test(document, name):
    validate_document(document.replace("{value}", "42"))

    with pytest.raises(ValidationError) as e_info:
        validate_document(document.replace("{value}", "false"))
    # assert e_info.value.json_path == f"$.{name}"
    # assert e_info.value.message == "False is not of type 'number'"

    with pytest.raises(ValidationError) as e_info:
        validate_document(document.replace("{value}", "true"))
    # assert e_info.value.json_path == f"$.{name}"
    # assert e_info.value.message == "True is not of type 'number'"

    with pytest.raises(ValidationError) as e_info:
        validate_document(document.replace("{value}", '"Hello world!"'))
    # assert e_info.value.json_path == f"$.{name}"
    # assert e_info.value.message == "'Hello world!' is not of type 'number'"

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

def option_field_test(document):
    field_boolean_type_test(document, "option")

def test_flag_type():
    # test minimal document
    validate_document("type: flag")

    # test the 'option' property
    option_field_test("type: flag\noption: {value}")

    # test additional properties
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: flag\nfoo: bar")
    assert e_info.value.message == "Unevaluated properties are not allowed ('foo' was unexpected)"

def test_integer_type():
    # test minimal document
    validate_document("type: integer")

    # test 'minimum' and 'maximum' properties
    validate_document("type: integer\nminimum: 42")
    validate_document("type: integer\nminimum:\n  value: 42")
    validate_document("type: integer\nminimum:\n  exclusive: false\n  value: 42")
    validate_document("type: integer\nminimum:\n  exclusive: true\n  value: 42")

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: integer\nminimum:\n  exclusive: false")
    # assert e_info.value.message == ""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: integer\nminimum:\n  value: 42\n  foo: bar")
    # assert e_info.value.message == ""

    validate_document("type: integer\nmaximum: 42")
    validate_document("type: integer\nmaximum:\n  value: 42")
    validate_document("type: integer\nmaximum:\n  exclusive: false\n  value: 42")
    validate_document("type: integer\nmaximum:\n  exclusive: true\n  value: 42")

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: integer\nmaximum:\n  exclusive: true")
    # assert e_info.value.message == ""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: integer\nmaximum:\n  value: 42\n  foo: bar")
    # assert e_info.value.message == ""

    validate_document("type: integer\nminimum: 42\nmaximum: 42")

    document = """\
type: integer
minimum:
  exclusive: false
  value: 10
maximum:
  exclusive: true
  value: 100
"""
    validate_document(document)

    # test 'option' property
    option_field_test("type: integer\noption: {value}")

    # test additional properties
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: integer\nfoo: bar")
    assert e_info.value.message == "Unevaluated properties are not allowed ('foo' was unexpected)"

def test_decimal_type():
    # test minimal document
    validate_document("type: decimal")

    # test 'minimum' and 'maximum' properties
    validate_document("type: decimal\nminimum: 42.0")
    validate_document("type: decimal\nminimum:\n  value: 42.0")
    validate_document("type: decimal\nminimum:\n  exclusive: false\n  value: 42.0")
    validate_document("type: decimal\nminimum:\n  exclusive: true\n  value: 42.0")

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: decimal\nminimum:\n  exclusive: false")
    # assert e_info.value.message == ""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: decimal\nminimum:\n  value: 42.0\n  foo: bar")
    # assert e_info.value.message == ""

    validate_document("type: decimal\nmaximum: 42.0")
    validate_document("type: decimal\nmaximum:\n  value: 42.0")
    validate_document("type: decimal\nmaximum:\n  exclusive: false\n  value: 42.0")
    validate_document("type: decimal\nmaximum:\n  exclusive: true\n  value: 42.0")

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: decimal\nmaximum:\n  exclusive: true")
    # assert e_info.value.message == ""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: decimal\nmaximum:\n  value: 42.0\n  foo: bar")
    # assert e_info.value.message == ""

    validate_document("type: decimal\nminimum: 42.0\nmaximum: 42.0")

    document = """\
type: decimal
minimum:
  exclusive: false
  value: 10.0
maximum:
  exclusive: true
  value: 100.0
"""
    validate_document(document)

    # test 'option' property
    option_field_test("type: decimal\noption: {value}")

    # test additional properties
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: decimal\nfoo: bar")
    assert e_info.value.message == "Unevaluated properties are not allowed ('foo' was unexpected)"

def test_string_type():
    # test minimal document
    validate_document("type: string")

    # test the 'length' property
    validate_document("type: string\nlength: 42")

    validate_document("type: string\nlength:\n  minimum: 42")
    validate_document("type: string\nlength:\n  maximum: 42")
    validate_document("type: string\nlength:\n  minimum: 0\n  maximum: 42")

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: string\nlength: -1")
    # assert e_info.value.message == ""
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: string\nlength:\n  minimum: -1")
    # assert e_info.value.message == ""
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: string\nlength:\n  maximum: -1")
    # assert e_info.value.message == ""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: string\nlength:\n  foo: bar")
    # assert e_info.value.message == ""

    # test the 'pattern' property
    validate_document("type: string\npattern: \"^[a-z]+(-[a-z]+)*$\"")

    # test 'option' property
    option_field_test("type: string\noption: {value}")

    # test additional properties
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: string\nfoo: bar")
    assert e_info.value.message == "Unevaluated properties are not allowed ('foo' was unexpected)"

def test_enum_type():
    # test minimal document
    minimal_document = """\
type: enum
values: [foo, bar, quz]
"""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: enum")
    # assert e_info.value.message == "'values' is a required property"

    validate_document(minimal_document)

    # test validity of names
    document = """\
type: enum
values: [{value}]
"""

    for name in VALID_NAMES:
        validate_document(document.replace("{value}", name))

    for name in INVALID_NAMES:
        with pytest.raises(ValidationError) as e_info:
            validate_document(document.replace("{value}", name))
        # assert e_info.value.message == ""

    # test 'option' property
    option_field_test(minimal_document + "option: {value}")

    # test additional properties
    with pytest.raises(ValidationError) as e_info:
        validate_document(minimal_document + "foo: bar")
    assert e_info.value.message == "Unevaluated properties are not allowed ('foo' was unexpected)"

def test_list_type():
    # test minimal document
    minimal_document = """\
type: list
value:
  type: string
"""
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: list")
    # assert e_info.value.message == "'value' is a required property"

    validate_document("type: list\nvalue:\n  type: flag")
    validate_document("type: list\nvalue:\n  type: integer")
    validate_document(minimal_document)

    # test 'length' property
    validate_document(minimal_document + "length: 42")
    validate_document(minimal_document + "length:\n  minimum: 42")
    validate_document(minimal_document + "length:\n  maximum: 42")
    validate_document(minimal_document + "length:\n  minimum: 0\n  maximum: 42")

    with pytest.raises(ValidationError) as e_info:
        validate_document(minimal_document + "length: -1")
    # assert e_info.value.message == ""
    with pytest.raises(ValidationError) as e_info:
        validate_document(minimal_document + "length:\n  minimum: -1")
    # assert e_info.value.message == ""
    with pytest.raises(ValidationError) as e_info:
        validate_document(minimal_document + "length:\n  maximum: -1")
    # assert e_info.value.message == ""

    with pytest.raises(ValidationError) as e_info:
        validate_document(minimal_document + "length:\n  foo: bar")
    # assert e_info.value.message == ""

    # test 'option' property
    option_field_test(minimal_document + "option: {value}")

    # test additional properties
    with pytest.raises(ValidationError) as e_info:
        validate_document(minimal_document + "foo: bar")
    assert e_info.value.message == "Unevaluated properties are not allowed ('foo' was unexpected)"

def test_tuple_type():
    # test minimal document
    minimal_document = """\
type: tuple
values:
  - type: flag
  - type: integer
  - type: string
"""
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: tuple")
    # assert e_info.value.message == "'values' is a required property"

    validate_document(minimal_document)

    # TODO; test checking empty array

    # test 'option' property
    option_field_test(minimal_document + "option: {value}")

    # test additional properties
    with pytest.raises(ValidationError) as e_info:
        validate_document(minimal_document + "foo: bar")
    assert e_info.value.message == "Unevaluated properties are not allowed ('foo' was unexpected)"

def test_map_type():
    # test minimal document
    minimal_document = """\
type: map
fields:
  foo:
    type: flag
  bar:
    type: integer
  quz:
    type: string
"""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: map")
    # assert e_info.value.message == "'fields' is a required property"

    validate_document(minimal_document)

    # test fields with invalid names
    document = """\
type: map
fields:
  {value}:
    type: integer
"""

    for name in VALID_NAMES:
        validate_document(document.replace("{value}", name))

    for name in INVALID_NAMES:
        with pytest.raises(ValidationError) as e_info:
            validate_document(document.replace("{value}", name))
        # assert e_info.value.message == ""

    # test fields with invalid values
    document = """\
type: map
fields:
  foo:
    bar: quz
"""

    with pytest.raises(ValidationError) as e_info:
        validate_document(document)
    # assert e_info.value.message == ""

    # test 'option' property
    option_field_test(minimal_document + "option: {value}")

    # test additional properties
    with pytest.raises(ValidationError) as e_info:
        validate_document(minimal_document + "foo: bar")
    assert e_info.value.message == "Unevaluated properties are not allowed ('foo' was unexpected)"
