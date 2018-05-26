<template>
  <div class="settings float-right">
    <button class="button" type="button" data-toggle="settings-dropdown">&#x205E;</button>
    <div class="dropdown-pane" id="settings-dropdown" data-dropdown data-auto-focus="true">
      <label for="server-url">Library URL</label>
      <input name="server-url" id="server-url" type="text" value="{{props.localUrl}}" placeholder="http://... " v-on:keyup.enter="onSubmit" />
    </div>
  </div>
</template>

<script> 
 export default {
   name: 'Menu',
   props: [
     localUrl
   ],
   methods: {
     onSubmit(event) {
       console.log('this:', this);  /* eslint-disable-line no-console */

       localStorage.setItem('evergreen_url', event.target.value);
       this.$emit('urlSet', event.target.value);
     }
   }
 }
</script>

<style>
</style>
