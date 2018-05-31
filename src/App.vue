<template>
  <div>
    <h1 class="title">Evergreen New Releases</h1>
    <Menu v-on:urlSet="urlSet" :url="url" :libraryNumber="libraryNumber" />
    <hr/>

    <p>Url: {{url}}</p>

    <DvdList :dvds="dvds" :url="url" />
  </div>
</template>

<script>
 import Menu from './components/Menu';
 import DvdList from './components/DvdList';
 const SEARCH_URL = '/opac/extras/opensearch/1.1?_adv=1&detail_record_view=0&fi%3Aitem_type=g&fi%3Avr_format=v&locg=132&pubdate=is&date1=&date2=&sort=pubdate.descending';
 
 export default {
   name: 'App',
   
   data() {
     return {
       url: '',
       libraryNumber: 1,
       dvds: []
     }
   },
   
   created() {
     this.url = localStorage.getItem('evergreen_url');
     this.libraryNumber = localStorage.getItem('library_number');
     console.log('created this.libaryNumber:', this.libraryNumber);
     this.getDvds();
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
     
     libraryNumberSet(number) {
       this.libraryNumber = number;
     },
     
     getDvds() {
       if (this.url.length) {
	 console.log('url:', this.url + SEARCH_URL); /* eslint-disable-line no-console */
	 // 
	 const searchUrl = '/eg/opac/results?bool=and&qtype=keyword&contains=contains&query=&bool=and&qtype=title&contains=contains&query=&bool=and&qtype=author&contains=contains&query=&_adv=1&detail_record_view=0&fi%3Aitem_type=g&fi%3Avr_format=v&locg=' + this.libraryNumber + '&pubdate=is&date1=&date2=&sort=pubdate.descending';
	 console.log('getDvds() searchUrl:', searchUrl);


	 /* var headers = new Headers();
	    headers.append('Content-Type', 'application/atom+xml'); */
	 
	 // Disable cors headers.
	 const CORS_PROXY = "https://cors-anywhere.herokuapp.com/"
	 const request = new Request(CORS_PROXY + this.url + searchUrl);
	 
	 // Get the data.
	 fetch(request)
	   .then(function(response) {
	     /* 	     console.log('fetch response:', response.arrayBuffer()); */
	     return response.text()
	   })
	   .then((text) => {
	     const rows = $(text).find('.record_title.search_link');
	     console.log('rows:', rows);
	     const titles = rows.map((idx, row) => {
	       return $(row).html().split('[videorecording]')[0].trim();
	     });

	     console.log('title:', titles);

	     // Get DVD info from yts.am.
	     $.each(titles, (idx, title) => {
	       console.log("'https://yts.am/ajax/search?query=' + title:", 'https://yts.am/ajax/search?query=' + title);
	       fetch('https://yts.am/ajax/search?query=' + title, {mode: 'no-cors'})
		 .then((response) => {
		   console.log('fetch yts.am response:', response);
		 });
	     });
	   });
	     
	     /* arrayBuffer CORS_PROXY = "https://cors-anywhere.herokuapp.com/"
		
		var oReq = new XMLHttpRequest();
		
		oReq.onload = (e) => {
		const xml = new DOMParser().parseFromString(oReq.response,'text/xml');
		this.dvds = xml.getElementsByTagName('atom:entry');
		console.log('this.dvds[0]:', this.dvds[0]);
		}
		
		oReq.open("GET", CORS_PROXY + this.url + SEARCH_URL);
		oReq.setRequestHeader('Content-Type', 'application/atom+xml');
		oReq.setRequestHeader('Mode', 'no-cors');
		oReq.send(); */
       } else {
	 console.log('Please set url...'); /* eslint-disable-line no-console */
       }
     }
   },
   /* mounted() {
    *   this.$nextTick(function () {
    *     this.getDvds();
    *   });
    * } */
 }
</script>
