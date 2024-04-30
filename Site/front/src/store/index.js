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
                                axios.post('http://localhost:8003/login/', user)
                                .then(resp => {
                                        const token = resp.data.token
                                        const user = resp.data.user
                                        localStorage.setItem('token', token)
                                        axios.defaults.headers.common['Authorization'] = token
                                        commit('auth_success', token, user)
                                        alert('auth_success')
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
                                axios.post('http://localhost:8003/logup/', user)
                                .then(resp => {
                                        const token = resp.data.token
                                        const user = resp.data.user
                                        localStorage.setItem('token', token)
                                        axios.defaults.headers.common['Authorization'] = token
                                        commit('auth_success', token, user)
                                        alert('reg_success')
                                        resolve(resp)
                                })
                                .catch(err => {
                                        commit('auth_error', err)
                                        localStorage.removeItem('token')
                                        reject(err)
                                })
                        })
                },
                logout({commit}){
                        return new Promise((resolve, reject) => {
                                
                                localStorage.removeItem('token')
                                axios.post('http://localhost:8003/logout/')
                                .then(resp => {
                                        resolve(resp)
                                })
                                .catch(err => {
                                        // commit('auth_error', err)
                                        console.log(err)
                                        reject(err)
                                })
                                // delete axios.defaults.headers.common['Authorization']
                                // resolve()
                        })
                }
        }
})