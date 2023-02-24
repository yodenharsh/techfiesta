<template>
  <header>
    <h1>Pothole Detection Dashboard</h1>
  </header>
  <EasyDataTable :headers="headers" :items="items" alternating></EasyDataTable>
</template>

<script setup lang="ts">
import { onBeforeMount, ref, type Ref } from "vue";
import type { Header, Item } from "vue3-easy-data-table";
import properties from "./properties";
import EasyDataTable from "vue3-easy-data-table";

const headers: Header[] = [
  { text: "ID", value: "id" },
  { text: "Length", value: "x_len" },
  { text: "Breadth", value: "y_len" },
  { text: "Risk", value: "risk", sortable: true },
  { text: "Confidence", value: "confidence", sortable: true },
];

const items: Ref<Item[] | undefined> = ref([
  { id: 1, x_len: 1, y_len: 2, risk: "HIGH", confidence: 20 },
]);

onBeforeMount(() => {
  anotherFunction();
});

async function anotherFunction() {
  const response = await fetch(properties.url);
  const resObject = await response.json();
  items.value = resObject;
  console.log(items.value);
}
</script>

<style scoped></style>
