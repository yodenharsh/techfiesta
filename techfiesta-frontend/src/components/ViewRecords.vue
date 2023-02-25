<template>
  <div>
    <EasyDataTable
      :headers="headers"
      :items="items"
      alternating
      class="pa-10 ma-4 mx-auto"
      :filter-options="filterOptions"
      :theme-color="theme"
    >
      <template #header-risk="header">
        <div class="filter-column">
          <img
            src="https://www.freeiconspng.com/thumbs/filter-icon/filter-icon-14.png"
            class="filter-icon"
            @click.stop="showRiskFilter = !showRiskFilter"
          />
          {{ header.text }}
          <div class="filter-menu filter-risk-menu" v-if="showRiskFilter">
            <select
              class="favoriteRisk-selector"
              v-model="riskCriteria"
              name="riskCriteria"
            >
              <option value="LOW">LOW</option>
              <option value="MEDIUM">MEDIUM</option>
              <option value="HIGH">HIGH</option>
              <option value="all">All</option>
            </select>
          </div>
        </div>
      </template>
      <template #header-confidence="header">
        <div class="filter-column">
          <img
            src="https://www.freeiconspng.com/thumbs/filter-icon/filter-icon-14.png"
            class="filter-icon"
            @click.stop="showConfidenceFilter = !showConfidenceFilter"
          />
          {{ header.text }}
          <div
            class="filter-menu filter-confidence-menu"
            v-if="showConfidenceFilter"
          >
            <input
              type="range"
              v-model="confidenceCriteria"
              min="0"
              max="100"
            />
          </div>
        </div>
      </template>
    </EasyDataTable>
  </div>
</template>

<script setup lang="ts">
import { computed, onBeforeMount, ref, type Ref } from "vue";
import type { FilterOption, Header, Item } from "vue3-easy-data-table";
import properties from "../properties";
import EasyDataTable from "vue3-easy-data-table";

const headers: Header[] = [
  { text: "ID", value: "id", width: 10 },
  { text: "Length", value: "x_len", width: 30 },
  { text: "Breadth", value: "y_len", width: 30 },
  { text: "Risk", value: "risk", sortable: true, width: 50 },
  { text: "Confidence", value: "confidence", sortable: true, width: 40 },
];

const theme = "#f48225";

const items: Ref<Item[]> = ref([
  { id: 1, x_len: 1, y_len: 2, risk: "HIGH", confidence: 20 },
]);

onBeforeMount(() => {
  anotherFunction();
});

const riskCriteria = ref("all");
const confidenceCriteria = ref(0);

async function anotherFunction() {
  const response = await fetch(properties.url);
  const resObject = await response.json();
  items.value = resObject;
}

const filterOptions = computed((): FilterOption[] => {
  const filterOptionsArray: FilterOption[] = [];
  if (riskCriteria.value != "all") {
    filterOptionsArray.push({
      field: "risk",
      comparison: "=",
      criteria: riskCriteria.value,
    });
  }
  filterOptionsArray.push({
    field: "confidence",
    comparison: ">=",
    criteria: confidenceCriteria.value,
  });
  return filterOptionsArray;
});

const showRiskFilter = ref(false);
const showConfidenceFilter = ref(false);
</script>

<style scoped>
.filter-column {
  display: flex;
  align-items: center;
  justify-items: center;
  position: relative;
}
.filter-icon {
  cursor: pointer;
  display: inline-block;
  width: 15px !important;
  height: 15px !important;
  margin-right: 4px;
}
.filter-menu {
  padding: 15px 30px;
  z-index: 1;
  position: absolute;
  top: 30px;
  width: 200px;
  background-color: #fff;
  border: 1px solid #e0e0e0;
}
.filter-confidence-menu {
  height: 40px;
}
.slider {
  margin-top: 36px;
}
.favoriteRisk-selector {
  width: 100%;
}
</style>
