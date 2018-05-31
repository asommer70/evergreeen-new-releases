<template>
  <div class="settings float-right">
    <button class="button" type="button" data-toggle="settings-dropdown">&#x205E;</button>
    <div class="dropdown-pane" id="settings-dropdown" data-dropdown data-auto-focus="true">
      <label for="server-url">Library URL</label>
      <input name="server-url" id="server-url" type="text" :value="url" placeholder="http://... " v-on:keyup.enter="sendUrl" />

      <label for="library-number">Library Number</label>
      <input name="library-number" id="library-number" type="text" :value="libraryNumber" placeholder="Default is 1..." v-on:keyup.enter="sendLibraryNumber" />
    </div>
  </div>
</template>

<script> 
 export default {
   name: 'Menu',
   
   props: ['url', 'libraryNumber'],
   
   methods: {
     sendUrl(event) {
       console.log('this:', this);  /* eslint-disable-line no-console */

       localStorage.setItem('evergreen_url', event.target.value);
       this.$emit('urlSet', event.target.value);
     },
     
     sendLibraryNumber(event) {
       localStorage.setItem('library_number', event.target.value);
       this.$emit('libraryNumber', event.target.value);
     }
   }
 }
</script>

<style>
</style>
