import { createRouter, createWebHistory } from 'vue-router'
import store from '@/store'
import Home from '../views/Home.vue'
import InsideLayout from '../views/InsideLayout.vue'
import InsidePage from '../views/InsidePage.vue'
import getLog from '@/components/getLog.vue'
import NotFound from '../views/404.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: Home
    },
    {
      path: '/',
      redirect: { name: 'home' }
    },
    {
      path: '/inside',
      name: 'inside',
      component: InsideLayout,
      meta: { 
        requiresAuth: true
      },
      children: [
        {
          path: 'info',
          name: 'info',
          // component: InsidePage
        },
        {
          path: 'warning',
          name: 'warning',
          // component: InsidePage
        },
        {
          path: 'error',
          name: 'error',
          // component: InsidePage
        },
        {
          path: 'critical',
          name: 'critical',
          component: InsidePage
        },
        {
          path: '*/*',
          redirect: { name: 'inside' }
        }
      ]
    },
    {
      path: '/:catchAll(.*)',
      name: 'notFound',
      component: NotFound
    },
  ]
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('home')
  } else {
    next()
  }
})
export default router
