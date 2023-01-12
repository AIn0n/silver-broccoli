<script setup lang="ts">
import { useRoute } from 'vue-router';
const route = useRoute();
const device = route.params.device;
</script>

<template lang="pug">
p {{ device }}
</template>