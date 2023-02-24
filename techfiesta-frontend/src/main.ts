import { createApp } from 'vue'
import App from './App.vue'
import Vue3EasyDataTable from 'vue3-easy-data-table'
import 'vue3-easy-data-table/dist/style.css'


const app = createApp(App);
app.component(Vue3EasyDataTable)

app.mount("#app")
