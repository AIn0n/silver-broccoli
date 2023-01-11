<script setup lang="ts">
import { useRoute, useRouter } from 'vue-router';
const route = useRoute();
const router = useRouter();
const name = route.params.name;
const devices_list = [
  'vacuum cleaner',
  'washing machine',
  'dishwasher',
  'tv'
]
</script>

<template lang="pug">
div(class="row container")
  div(class="col-3 border-end border-secondary me-5")
      h3(class="text-center my-3") Devices
      ul(class="list-group list-group-flush me-1")
        li(class="list-group-item list-group-item-action fs-5" v-for="device in devices_list") {{ device }}
        li(class="list-group-item list-group-item-action list-group-item-primary fs-5") Add new device
  div(class="col text-center")
    h1(class="my-5") {{ name }}
    div(class="alert alert-primary") placeholder for chart
    button(@click="router.push('/')" class="btn btn-outline-secondary position-absolute bottom-0 end-0 mx-5 my-5 fs-4") back
</template>