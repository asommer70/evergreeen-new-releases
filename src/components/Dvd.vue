<template>
  <li>
    ID: {{getId}}
    <br/>
    TITLE: {{dvd.getElementsByTagName('title')[0].textContent}}
    <br/>
    <img alt="" :src="getImg" />
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
       return this.dvd.getElementsByTagName('id')[0].textContent;
     },
     getImg() {
       return this.url + '/Opac/extras/ac/jacket/medium/r/' + this.getId();
     }
   }
 }
</script>

<style>
 
</style>
