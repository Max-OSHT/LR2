import Vuex, { createStore } from 'vuex'
import axios from 'axios'

export default createStore({
        state: {
                status: '',
                token: localStorage.getItem('token') || '',
                user: {},
        },
        getters: {
                isLoggedIn: state => !!state.token,
                authStatus: state => state.status,
        },
        mutations: {
                auth_request(state){
                        state.status = 'loading'
                },
                auth_success(state, token, user){
                        state.status = 'success'
                        state.token = token
                        state.user = user
                },
                auth_error(state){
                        state.status = 'error'
                },
                logout(state){
                        state.status = ''
                        state.token = ''
                },
        },
        actions: {
                login({commit}, user){
                        return new Promise((resolve, reject) => {
                                commit('auth_request')
                                axios.defaults.headers.common['Authorization'] = `null`
                                axios.post('http://localhost:8003/login/', user)
                                .then(resp => {
                                        const token = resp.data.auth_token
                                        localStorage.setItem('token', token)
                                        axios.defaults.headers.common['Authorization'] = token
                                        commit('auth_success', token)
                                        resolve(resp)
                                })
                                .catch(err => { 
                                        commit('auth_error')
                                        alert('Wrong login or password')
                                        localStorage.removeItem('token')
                                        reject(err)
                                })
                        })
                },
                register({commit}, user){
                        return new Promise((resolve, reject) => {
                                commit('auth_request')
                                axios.defaults.headers.common['Authorization'] = `null`
                                axios.post('http://localhost:8003/logup/', user)
                                .then(resp => {
                                        const user = resp.data.username
                                        const id = resp.data.id
                                        commit('auth_success', user, id)
                                        alert('Registration success')
                                        resolve(resp)
                                })
                                .catch(err => {
                                        commit('auth_error', err)
                                        localStorage.removeItem('token')
                                        alert('Registration error')
                                        reject(err)
                                })
                        })
                },
                logout({commit}){
                        return new Promise((resolve, reject) => {
                                axios.defaults.headers.common['Authorization'] = "Token " + localStorage.getItem('token')
                                axios.post('http://localhost:8003/logout/')
                                .then(resp => {
                                        resolve(resp)
                                })
                                .catch(err => {
                                        console.log(err)
                                        reject(err)
                                })
                                localStorage.removeItem('token')
                        })
                },
        }
})