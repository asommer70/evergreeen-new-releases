<template>
  <li>
    ID: {{getId}}
    <br/>
    TITLE: {{dvd.getElementsByTagName('title')[0].textContent}}
    <br/>
    <img alt="" :src="imgSrc" />
    <br/>
    ISBN: {{isbn}}
    <hr/>
  </li>
</template>

<script>
 // Link for item:
 // /opac/extras/unapi?id=tag:open-ils.org,2018-05-29:biblio-record_entry/2303081/-&format=opac
 
 // URL for Image:
 // http://nccardinal.org/Opac/extras/ac/jacket/medium/r/2303081
 
 export default {
   name: 'Dvd',
   props: ['dvd', 'url'],
   computed: {
     getId() {
       return this.dvd.getElementsByTagName('id')[1].textContent;
     },
     imgSrc() {
       return this.getImg();
     },
     isbn() {
       try {
	 return this.dvd.getElementsByTagName('dc:identifier')[0].textContent;
       } catch (e) {
       }
     }
   },
   methods: {
     getImg() {
       // http://nccardinal.org/eg/opac/results?bool=and&qtype=keyword&contains=contains&query=&bool=and&qtype=title&contains=contains&query=&bool=and&qtype=author&contains=contains&query=&_adv=1&detail_record_view=0&fi%3Aitem_type=g&fi%3Avr_format=v&locg=132&pubdate=is&date1=&date2=&sort=pubdate.descending
       return this.url + '/opac/extras/ac/jacket/medium/r/' + this.getId.split('/')[1];
     }
   }
 }
</script>

<style>
 
</style>
