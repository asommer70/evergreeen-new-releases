<template>
  <div class="settings float-right">
    <button class="button" type="button" data-toggle="settings-dropdown">&#x205E</button>
    <div class="dropdown-pane" id="settings-dropdown" data-dropdown data-auto-focus="true">
      <input name="server-url" type="text" value="" placeholder="Server URL" @:input="onInput" />
    </div>
  </div>
</template>

<script> 
 export default {
   name: 'Menu',
   methods: {
     onInput: (e) => {
       console.warn('e.target.value:', e.target.value);
     }
   }
 }
</script>

<style>
</style>
