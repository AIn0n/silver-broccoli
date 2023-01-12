<script setup lang="ts">
import { useRoute } from 'vue-router';
const route = useRoute();
const device = route.params.device;
</script>

<template lang="pug">
div(class="container text-center")
  h1(class="my-5") Edit {{ device }}
</template>