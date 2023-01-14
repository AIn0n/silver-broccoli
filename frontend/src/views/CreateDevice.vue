<script setup lang="ts">
import { useRouter } from "vue-router";
import { ref, onBeforeMount } from "vue";
// components
import AlertComponent from "@/components/AlertComponent.vue";
import IconAndSpan from "@/components/IconAndSpan.vue";
import api from "@/utilities/axios_config";

const router = useRouter();
let energy_classes: Object;
const device_types = ["default", "solar", "accumulator"];
const error_text = ref("example warning message");

const en_cls = ref(0);

onBeforeMount(() => {
  api
    .get("/energy-class")
    .then((res) => {
      energy_classes = res.data;
      console.log(energy_classes);
    })
    .catch((e) => {
      error_text.value = "cannot get available energy classes: " + e.message;
    });
});
</script>

<template lang="pug">
div(class="container w-50 text-center")
  h1(class="my-5") Add new device
  AlertComponent(:text="error_text" @clear="error_text = ''")
  IconAndSpan(icon="fa-house-laptop" text="Device name")
  input(class="form-control form-control-lg mt-1" type="text" placeholder="new device's name")
  IconAndSpan(icon="fa-lightbulb" text="type")
  select(class="form-select form-select-lg mt-1")
    option(v-for="device_type in device_types") {{ device_type }}
  IconAndSpan(icon="fa-plug" text="energy class")
  select(class="form-select form-select-lg" v-model="en_cls")
    option(v-for="(value, key) in energy_classes" :value="value") {{ key }}
  IconAndSpan(icon="fa-bolt" text="energy drain")
  div(class="input-group mt-1")
    input(type="text" class="form-control form-control-lg" placeholder="energy drain in kWh")
    span(class="input-group-text") kWh
button(@click="router.back()" class="btn btn-outline-secondary position-absolute top-0 end-0 mx-5 my-5 fs-4") back
button(class="btn btn-primary position-absolute top-0 start-0 mx-5 my-5 fs-4") Create
</template>
