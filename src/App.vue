<template>
  <div>
    <h1 class="title">Evergreen New Releases</h1>
    <Menu v-on:urlSet="urlSet" storedUrl=this.url />
    <hr/>

    <p>Url: {{url}}</p>
  </div>
</template>

<script>
 import Menu from './components/Menu';
 const SEARCH_URL = '/opac/extras/opensearch/1.1?searchTerms=thor&searchClass=keyword&count=25';
 
 export default {
   name: 'App',
   data() {
     return {
       url: ''
     }
   },
   created() {
     this.url = localStorage.getItem('evergreen_url');
   },
   components: {
     Menu
   },
   methods: {
     urlSet(url) {
       console.log('urlSet url:', url, SEARCH_URL); /* eslint-disable-line no-console */
       this.url = url;
     }
   }
 };
</script>
