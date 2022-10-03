<template>
  <main>
    <div>Byteplug Standards</div>
    <div v-if="$route.path === '/'">
      <router-link to="/document-validator">Document Validator</router-link>
      <br>
      <router-link to="/endpoints">Endpoints</router-link>
    </div>
    <router-view v-else/>
  </main>
</template>

<style>
html, body, #app {
  height: 100%;
}

@font-face {
  font-family: "Xolonium";
  src: local("Xolonium"), url(./fonts/Xolonium/Xolonium-Regular.ttf) format("truetype");
}
</style>
