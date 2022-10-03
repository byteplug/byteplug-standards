<template>
  <div class="min-vh-100 d-flex flex-column">
    <div class="flex-grow-1 container">
      <div class="h-100 row mt-5">
        <div class="col-6">
          <div class="mb-5">
            <h1 class="h2 mb-2">Document Validator</h1>
            <div class="mb-4">
Validate your JSON documents with specs written in YAML. An alternative to JSON
Schema.
            </div>
            <div>
              <a
                href="https://validator.byteplug.io/"
                type="button"
                class="btn btn-primary text-white me-2"
              >Playground</a>
              <a
                href="/standards/json-validator/document.html"
                type="button"
                class="btn btn-primary text-white me-2"
              >Document</a>
              <button type="button" class="btn btn-primary text-white me-2">Toolkit</button>
            </div>
          </div>
          <div>
            <figure class="text-left">
              <blockquote class="blockquote">
                <p class="fs-6 f fst-italic">
How many times do we need to define what a valid input (or output) is. For JSON
documents, the JSON Schema vocabulary does the job, but couldn't its syntax be
nicer? This standard provides the easier-to-work-with alternative we need.
                </p>
              </blockquote>
              <figcaption class="blockquote-footer">
                Jonathan De Wachter, <cite title="Source Title">CTO at Byteplug</cite>
              </figcaption>
            </figure>
          </div>
        </div>
        <div class="col-6 d-flex flex-column justify-content-center">
          <div class="fw-bold">YAML Specs</div>
          <pre v-highlightjs="specsExample">
            <code class="yaml"></code>
          </pre>
          <div class="fw-bold">JSON Document</div>
          <pre v-highlightjs="validJson">
            <code class="json"></code>
          </pre>
        </div>
      </div>
    </div>
  </div>
  <div class="bg-dark text-white py-5">
    <div class="container">
      <h3>An alternative to JSON Schema</h3>
      <div class="mb-3">
This standard specifies how to write a YAML written specs to define what is a
valid JSON document. It can be seen as a simpler alterative to JSON Schema with
a nicer syntax and without its dynamic values.
      </div>
      <p class="fw-bold">Advantages over JSON Schema</p>
      <ul>
        <li>
          <p>Nice syntax</p>
          <p>
OK. It's not that hard to work with JSON Schema, but the syntax is annoyingly
awkward and is not as simple as it should be. Document Validator does not have
all these issues and is a lot more approachable.
          </p>
        </li>
        <li>
          <p>No dynamic values</p>
          <p>
Its simplicity is directly derived from a number of features it does NOT
implement. Notably, you will not find "dynamic values" (for instance, a value
that can either be a boolean or a number to be valid). The rational behind this
design decision is that it creates a whole set of pattern matching rules that
heavily complexity the matter. You will also find it creates caveats in tools.
          </p>
        </li>
        <li>
          <p>Simpler</p>
          <p>
Because it purposely aims to be simple, it makes it a less-bloated interface
to work with, and therefore is one of the strength. You will not find, in this
version and the upcoming versions, hundreds of custom types.
          </p>
        </li>
      </ul>
      <p>
Currently, the major disadvantage is the lack of a time-related type. Next
version of the standard will implement one along with (perhaps one or two)
other useful types.
      </p>
    </div>
  </div>
  <div class="container my-5">
    <h3>The Augmented Types</h3>
    <div class="mb-5">
It virtually extends the native JSON type system to build augmented types. All
augmented types have a YAML representation.
    </div>
    <div class="row">
      <div class="col-6">
        <div class="list-group">
          <a
            v-for="type_ in metadata.categories.fundamental.types"
            :key="type_"
            @click="selectedType = type_"
            class="list-group-item list-group-item-action"
            :class="{ 'active': selectedType == type_ ? true : false }"
          >
            {{ metadata.types[type_].name }}
          </a>
        </div>
        <div class="list-group my-4">
          <a
            v-for="type_ in metadata.categories.composite.types"
            :key="type_"
            @click="selectedType = type_"
            class="list-group-item list-group-item-action"
            :class="{ 'active': selectedType == type_ ? true : false }"
          >
            {{ metadata.types[type_].name }}
          </a>
        </div>
        <div class="list-group">
          <a
            v-for="type_ in metadata.categories.extra.types"
            :key="type_"
            @click="selectedType = type_"
            class="list-group-item list-group-item-action"
            :class="{ 'active': selectedType == type_ ? true : false }"
          >
            {{ metadata.types[type_].name }}
          </a>
        </div>
      </div>
      <div class="col-6">
        <!-- <div class="h5 fw-bold text-left mb-2">The '{{ selectedType }}' Type</div> -->
        <div class="mb-3">{{ metadata.types[selectedType].description }}</div>
        <div class="fw-bold">YAML Specs</div>
        <div>
          <pre class="mb-0" v-highlightjs="metadata.types[selectedType].example.specs">
            <code class="yaml"></code>
          </pre>
        </div>
        <div class="fw-bold">JSON Document</div>
        <div>
          <pre class="mb-0" v-highlightjs="metadata.types[selectedType].example.validDocument">
            <code class="json"></code>
          </pre>
        </div>
      </div>
    </div>
  </div>
  <div class="bg-primary text-white py-5" style="height: 500px;">
    <div class="container">
      <h3>A validation Playground</h3>
      <div>
