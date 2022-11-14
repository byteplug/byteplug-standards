<template>
  <div class="min-vh-100 d-flex flex-column">
    <navigation-bar/>
    <section class="py-5 text-center container">
      <div class="row py-lg-5">
        <div class="col-lg-6 col-md-8 mx-auto">
          <h1 class="fw-light">Endpoints*</h1>
          <p class="lead text-muted">
            An even simpler than OAS set of HTTP API rules making development
            simpler and headache-free.
          </p>
          <p>
            <a
              href="#browser-section"
              class="btn btn-primary my-2 me-2"
            >Browser</a>
            <router-link
              to="/endpoints/document"
              class="btn btn-secondary my-2 me-2"
            >Document (draft)</router-link>
            <a
              href="#toolkits-section"
              class="btn btn-secondary my-2"
            >Toolkits</a>
          </p>
          <div class="fst-italic">*This is a development version; do not use in production software until it reaches stable version.</div>
        </div>
      </div>
    </section>
    <div class="bg-light" style="height:500px;">
      <div class="container h-100">
        <div class="row h-100">
          <div class="col-5 d-flex flex-column justify-content-center">
            <figure class="text-left">
              <blockquote class="blockquote">
                <p class="fs-6 f fst-italic">
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
          <div class="col-1"></div>
          <div class="col-6 d-flex flex-column justify-content-center">
            <pre v-highlightjs="specsExample">
              <code class="yaml"></code>
            </pre>
          </div>
        </div>
      </div>
    </div>
  </div>


  <div class="bg-dark text-white py-5" style="height: 500px;">
    <div class="container">
      <h3>An alternative to OpenAPI Specification (OAS)</h3>
      <div class="mb-3">
This standard specifies how an HTTP API should be implemented and behave, by
respecting a set of rules. It forces software to implement and work with
consistent and simple HTTP API interface. It's a simpler and cleaner
alternative to OpenAPI Specification.
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
  <div
    id="browser-section"
    class="bg-primary text-white py-5"
  >
    <div class="container">
      <h3>Online HTTP API Browser</h3>
      <div>
Our browser gives you a helpful view of your HTTP API, which is useful during
both early development and later after release. If you're developing it using
our toolkit, it becomes automatically browsable because it creates an endpoint
exposing its YAML specification.
      </div>
      <div class="row">
        <div class="col-2"></div>
        <div class="col-8">
          <img
            src="/screenshots/endpoints-browser-screenshot.png"
            class="img-fluid py-5"
          >
        </div>
        <div class="col-2"></div>
      </div>
      <div class="text-center">
        <a href="https://browser.byteplug.io" class="btn btn-dark">Open the Software</a>
      </div>
    </div>
  </div>
  <div id="toolkits-section" class="container my-5">
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
        <p class="h5 fw-bold">JavaScript Client (not official)</p>
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
        <pre v-highlightjs="javascriptClientExample"><code class="javascript"></code></pre>
      </div>
    </div>
    <div>
Note that the Python toolkit is built on top of <b>Flask</b> and the JavaScript
toolkit is built on top of <b>express.js</b>.
    </div>
  </div>
</template>

<script>
import NavigationBar from '@/components/NavigationBar.vue'
import specsExample from '@/assets/endpoints/specs-example.yml?raw'
import pythonToolkitExample  from '@/assets/endpoints/python-toolkit-example.py?raw'
import javascriptClientExample  from '@/assets/endpoints/javascript-client-example.js?raw'

export default {
  name: 'Endpoints',
  components: {
    NavigationBar
  },
  data() {
    return {
      specsExample: specsExample,
      pythonToolkitExample: pythonToolkitExample,
      javascriptClientExample: javascriptClientExample,
      foo: "pip install byteplug-endpoints",
      bar: "npm install byteplug-endpoints"
    }
  }
}
</script>
