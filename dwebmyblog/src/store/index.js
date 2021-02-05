import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
    //vuex使用
export default new Vuex.Store({
    state: {
        userinfo: {}
    },
    mutations: {
        editUserinfo(state, user) {
            state.userinfo = user
            console.log(state.userinfo)
        }
    },
    actions: {},
    modules: {}
})