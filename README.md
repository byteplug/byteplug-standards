# Byteplug Standards

This repository contains the documents and test suites of the Byteplug in-house
standards.

Test suites are written in Python and should be executed after creating a
virtual environment (with `python3 -m virtualenv .python && source .python/bin/activate`)
and installing `pytest`, `pyyaml` and `jsonschema` packages.

## Document Validator

This standard specifies how to write a YAML written specs that defines what is
a valid JSON document. It virtually extends the native JSON type system to
introduce augmented types, and thus, convey more information.

It can be seen as an alterative to JSON Schema with a nicer syntax (in YAML
instead of JSON) and without its dynamic fields.

**Documents**

- `document.md` - The only text defining the standard.
- `example.yml` - The official example showcasing a YAML specs.
- `schema.json` - The JSON Schema to validate YAML specs (used for external tools)

**Test Suites**

- `schema` - Check if the JSON Schema properly validates YAML specs

## Easy Endpoints

This standard defines a set of rules to implement HTTP API. It's built on top
of the Document Validator standard to define input and output of its endpoints.

It can be seen as an alterative to OpenAPI Specs with a lot more restrictions.

**Documents**

- `document.md` - The only text defining the standard.
- `example.yml` - The official example showcasing a YAML specs.
- `schema.json` - The JSON Schema to validate YAML specs (used for external tools)

**Test Suites**

- `schema` - Check if the JSON Schema properly validates YAML specs
