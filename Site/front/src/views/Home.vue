<script>

export default {
        data() {  
                return {
                        mode: true,
                        form: {
                                username: '',
                                email: '',
                                password: '',
                                repeatPassword: ''
                                
                        },
                        errors: []
                }
        },
        computed:{
                
        }
}
</script>

<template>
        <div class="home">
                <div id="title">Log Profile</div>
                <form>   
                        <input v-if="!mode" type="text" class="form-control" placeholder="Username" aria-label="username"
                                aria-describedby="basic-addon1" v-model="form.username" required>
                        <input type="text" class="form-control" placeholder="Login/Email" aria-label="Login"
                                aria-describedby="basic-addon1" v-model="form.email" required>
                        <input type="password" class="form-control" placeholder="Password" aria-label="Password"
                                aria-describedby="basic-addon1" v-model="form.password" required>
                        <input v-if="!mode" type="password" class="form-control" placeholder=" Repeat Password" aria-label="Password"
                                aria-describedby="basic-addon1" v-model="form.repeatPassword" required>
                        <div v-if="mode" class="d-flex justify-content-between">
                                <div><button type="submit" class="btn btn-outline-light">Log in</button></div>
                                <div><button @click="mode = !mode" type="submit" class="btn btn-outline-light">No account</button></div>
                        </div>
                        <div v-if="!mode"><button v-if="!mode" @click="mode = !mode" type="submit" class="btn btn-outline-light w-100">Registration</button></div>
                </form>  
        </div>
        <div class="d-flex justify-content-center">etc. osht</div>
</template>

<style scoped>
.home {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 97vh;
}
form > input, button{
        margin-bottom: 10px;
        border-width: 3px;
        border-color: rgb(51, 182, 123);
}
#title{
        padding: 0;
        margin-bottom: 10px;
        font-weight: 700;
        font-size: xx-large;
        color: aliceblue;
}
</style>