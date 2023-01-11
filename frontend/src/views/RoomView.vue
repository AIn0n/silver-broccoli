<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
const route = useRoute();
const router = useRouter();
const name = route.params.name;
</script>

<template lang="pug">
div(class="container text-center")
  h1(class="my-5") {{ name }}
  div(class="alert alert-primary") placeholder for chart
button(@click="router.push('/')" class="btn btn-outline-secondary position-absolute bottom-0 end-0 mx-5 my-5 fs-4") back
</template>