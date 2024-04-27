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
                                axios.post('http://localhost:8003login/', JSON.stringify(user))
                                .then(resp => {
                                        const token = resp.data.token
                                        const user = resp.data.user
                                        localStorage.setItem('token', token)
                                        axios.defaults.headers.common['Authorization'] = token
                                        commit('auth_success', token, user)
                                        console.log('auth_success')
                                        resolve(resp)
                                })
                                .catch(err => { 
                                        commit('auth_error')
                                        localStorage.removeItem('token')
                                        reject(err)
                                })
                        })
                },
                register({commit}, user){
                        return new Promise((resolve, reject) => {
                                commit('auth_request')
                                axios.post('http://localhost:8003/reg/', user)
                                .then(resp => {
                                        const token = resp.data.token
                                        const user = resp.data.user
                                        localStorage.setItem('token', token)
                                        axios.defaults.headers.common['Authorization'] = token
                                        commit('auth_success', token, user)
                                        console.log('reg_success')
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
                                commit('logout')
                                localStorage.removeItem('token')
                                delete axios.defaults.headers.common['Authorization']
                                resolve()
                        })
                }
        }
})