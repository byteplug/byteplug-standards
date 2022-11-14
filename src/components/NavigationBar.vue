<template>
  <header>
    <div class="navbar navbar-dark bg-dark shadow-sm">
      <div class="container">
        <a
          class="navbar-brand d-flex align-items-center"
          @click="$router.push('/')"
          >
          <img src="@/assets/logo-white.svg" height="42" class="me-3">
          <!-- <strong>Byteplug Standards</strong> -->
        </a>
        <div class="dropdown">
          <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
            <span v-if="$route.name == 'DocumentValidator'">Document Validator</span>
            <span v-else-if="$route.name == 'Endpoints'">Endpoints</span>
          </button>
          <ul class="dropdown-menu">
            <li>
              <router-link
                class="dropdown-item"
                to="document-validator"
              >Document Validator</router-link>
            </li>
            <li>
              <router-link
                class="dropdown-item"
                to="endpoints"
                disabled
              >Endpoints</router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
export default {
  name: "NavigationBar"
}
</script>
