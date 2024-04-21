<script>
import axios from 'axios';
export default {
        data() {  
                return {
                        mode: true,
                        login: '',
                        username: '',
                        email: '',
                        password: '',
                        password_confirm: '',
                        errors: []
                }
        },
        methods:{
                async handleSubmit(action){
                        if (action === true) 
                        {
                                const data = {
                                        login: this.username,
                                        login: this.email,
                                        password: this.password
                                };
                                const response = await axios.post('log', data);
                                console.log(response);
                                return
                        }
                        else {
                                const data = {
                                        username: this.username,
                                        email: this.email,
                                        password: this.password,
                                        password_confirm: this.password_confirm
                                };
                                const response = await axios.post('reg', data);
                                console.log(response);
                        }


                },
        }
}
</script>

<template>
        <div class="home">
                <div id="title">Log Profile</div>
                <form @submit.prevent="">   
                        <input v-if="!mode" type="text" class="form-control" placeholder="Username" aria-label="username"
                                aria-describedby="basic-addon1" v-model="username" required>
                        <input type="text" class="form-control" placeholder="Login/Email" aria-label="Login"
                                aria-describedby="basic-addon1" v-model="email" required>
                        <input type="password" class="form-control" placeholder="Password" aria-label="Password"
                                aria-describedby="basic-addon1" v-model="password" required>
                        <input v-if="!mode" type="password" class="form-control" placeholder=" Confirm Password" aria-label="Password"
                                aria-describedby="basic-addon1" v-model="password_confirm" required>
                        <div v-if="mode" class="d-flex justify-content-between">
                                <div><button type="submit" class="btn btn-outline-light" @click="handleSubmit(mode)">Log in</button></div>
                                <div><button @click="mode = !mode" type="submit" class="btn btn-outline-light">No account</button></div>
                        </div>
                        <div v-if="!mode"><button type="submit" class="btn btn-outline-light w-100" @click="handleSubmit(mode), mode = !mode">Registration</button></div>
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