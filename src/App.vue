<script setup>
import { ref } from 'vue'

const count = ref(0);

const incrementCount = async () => {
  const response = await fetch(`/api/increment/${count.value}`)
  const text = await response.text()

  count.value = parseInt(text);
};

</script>

<template>
  <div>
    HelloWorld
  </div>
  <div class="card">
    <button type="button" @click="incrementCount">count is {{ count }}</button>
  </div>
</template>

<style scoped>

</style>
