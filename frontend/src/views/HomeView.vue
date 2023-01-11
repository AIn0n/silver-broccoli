<script setup lang="ts">
  const room_names: string[] = [
    'bedroom',
    'bedroom 2', 
    'kitchen',
    'toilet',
    'roof'
  ]
</script>

<template lang="pug">
div(class="row container")
  ul(class="list-group col-3 me-5")
    li(class="list-group-item d-flex justify-content-between" v-for="name in room_names")
      span {{ name }}
      button(class="btn btn-danger") Delete
  div(class="col text-center")
    h1(class="my-5") hello User!
    div(class="alert alert-danger") hello world
    div(class="row my-5")
      div(class="col-6 alert alert-danger") placeholder for chart
      div(class="col")
        p energy cost = 41 zl 
        p estimated month bill 30 zl 
    div(class="row my-5")
      div(class="col")
        label(class="form label") price before limit
        input(class="form-control form-control-sm" type="number")
      div(class="col")
        label(class="form label") price after limit
        input(class="form-control form-control-sm" type="number")
      button(class="btn btn-primary col") refresh price
</template>
