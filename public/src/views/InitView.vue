<script setup>
import MainTitle from '../components/MainTitle.vue'
import Navigator from '../components/Navigator.vue'
</script>

<template>
  <MainTitle />
  <div class="py-4"></div>
  <Navigator />
  <div class="py-3"></div>
  <RouterView />
</template>
