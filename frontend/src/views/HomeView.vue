<script setup lang="ts">
import { useRouter } from 'vue-router';
const router = useRouter();
const room_names: string[] = [
  "bedroom",
  "bedroom 2",
  "kitchen",
  "toilet",
  "roof",
];
const highest_consumption_devices = [
  {
    name: "TV",
    energy_class: "C",
    energy_drain: 300,
    room: "kitchen",
  },
  {
    name: "Vacuum cleaner",
    energy_class: "D--",
    energy_drain: 250,
    room: "bedroom",
  },
  {
    name: "Blender",
    energy_class: "E",
    energy_drain: 250,
    room: "kitchen",
  },
];
</script>

<template lang="pug">
div(class="row container")
  div(class="col-3 border-end border-secondary me-5")
    h3(class="text-center my-3") Rooms
    ul(class="list-group list-group-flush me-1")
      li(class="list-group-item list-group-item-action d-flex justify-content-between"
      v-for="name in room_names" @click="router.push('/room/' + name)")
        span(class="fs-4") {{ name }}
        button(class="btn btn-danger") Delete
      li(class="list-group-item list-group-item-action d-flex justify-content-between")
        div(class="input-group")
          input(type="text" class="form-control fs-5" placeholder="new room name")
          button(class="btn btn-outline-primary fs-5") Add
  div(class="col text-center")
    h1(class="my-5") hello User!
    div(class="alert alert-danger d-flex justify-content-between") example of warning message
      button(type="button" class="btn-close" aria-label="Close")
    div(class="row my-5")
      div(class="col-6 alert alert-danger") placeholder for chart
      div(class="list-group col mx-5")
        div(class="list-group-item d-flex justify-content-between fs-4")
          p energy cost
          p 40 zl
        div(class="list-group-item d-flex justify-content-between fs-4")
          p estimated month bill
          p 30 zl 
    div(class="row my-5")
      div(class="col mx-3")
        label(class="form label") price before limit
        input(class="form-control form-control-sm" type="number")
      div(class="col mx-3")
        label(class="form label") price after limit
        input(class="form-control form-control-sm" type="number")
      button(class="btn btn-primary col fs-5 mx-3") refresh price
    h2 highest consumption devices
    div(class="row my-5")
      div(class="card col mx-3" v-for="device in highest_consumption_devices")
        div(class="card-body")
          h5(class="card-title") {{device.name}}
          h6(class="card-subtitle mb-2 text-muted") {{  device.room }}
        ul(class="list-group list-group-flush")
          li(class="list-group-item fs-5") energy drain = {{ device.energy_drain }} kWh 
          li(class="list-group-item fs-5") energy class {{ device.energy_class }}
</template>
