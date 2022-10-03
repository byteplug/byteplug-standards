<template>
  <div class="min-vh-100 d-flex flex-column">
    <navigation-bar/>
    <div class="flex-grow-1 container">
      <div class="h-100 row mt-5">
        <div class="col-6">
          <div class="mb-5">
            <h1 class="h2 mb-2">Byteplug HTTP API</h1>
            <div class="mb-4">
An even simpler than OAS set of HTTP API rules making development simpler and
headache-free.
            </div>
            <div>
              <a
                href="https://browser.byteplug.io/"
                type="button"
                class="btn btn-primary text-white me-2"
              >Browser</a>
              <a
                href="/standards/http-api/document.html"
                type="button"
                class="btn btn-primary text-white me-2"
              >Document</a>
              <button type="button" class="btn btn-primary text-white me-2">Toolkit</button>
            </div>
          </div>
          <div>
            <figure class="text-left">
              <blockquote class="blockquote">
                <p>
We grew sick of overly complicated HTTP API standards that are not as
developer-friendly as they could be. The result is our in-house standard,
simple behavior rules, simple YAML specs format and development tools.
                </p>
              </blockquote>
              <figcaption class="blockquote-footer">
                Jonathan De Wachter, <cite title="Source Title">CTO at Byteplug</cite>
              </figcaption>
            </figure>
          </div>
        </div>
        <div class="col-6">
          Right Side
        </div>
      </div>
    </div>
  </div>
  <div class="bg-dark text-white py-5" style="height: 500px;">
    <div class="container">
      <h3>Meet the sweet alternative to OpenAPI Specification</h3>
      <div class="mb-3">
Byteplug HTTP API is standard that specifies how an HTTP API should be
implemented and behave, with respect to a set of rules. It forces software to
implement and work with consistent and simple HTTP API interface.
<!-- <br><br> -->
It's a simpler and cleaner alternative to OpenAPI Specification.
      </div>
      <p class="fw-bold">Advantages over OpenAPI Specification</p>
      <ul>
        <li>
          <p>Foo</p>
          <p>
Aenean nec ligula eu purus iaculis commodo. In lectus enim, molestie non massa
lobortis, pulvinar elementum lorem.
          </p>
        </li>
        <li>
          <p>Bar</p>
          <p>
Pellentesque egestas mi nisl. Maecenas ullamcorper orci eget rhoncus auctor.
          </p>
        </li>
        <li>
          <p>Quz</p>
          <p>
Fusce lobortis, justo a cursus suscipit, ligula turpis ultrices arcu, vel
faucibus turpis turpis volutpat dui.
          </p>
        </li>
      </ul>
    </div>
  </div>
  <div class="container my-5">
    <h3>The Set of Rules</h3>
    <div class="mb-3">
Fusce lobortis, justo a cursus suscipit, ligula turpis ultrices arcu, vel
faucibus turpis turpis volutpat dui.
    </div>
    <div class="row">
      <div class="col-6">
        Left Side
      </div>
      <div class="col-6">
        Right Side
      </div>
    </div>
  </div>
  <div class="bg-primary text-white py-5" style="height: 500px;">
    <div class="container">
      <h3>Online HTTP API Browser</h3>
      <div>
Our browser gives you a helpful view of your HTTP API, which is useful during
both early development and later after release. If you're developing it using
our toolkit, it becomes automatically browsable because it creates an endpoint
exposing its YAML specification.
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
    <h3>Python and Erlang Toolkit</h3>
    <div class="mb-3">
      Because a standard is merely a document describing things, we rely on
      tools to get it right.<br>
      At Byteplug, we make intensive use of Python and Erlang, and our toolkit
      are available under the MIT license.
    </div>
    <div class="row">
      <div class="col-6">
        <pre v-highlightjs="pythonToolkitExample"><code class="python"></code></pre>
      </div>
      <div class="col-6">
        <pre v-highlightjs="erlangToolkitExample"><code class="erlang"></code></pre>
      </div>
    </div>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'

// import pythonToolkitExample  from '@/assets/examples/validator/python-toolkit-example.py?raw'
// import erlangToolkitExample  from '@/assets/examples/validator/erlang-toolkit-example.erl?raw'

export default {
  name: 'Endpoints',
  components: {
    NavigationBar
  },
  data() {
    return {
      // pythonToolkitExample: pythonToolkitExample,
      // erlangToolkitExample: erlangToolkitExample
    }
  }
}
</script>
