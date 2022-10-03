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
