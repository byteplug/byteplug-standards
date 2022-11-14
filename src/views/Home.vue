<template>
  <div
    class="container"
    style="margin-top: 80px;"
  >
    <div class="p-5 mb-4 bg-light rounded-3">
      <div class="container-fluid py-5">
        <h1 class="display-5 fw-bold">Development Made Easier</h1>
        <p class="col-md-8 fs-4">
          Simplify development process by adopting dead-easy standards.
        </p>
        <div class="pt-3">
          <button
            class="btn btn-outline-primary btn-lg me-2"
            type="button"
            @click="$router.push('document-validator')"
          >Document Validator</button>
          <button
            class="btn btn-outline-primary btn-lg"
            type="button"
            @click="$router.push('endpoints')"
          >Endpoints</button>
        </div>
      </div>
    </div>
    <div class="row align-items-md-stretch">
      <div class="col-md-6">
        <div class="h-100 p-5 text-bg-dark rounded-3">
          <h2>Open-source Tools</h2>
          <p>
            Our standards come with useful web-based tools to help you develop
            software. Bonus point, they are entirely open-source.
          </p>
          <a
            href="https://validator.byteplug.io"
            class="btn btn-outline-light me-2"
            type="button"
          >Validation Playground</a>
          <a
            href="https://browser.byteplug.io"
            class="btn btn-outline-light"
            type="button"
          >Endpoints Browser</a>
        </div>
      </div>
      <div class="col-md-6">
        <div class="h-100 p-5 bg-light border rounded-3">
          <h2>Battle-tested Libraries</h2>
          <p>
            Whether you write in Python or JavaScript, we got you covered.
            You'll benefit from the same battle-tested libraries we use in
            our own software.
          </p>
          <a
            href="https://docs.byteplug.io/python"
            class="btn btn-outline-dark me-2"
            type="button"
          >Python</a>
          <a
            href="https://docs.byteplug.io/javascript"
            class="btn btn-outline-dark"
            type="button"
          >JavaScript</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>
