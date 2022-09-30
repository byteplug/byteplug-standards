import json
import yaml
from yaml import CLoader as Loader
from jsonschema import validate, Validator
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

# - check map.fields can be empty
# - check tuple.values can be empty


VALID_NAMES = [
    "foobar",
    "FOOBAR",
    "123456",
    "foo-bar",
    "foo_bar"
]

INVALID_NAMES = [
    "foo*bar",
    "foo&bar",
    "bar'foo",
    "foo)bar"
]


schema = json.load(open("../../schema.json"))
Validator.check_schema(schema)

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

def test_number_type():
    # test minimal document
    validate_document("type: number")

    # test 'decimal' property
    option_field_test("type: number\ndecimal: {value}")

    # test 'minimum' and 'maximum' properties (with decimal variants)
    validate_document("type: number\nminimum: 42")
    validate_document("type: number\nminimum:\n  value: 42")
    validate_document("type: number\nminimum:\n  exclusive: false\n  value: 42")
    validate_document("type: number\nminimum:\n  exclusive: true\n  value: 42")

    validate_document("type: number\nminimum: 42.0")
    validate_document("type: number\nminimum:\n  value: 42.0")
    validate_document("type: number\nminimum:\n  exclusive: false\n  value: 42.0")
    validate_document("type: number\nminimum:\n  exclusive: true\n  value: 42.0")

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: number\nminimum:\n  exclusive: false")
    # assert e_info.value.message == ""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: number\nminimum:\n  value: 42\n  foo: bar")
    # assert e_info.value.message == ""

    validate_document("type: number\nmaximum: 42")
    validate_document("type: number\nmaximum:\n  value: 42")
    validate_document("type: number\nmaximum:\n  exclusive: false\n  value: 42")
    validate_document("type: number\nmaximum:\n  exclusive: true\n  value: 42")

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: number\nmaximum:\n  exclusive: true")
    # assert e_info.value.message == ""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: number\nmaximum:\n  value: 42\n  foo: bar")
    # assert e_info.value.message == ""

    validate_document("type: number\nminimum: 42\nmaximum: 42")

    document = """\
type: number
minimum:
  exclusive: false
  value: 10
maximum:
  exclusive: true
  value: 100
"""
    validate_document(document)

    # test 'option' property
    option_field_test("type: number\noption: {value}")

    # test additional properties
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: number\nfoo: bar")
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

def test_array_type():
    # test minimal document
    minimal_document = """\
type: array
value:
  type: string
"""
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: array")
    # assert e_info.value.message == "'value' is a required property"

    validate_document("type: array\nvalue:\n  type: flag")
    validate_document("type: array\nvalue:\n  type: number")
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

def test_object_type():
    # test minimal document
    minimal_document = """\
type: object
value:
  type: string
"""
    with pytest.raises(ValidationError) as e_info:
        validate_document("type: object")
    # assert e_info.value.message == "'value' is a required property"

    validate_document("type: object\nvalue:\n  type: flag")
    validate_document("type: object\nvalue:\n  type: number")
    validate_document(minimal_document)

    # test 'key' property
    validate_document(minimal_document + "key: integer")
    validate_document(minimal_document + "key: string")
    with pytest.raises(ValidationError) as e_info:
        validate_document(minimal_document + "key: yolo")
    # assert e_info.value.message == ""

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
items:
  - type: flag
  - type: number
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
    type: number
  quz:
    type: string
"""

    with pytest.raises(ValidationError) as e_info:
        validate_document("type: map")
    # assert e_info.value.message == "'fields' is a required property"

    validate_document(minimal_document)

    # TODO; test fields with invalid names
    document = """\
type: map
fields:
  {value}:
    type: number
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
values: ["{value}"]
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
