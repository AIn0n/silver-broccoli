<script setup lang="ts">
import { useRoute, useRouter } from "vue-router";
import { ref, onBeforeMount } from "vue";

import BorderList from "@/components/BorderList.vue";
import api from "@/utilities/axios_config";

const route = useRoute();
const router = useRouter();
const name = route.params.name;
const devices = ref([]);

onBeforeMount(() => {
  api
    .get("/" + name + "/device")
    .then((res) => (devices.value = res.data))
    .catch((e) => router.back());
});
</script>

<template lang="pug">
div(class="row container")
  BorderList(title="Devices")
    li(@click="router.push('/edit-device/' + device.name)" class="list-group-item list-group-item-action fs-5" v-for="device in devices") {{ device.name }}
    li(@click="router.push('/' + name + '/add-device')" class="list-group-item list-group-item-action list-group-item-primary fs-5") Add new device
  div(class="col text-center")
    h1(class="my-5") {{ name }}
    div(class="alert alert-primary") placeholder for chart
    button(@click="router.push('/')" class="btn btn-outline-secondary position-absolute top-0 end-0 mx-5 my-5 fs-4") back
</template>
