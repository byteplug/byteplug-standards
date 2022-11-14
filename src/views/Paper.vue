<template>
  <div class="container bg-light">
    <div v-if="$route.name == 'DocumentValidatorPaper'" v-html="documentValidatorHtml"></div>
    <div v-else-if="$route.name == 'EndpointsPaper'" v-html="endpointsHtml"></div>
  </div>
</template>

<script>
import MarkdownIt from 'markdown-it'
import documentValidatorMarkdown from '@/standards/document-validator/1.0/document.md?raw'
import endpointsMarkdown from '@/standards/endpoints/1.0/document.md?raw'

var markdownRenderer = new MarkdownIt()

export default {
  name: 'Paper',
  data() {
    return {
      documentValidatorHtml: markdownRenderer.render(documentValidatorMarkdown),
      endpointsHtml: markdownRenderer.render(endpointsMarkdown)
    }
  }
}
</script>
