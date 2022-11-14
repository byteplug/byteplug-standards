<template>
  <div class="min-vh-100 d-flex flex-column">
    <router-view class="flex-grow-1"/>
    <footer class="text-center py-3">© 2022 Byteplug Inc. All rights reserved.</footer>
  </div>
</template>

<style>
html, body, #website{
  height: 100%;
}

@font-face {
  font-family: "Xolonium";
  src: local("Xolonium"), url(./fonts/Xolonium/Xolonium-Regular.ttf) format("truetype");
}
</style>