To facilitate development, visit the playground. It allows you to toy around
with YAML schemas and see how it validates and invalidates JSON document. Not
only you can learn with it, but it will also remain useful as you work with
the standard.
      </div>
      <div class="row">
        <div class="col-6">
          Image
        </div>
        <div class="col-6">
          Image
        </div>
      </div>
    </div>
  </div>
  <div class="container my-5">
    <h3>With official Toolkits</h3>
    <div class="mb-3">
      Because a standard is merely a document describing things, we rely on
      tools to actually implement them. At Byteplug, we make intensive use of
      Python and JavaScript, and our toolkit are available under the MIT
      license.
    </div>
    <div class="row">
      <div class="col-6">
        <p class="h5 fw-bold">Python Toolkit</p>
        <ul class="mb-5">
          <li>
            <img src="@/assets/icons/email-address.svg" height="24"/>
            <span class="ms-2">Git Repository</span>
          </li>
          <li class="my-1">
            <img src="@/assets/icons/phone-number.svg" height="24"/>
            <span class="ms-2">Documentation</span>
          </li>
          <li>
            <img src="@/assets/icons/location.svg" height="24"/>
            <span class="ms-2">MIT License</span>
          </li>
        </ul>
        <pre v-highlightjs="foo"><code class="bash"></code></pre>
        <pre v-highlightjs="pythonToolkitExample"><code class="python"></code></pre>
      </div>
      <div class="col-6">
        <p class="h5 fw-bold">JavaScript Toolkit</p>
        <ul class="mb-5">
          <li>
            <img src="@/assets/icons/email-address.svg" height="24"/>
            <span class="ms-2">Git Repository</span>
          </li>
          <li class="my-1">
            <img src="@/assets/icons/phone-number.svg" height="24"/>
            <span class="ms-2">Documentation</span>
          </li>
          <li>
            <img src="@/assets/icons/location.svg" height="24"/>
            <span class="ms-2">MIT License</span>
          </li>
        </ul>
        <pre v-highlightjs="bar"><code class="bash"></code></pre>
        <pre v-highlightjs="javascriptToolkitExample"><code class="javascript"></code></pre>
      </div>
    </div>
    <div>
Note that lazy validation is supported by both toolkits. When validation
warnings and errors occur, a proper path is comes with the exception which
allow you to pinpoint where the mistake comes from.
    </div>
  </div>
</template>

<script>
import YAML from 'yaml'

import specsExample from '@/assets/document-validator/specs-example.yml?raw'
import validJson    from '@/assets/document-validator/valid-json.json?raw'
import invalidJson  from '@/assets/document-validator/invalid-json.json?raw'
import metadata from '@/assets/document-validator/metadata.yml?raw'

import pythonToolkitExample  from '@/assets/document-validator/python-toolkit-example.py?raw'
import javascriptToolkitExample  from '@/assets/document-validator/javascript-toolkit-example.js?raw'

export default {
  name: 'DocumentValidator',
  components: {
    // NavigationBar
  },
  data() {
    return {
      specsExample: specsExample,
      validJson: validJson,
      invalidJson: invalidJson,

      metadata: YAML.parse(metadata),
      selectedType: 'number',

      pythonToolkitExample: pythonToolkitExample,
      javascriptToolkitExample: javascriptToolkitExample,

      foo: "pip install byteplug-document",
      bar: "npm install @byteplug/document"
    }
  }
}
</script>

<style lang="css" scoped>
ul {
  list-style-type: none;
}
</style>