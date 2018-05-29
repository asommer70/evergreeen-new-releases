<template>
  <div>
    <p>{{dvds.length ? '': 'Gettings DVDs...'}}</p>
    <ul>
      <Dvd v-for="dvd in dvds" :dvd="dvd" :key="dvd.getElementsByTagName('id')[0].textContent" :url="url" />
    </ul>
  </div>
</template>

<script>
 import Dvd from './Dvd';
 
 export default {
   name: 'DvdList',
   props: ['dvds', 'url'],
   components: {
     Dvd
   }
   /* mounted() {
    *   this.$nextTick(() => {
    *     console.log('this.dvds[0]:', this.dvds[0].getElementsByTagName('title')[0].textContent);
    *   });
    * } */
 }
</script>

<style>
 
</style>
