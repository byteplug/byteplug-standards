# Document Validator: Augmented JSON documents

This is **version 1.0** of this document. Written by **Jonathan De Wachter**, in
June 2022. Released under the **CC BY-NC-SA 4.0** license.

## Abstract

Document Validator is a standard developed by Byteplug to provide a simpler
alternative to JSON Schema. This document fully describes the standard.

## Notes to the readers

This document is purposely written informally. Instead of heavily specifying
everything single aspect, and thus making this document more dull than
necessary, it relies on developer's common sense. If some part of this document
is really ambiguous, you can report it and it will be updated accordingly.

## Copyright notice

This document is released under the **CC BY-NC-SA 4.0** license with all rights
reserved to **Byteplug**.

---

**Table of Content**

- Introduction
  - Comparison with JSON Schema
  - Motivations behind this standard
  - Expectation for the upcoming versions
- Terminology
  - The hyphen-lowercase regex
- The native JSON types
- The augmented types
- YAML representation of types
- Notion of optional
- Default values
- The fundamental types
  - The 'flag' type
  - The 'integer' type
  - The 'decimal' type
  - The 'string' type
  - The 'enum' type
- The composite types
  - The 'list' type
  - The 'tuple' type
  - The 'map' type
- The utility types
  - The 'time' type
  - The 'date' type
  - The 'datetime' type
  - The 'duration' type

~~The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 RFC2119 RFC8174 when, and only when, they appear in all capitals, as shown here.~~

No. This document isn't going to this formal. Its audience is human developers
and thus, the content should be easy to read and digest. If a part of this
document is unclear and really keeps you from implementing it, report it on the
Github issues tracker and it will be updated accordingly.

## Introduction

The **Document Validator** standard specifies how to write a YAML written specs
that defines what is a valid JSON document. It virtually extends the native
JSON type system to introduce augmented types, and thus, convey more
information.

Note that it doesn't specify how those augmented types must be converted or
represented in some programming languages; it only specifies how they must be
represented in a JSON document.

### Comparison with JSON Schemas

It can be seen as an alterative to JSON Schema with a nicer syntax (in YAML,
instead of JSON), with far less features, and most importantly, without its
matching pattern rules.

The most striking points compared to JSON Schema is the absence of default
values. But it does have a notion of optional values (the absence of a value is
a value).

### Motivations behind this work

We use our own HTTP API standard at Byteplug, and it exclusively uses JSON as a
communication medium. Indirectly we constantly need to validate and document
those JSON input and output. JSON Schema was our initial choice for the job
before we developed our own simpler in-house alternative.

We were not happy with JSON Schema because it was more complicated than it
should be for our relatively simple use cases. We saw rooms for a clearer
syntax and simpler set of rules that would tremendously facilitate development
on our side; from making design decisions, understand implementations and
generating documentation.

### Expectation for the upcoming versions

This standard won't grow in complexity in the future. Notably, complex matching
pattern rules won't be added, not because they're hard to understand or even
implement, but because it creates subtleties and make documenting a lot more
complicated.

It may support validating YAML documents later. It will introduce more
augmented types (the common ones). This document will become more formal and
get more precise. Notion of default values may be added.

Random little things that is likely to be added.

- Scientific notation
- Support fancy literals (0b0101001, 0xFA37)
- More properties for each augmented types
- Support values `-Infinity'` and `NaN` for decimal types
- Add more precision as for encoding of string.

It will strive for a sweet spot, convenience during development and without
adding unwanted complexity.

## Terminology

To be written.

- Schema

- Field

The terminology is used in two cases, for the map type. A map has the concept of
list of key-value pairs also called field.

To be written.

### The hyphen-lowercase regex

More than once throughout this standard, you will find naming restrictions.
This is often a matter of forcing simplicity and creating homogeneity rather
than caused by some underlying technical limitation.

One of the notable naming restriction is what we are going to refer as the
**hyphen-lowecase regex** in this document. The regex that corresponds to this
naming restriction is `^[a-z]+(-[a-z]+)*$`.

In English words, a valid name can only contain the lowercase version of the
alphabet of the ASCII characters, and can also contain hyphen, except that the
name can't start or end with an hyphen character.

It's a lot common out there and examples will speak better than words.

**Valid names**

- foobar
- foo-bar

**Invalid names**

- Foobar
- foo_bar
- -foobar
- barfoo-
- foo--bar

This naming restriction is used for the keys of the map type, and for the
values of an enum type.

## The native JSON types

Because this standard augments the JSON type system, it's good to refresh
memory as to what the native JSON types are.

- a string
- a number
- an object (JSON object)
- an array
- a boolean
- null

