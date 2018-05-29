<template>
  <div>
    <h1 class="title">Evergreen New Releases</h1>
    <Menu v-on:urlSet="urlSet" :url="url" />
    <hr/>

    <p>Url: {{url}}</p>

    <DvdList :dvds="dvds" :url="url" />
  </div>
</template>

<script>
 import Menu from './components/Menu';
 import DvdList from './components/DvdList';
 const SEARCH_URL = '/opac/extras/opensearch/1.1?searchTerms=thor&searchClass=keyword&count=25';
 
 export default {
   name: 'App',
   data() {
     return {
       url: '',
       dvds: []
     }
   },
   created() {
     this.url = localStorage.getItem('evergreen_url');
   },
   components: {
     Menu,
     DvdList
   },
   methods: {
     urlSet(url) {
       console.log('urlSet url:', url, SEARCH_URL); /* eslint-disable-line no-console */
       this.url = url;
     },
     getDvds() {
       if (this.url.length) {
	 console.log('url:', this.url + SEARCH_URL); /* eslint-disable-line no-console */
	 /* var headers = new Headers();
	    headers.append('Content-Type', 'application/atom+xml');
	    
	    // Disable cors headers.
	    const request = new Request(this.url + SEARCH_URL, {mode: 'no-cors', headers});
	    

	    // Get the data.
	    fetch(request)
	    .then(function(response) {
	    console.log('fetch response:', response);
	    }) */
	 const CORS_PROXY = "https://cors-anywhere.herokuapp.com/"
	 
	 var oReq = new XMLHttpRequest();
	 
	 oReq.onload = (e) => {
	   /* 	   console.log('oReq.response:', oReq.response); */
	   const xml = new DOMParser().parseFromString(oReq.response,'text/xml');
	   /* 	   console.log('onload xml:', xml.getElementsByTagName('atom:entry')); */
	   this.dvds = xml.getElementsByTagName('atom:entry');
	   console.log('this.dvds[0]:', this.dvds[0]);
	 }
	 
	 oReq.open("GET", CORS_PROXY + this.url + SEARCH_URL);
	 oReq.setRequestHeader('Content-Type', 'application/atom+xml');
	 oReq.setRequestHeader('Mode', 'no-cors');
	 oReq.send();
       } else {
	 console.log('Please set url...'); /* eslint-disable-line no-console */
       }
     }
   },
   mounted() {
     this.$nextTick(function () {
       this.getDvds();
     });
   }
 }
</script>
