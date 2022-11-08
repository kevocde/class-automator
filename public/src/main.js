import { createApp } from "vue";
import { createPinia } from "pinia";
import axios from "axios";

axios.defaults.baseURL = import.meta.env.VITE_BASE_URL;
axios.defaults.headers.common["Content-Type"] = "application/json;charset=utf-8";

import App from "./App.vue";
import router from "./router";

import "./assets/main.scss";

const app = createApp(App);

app.use(createPinia());
app.use(router);

app.mount("#app");
