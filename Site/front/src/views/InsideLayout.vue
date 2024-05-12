<script>
    import Header from './../components/Header.vue'
    import Log from './../components/getLog.vue'
    export default {
        components: {Header, Log}, 
    }
</script>

<template>
    <Header/>
    <Log/>
    <RouterView/>
</template>
      
