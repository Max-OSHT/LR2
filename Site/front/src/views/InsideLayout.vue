<script>
    import Header from './../components/Header.vue'
    export default {
        components: { Header}, 
    }
</script>

<template>
    <Header/>
    <h2>Полученные логи</h2>
    <RouterView/>
</template>
      