Notes for JavaScript developers, it can't be a function, date or 'undefined'.

This standard augments this type system but it must of course re-use the
the native types to represent the augmented types. For instance, a decimal
number could be represented as a JSON string, or if you want a more silly
example, a binary type could be represented as a JSON array of JSON booleans.

As you'll see later, the JSON null value is never used to represent any
augmented type, it's exclusively used to represent the absence of value, a
concept named 'option' and introduced later in this document.

## The augmented types.

This standard adds the following types which are categorized into the
**fundamental types** and the **composite types** categories. To make it a lot
clearer, it also adds the a third category, the **utility types** category,
but they should be seen as fundamental types as they're just non-composite
types that don't have any extra characteristics.

The fundamental types are `flag`, `integer`, `decimal`, `string`, `enum`.
The composite types are `list`, `tuple` and `map`.
The utility types are `time`, `date`, `datetime` and `duration`.

In case you're wondering, the "flag" type is the boolean type.

## YAML representation of types

Each augmented type can be described by one YAML block. With the composite
types, the YAML blocks eventually start to nest into each other. For an early
example of what those blocks look like, consider the following simple block.

```yaml
type: integer
```

It will validate any integer. To restrict further what is a valid integer, add
properties.

```yaml
type: integer
minimum: 10
maximum:
  exclusive: false
  value: 42
```

It will validate any integer greater or equal to 10, and strictly lower than
42.

## Notion of optional

The notion of optionality is shared among ALL augmented types. If one type is
marked as optional, with `option: true`, the value can be a JSON null and
should be thought of the absence of the value.

For instance, the following specs will accept either "null" or an actual
number.

```yaml
type: integer
option: true
```

For Rust programers, it can be thought of the `Option<T>` type and for C++
programmer, it can be thought of the `std::optional<T>` type.

## Default values

This standard introduces no notion of default value. All values must be
explicit and included in the document in order to be valid. One alternative is
to use the 'option' feature to represent the absence of value.

Technical reason behind this decision is that, while it's an undeniable very
convenient feature, it does introduce subtle confusions, sometimes. It doesn't
blend nicely with the 'option' feature, and because root element of JSON
document is mandatory, it introduce some unwanted complexity.

## The fundamental types

A fundamental type is just a non-composite type, meaning they're the leaves of
the tree structure of the JSON document and won't allow further ramification.
This category also excludes the utility types and only contains the most common
primitive types any programmer work with regardless of the programming
language.

Just like any type, they all can be optional, with `option: true` property.

### The 'flag' type

The flag type is the common boolean type with a fancy name. It's implemented
with the JSON boolean type and has no notable particular behavior.

**YAML representation**

The simplest YAML representation of the flag type is the following.

```yaml
type: flag
```

It doesn't support more properties.

**JSON implementation**

The flag type has a one-on-one mapping with the JSON boolean type, which is
therefore used to implement the flag type.

Example of valid JSON document.

```json
true
```

For the following specifications.

```yaml
type: flag
```

### The 'integer' type

The integer type represents the common integer type of the other programming
languages. It's implemented with the JSON number type and has the decimal part
(if any) discarded. The value can be negative, zero and positive. It has no
notable particular behavior.

The default value is 0 if not specified (review this).

It can define restrictions as to what values are accepted. It can defines a
valid range and whether it should be a multiple of another integer.

**YAML representation**

The simplest YAML representation of the integer type is the following.

```yaml
type: integer
```

Use the `minimum` or `minimum_exclude` fields to restrict the value to be
higher than another integer. Both fields cannot be used at the same time.

```yaml
type: integer
minimum_exclude: 42
```

Use the `minimum` or `minimum_exclude` fields to restrict the value to be
higher than another integer. Both fields cannot be used at the same time.

```yaml
type: integer
minimum_exclude: 42
```

If minimum is higher than the maximum, it's invalid.

Its default value can be defined by a YAML integer value.

```yaml
type: integer
default: 42
```

**JSON implementation**

The integer type is implemented with a JSON number. Because the JSON number
supports decimal numbers too, the decimal part is simply discarded.

Example of valid JSON document.

```json
42
```

For the following specifications.

```yaml
type: integer
minimum_exclude: 10
maximum: 100
multiple_of: 2
```

### The 'decimal' type

The decimal type can represents the common floating-point type of the other
programming languages. It's implemented with the JSON number type and therefore
share the same limitation in terms of precision. The value can be negative,
zero and positive. It has no notable particular behavior.

Its default value is 0.0 when not specified.

**YAML representation**

The simplest YAML representation of the decimal type is the following.

```yaml
type: decimal
```

