<template>
  <div class="header-div">
    <v-container>
      <v-row no gutters>
        <v-col cols="6">
          <header>
            <h2 class="header-text">Pothole Detection Dashboard</h2>
          </header>
        </v-col>
        <v-col cols="6" class="text-right nav-item-container">
          <v-btn variant="tonal" class="nav-item" color="white"
            ><h4>Insert Record</h4></v-btn
          >
          <v-btn variant="tonal" class="nav-item" color="white"
            ><h4>View all Records</h4></v-btn
          >
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<style scoped>
.header-div {
  height: 70px;
  background-color: rgb(3, 37, 140);
}
header {
  color: aliceblue;
  margin-left: 50px;
}

.nav-item {
  display: inline;
  margin-inline: 5% 0;
}
</style>
