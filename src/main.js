import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'

import "bootstrap/dist/css/bootstrap.css"
import "@/main.scss"
import 'bootstrap'

import Website from './Website.vue'
import Home from '@/views/Home.vue'
import DocumentValidator from '@/views/DocumentValidator.vue'
import Endpoints from '@/views/Endpoints.vue'
import Paper from '@/views/Paper.vue'

const app = createApp(Website)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/document-validator',
    name: 'DocumentValidator',
    component: DocumentValidator
  },
  {
    path: '/document-validator/document',
    name: 'DocumentValidatorPaper',
    component: Paper
  },
  {
    path: '/endpoints',
    name: 'Endpoints',
    component: Endpoints
  },
  {
    path: '/endpoints/document',
    name: 'EndpointsPaper',
    component: Paper
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