<!-- A valid range can be specified with the `min` and `max` fields.

```yaml
type: decimal
min: 10
max: 100
``` -->

Its default value can be defined by a YAML floating-point number value.

```yaml
type: decimal
default: 4.2
```

**JSON implementation**

The decimal type is implemented with a JSON number. Because the JSON number
supports decimal numbers too, it shares its limiation in terms of precision.

Example of valid JSON document.

```json
4.2
```

For the following specifications.

```yaml
type: decimal
```

### The 'string' type

The string type represents the common string type of the other programming
languages, or in other words, an array of human-readable characters. Details
related to encoding format is not defined by this standard. It's implemented
with the JSON string type and its default value is an empty string when not
specified.

It can define restrictions as to what values are accepted with the form of a
regex. It can also restricts the number of charaters it should .

**YAML representation**

The simplest YAML representation of the string type is the following.

```yaml
type: string
```

A length can be defined with `length_minimum` and `length_maximum`.

```yaml
type: string
length_minimum: 10
length_maximum: 100
```

To be written.

```yaml
type: string
pattern: foobar
```

To be written.

Its default value can be defined by a YAML string value.

```yaml
type: string
default: "Hello world!"
```

**JSON implementation**

The string type is implemented with a JSON string. Because the JSON number.

Example of valid JSON document.

```json
"Hello world!"
```

For the following specifications.

```yaml
type: string
pattern: foo
length_minimum: 0
length_maximum: 100
```

### The 'enum' type

To be written.

## The composite types

The composite types allow to create nested data structure. They can be
optional, with `option: true` just like all types, but they do not have
default values. However, they honor the default values of their children. The
rules as how they honor the default value depends on the composite type.

### The 'list' type

The list type represents a dynamic array.
Dynamic array means that the number of elements is not known in advance, meaning it can
contain from 0 element up to an undefined amount of element.

All elements must be of a single type. If you're wondering why it doesn't
support multiple types value, that's because it would open a whole world of
pattern-matching related rules. If really need dynamic, use the json type and
you become responsible for the validation of the JSON value.

Elements are accessed using an integer index.


```yaml
type: list
```

To be written.

```yaml
type: list
foo: bar
bar: foo
```

To be written.

```yaml
type: list
default: foobar
```

To be written.

### The 'tuple' type

The tuple type represents a fixed array.
Fixed array means that the number of elements is known in advance, meaning that it
can't be smaller or bigger than defined.

Elements are accessed using an integer index.

It behaves and is akin to the 'map' type except that the elements are not named, therefore refer to the map type to understand the behavior of the tuple type.

```yaml
type: tuple
```

To be written.

```yaml
type: tuple
foo: bar
bar: foo
```

To be written.

```yaml
type: tuple
default: foobar
```

To be written.

### The 'map' type

The map type represents a set of key-value pairs called field. The number of
fields are fixed and the fields are ordered.

Values are accessed using keys, keys that must be string following the foobar
pattern.

If the field is missing, the default value of the value is used. Note that if the
value has the option set to yes.

**JSON implementation**

The map type is implemented with a JSON object where the key is the key of the
map and the value is the value of the map. (reword this)

```json
{
    "foo": 42,
    "bar": "Hello world"
}
```

This example showed the representation of a map

```yaml
type: map
fields:
  foo:
    type: number
  bar:
    type: string
```

**YAML specification**

```yaml
type: map
```

To be written.

```yaml
type: map
foo: bar
bar: foo
```

To be written.

```yaml
type: map
default: foobar
```

To be written.

## The utility types

The convenience types are non-composite types are therefore can be optional
with `option: true` and can have a default value. The only reason why they're
described in a separate category is not to bloat the non-composite types
category and because they're not the most primitive types in the sense that
they can be implemented by the users on top of the primitive types.

### The 'time' type

To be written.

```yaml
type: time
```

To be written.

```yaml
type: time
foo: bar
bar: foo
```

To be written.

```yaml
type: time
default: foobar
```

To be written.

### The 'date' type

To be written.

```yaml
type: date
```

To be written.

```yaml
type: date
foo: bar
bar: foo
```

To be written.

```yaml
type: date
default: foobar
```

To be written.

### The 'datetime' type

To be written.

```yaml
type: datetime
```

To be written.

```yaml
type: datetime
foo: bar
bar: foo
```

To be written.

```yaml
type: datetime
default: foobar
```

To be written.

### The 'duration' type

To be written.

```yaml
type: duration
```

To be written.

```yaml
type: duration
foo: bar
bar: foo
```

To be written.

```yaml
type: duration
default: foobar
```

To be written.
