import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store/index'
import axios from 'axios'

import "bootstrap/dist/css/bootstrap.min.css"
import './assets/main.scss'


const app = createApp(App)

app.use(router)
app.use(store)

const token = localStorage.getItem('token')
if (token) {
        axios.defaults.headers.common['Authorization'] = token
}

app.mount('#app')
