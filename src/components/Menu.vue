<template>
  <ul class="dropdown menu" data-dropdown-menu>
    <li><input name="server-url" type="text" value="" placeholder="Server URL" @:input="onInput" /></li>
  </ul>
</template>

<script>
 export default {
   name: 'Menu',
   methods: {
     onInput: (e) => {
       console.log('e.target.value:', e.target.value);
     }
   }
 }
</script>

<style>
</style>
