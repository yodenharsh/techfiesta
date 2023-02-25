<template>
  <TheHeader></TheHeader>
  <v-parallax src="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg">
    <v-card
      class="d-flex align-center justify-center flex-wrap text-center mx-auto mt-15"
      elevation="4"
      rounded
      max-width="600"
      width="100%"
      theme="light"
    >
      <component :is="component"></component>
    </v-card>
  </v-parallax>
</template>

<script setup lang="ts">
import { markRaw } from "vue";
import TheHeader from "./components/TheHeader.vue";
import ViewRecords from "./components/ViewRecords.vue";

const component = markRaw(ViewRecords);
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
