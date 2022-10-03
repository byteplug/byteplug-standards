import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import "bootstrap/dist/css/bootstrap.css"
import "@/main.scss"
import 'bootstrap'

import Website from './Website.vue'
import DocumentValidator from '@/views/DocumentValidator.vue'
import Endpoints from '@/views/Endpoints.vue'

const app = createApp(Website)

const routes = [
  {
      path: '/',
      name: 'Home'
  },
  {
      path: '/document-validator',
      name: 'DocumentValidator',
      component: DocumentValidator
  },
  {
      path: '/endpoints',
      name: 'Endpoints',
      component: Endpoints
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

app.use(router)

import VueHighlightJS from 'vue3-highlightjs'
import 'highlight.js/styles/solarized-light.css'
app.use(VueHighlightJS)

app.mount('#website')
