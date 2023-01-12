<script setup lang="ts">
import { useRouter } from "vue-router";
import IconAndSpan from "@/components/IconAndSpan.vue";
const router = useRouter();
const energy_classes = ["A++", "A+", "B", "C"];
const device_types = ["default", "solar", "accumulator"];
</script>

<template lang="pug">
div(class="container w-50 text-center")
  h1(class="my-5") Add new device
  div(class="alert alert-danger d-flex justify-content-between") example of warning message
    button(type="button" class="btn-close" aria-label="Close")
  IconAndSpan(icon="fa-house-laptop" text="Device name")
  input(class="form-control form-control-lg" type="text" placeholder="new device's name")
  IconAndSpan(icon="fa-lightbulb" text="type")
  select(class="form-select form-select-lg")
    option(v-for="device_type in device_types") {{ device_type }}
  IconAndSpan(icon="fa-plug" text="energy class")
  select(class="form-select form-select-lg")
    option(v-for="cls in energy_classes") {{ cls }}
  IconAndSpan(icon="fa-bolt" text="energy drain")
  div(class="input-group")
    input(type="text" class="form-control form-control-lg" placeholder="energy drain in kWh")
    span(class="input-group-text") kWh
  div(class="d-flex justify-content-between mt-5")
    button(class="btn btn-lg btn-primary") Create 
    button(@click="router.back()" class="btn btn-lg btn-outline-secondary") Back 
</template>
