import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [{
        path: '/',
        name: 'UserList',
        component: () =>
            import ('../views/UserList.vue')
    },
    {
        path: '/userinfo',
        name: 'Userinfo',
        component: () =>
            import ('../views/Userinfo.vue')
    }

]

const router = new VueRouter({
    routes
})
export default router