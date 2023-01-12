<script setup lang="ts">
import { useRoute } from 'vue-router';
const route = useRoute();
const device = route.params.device;
const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
const timestamps = [
  {
    weekdays: ["Monday", "Saturday"],
    start_hour: 12,
    start_minute: 30,
    end_hour: 13,
    end_minute: 0
  },
  {
    weekdays: ["Sunday"],
    start_hour: 12,
    start_minute: 30,
    end_hour: 13,
    end_minute: 0
  },
  {
    weekdays: ["Monday", "Tuesday"],
    start_hour: 13,
    start_minute: 45,
    end_hour: 20,
    end_minute: 30
  }
]
</script>

<template lang="pug">
div(class="container text-center")
  h1(class="my-5") Edit {{ device }}
  div(class="card mx-5")
    div(class="list-group list-group-flush")
      div(class="list-group-item d-flex justify-content-between")
        div(class="input-group input-group-sm w-50 mx-3 my-3")
          span(class="input-group-text") start
          input(type="number" class="form-control")
          span(class="input-group-text") H
          input(type="number" class="form-control")
          span(class="input-group-text") M
        div(class="input-group input-group-sm w-50 mx-3 my-3")
          span(class="input-group-text") end
          input(type="number" class="form-control")
          span(class="input-group-text") H
          input(type="number" class="form-control")
          span(class="input-group-text") M
      div(class="list-group-item")
        div(class="form-check form-check-inline mx-4" v-for="day in days")
          input(class="form-check-input" type="checkbox")
          label(class="form-check-label") {{ day }}
</template>