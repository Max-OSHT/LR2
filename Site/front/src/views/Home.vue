<script>
import axios from 'axios';
import { reactive } from 'vue'
import { useVuelidate } from '@vuelidate/core'
import { helpers, required, minLength, email, sameAs} from '@vuelidate/validators'

export default {
        data() {
                return {
                        mode: true,
                        formLog: {
                                login: '',
                                password: '',
                        },
                        formReg: {
                                username: '',
                                email: '',
                                password: '',
                                password_confirm: '',
                        }
                }
        },
        methods: {
                async handleSubmit(action) {
                        if (action === true) {
                                const result = await this.v$.formLog.$validate()
                                if (result) {
                                        const data = {
                                                username: this.formLog.login,
                                                password: this.formLog.password
                                        };
                                        this.$store.dispatch('login', data)
                                        .then(() => this.$router.push({name:'inside'}))
                                        .catch(err => console.log(err))
                                }
                                else {
                                        console.log("valid not successful")
                                }
                                return
                        }
                        else {
                                const result = await this.v$.formReg.$validate()
                                if (result) {
                                        const data = {
                                                username: this.formReg.username,
                                                email: this.formReg.email,
                                                password: this.formReg.password
                                        };
                                        this.$store.dispatch('register', data)
                                        .then(() => this.$router.push({name:'home'}))
                                        .catch(err => console.log(err))
                                }
                                else {
                                        console.log("valid not successful")
                                }
                        }
                },
        },
        validations() {
                return {
                        formLog: {
                                login: { required, minLength: minLength(3) },
                                password: { 
                                        required, 
                                        minLength: minLength(6),
                                        containsPasswordRequirement: helpers.withMessage(
                                                () => `The password requires an uppercase, lowercase, number and special character`,
                                                (value) => /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])/.test(value)
                                        ),
                                },
                        },
                        formReg: {
                                username: { required, minLength: minLength(3) },
                                email: { required, email },
                                password: { 
                                        required,
                                        minLength: minLength(6),
                                        containsPasswordRequirement: helpers.withMessage(
                                                () => `The password requires an uppercase, lowercase, number and special character`,
                                                (value) => /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])/.test(value)
                                        ),
                                },
                                password_confirm: { required, sameAsPassword: sameAs(this.formReg.password) }
                        }
                }
        },
        setup: () => ({ v$: useVuelidate( ), }),
}
</script>

<template>
        <div class="home">
                <div id="title">Log Profile</div>
                <form  @submit.prevent="">

                        <!-- Log in -->
                        <input v-if="mode" type="text" class="form-control" placeholder="Login" v-model.trim="formLog.login">
                        <p v-if="mode && v$.formLog.login.required.$invalid && v$.formLog.login.$dirty" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="mode && v$.formLog.login.minLength.$invalid" class="error">
                                Должно быть не менее 4 символов
                        </p>

                        <input v-if="mode" type="password" class="form-control" placeholder="Password" v-model.trim="formLog.password">
                        <p v-if="mode && v$.formLog.password.required.$invalid && v$.formLog.password.$dirty" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="mode && v$.formLog.password.minLength.$invalid && v$.formLog.password.$dirty" class="error">
                                Должно быть не менее 8 символов
                        </p>
                        <p v-if="mode && v$.formLog.password.containsPasswordRequirement.$invalid && v$.formLog.password.$dirty" class="error">
                                Пароль должен содержать <br/> заглавные, строчные, цифры и специальные символы
                        </p>

                        <!-- Registration -->
                        <input v-if="!mode" type="text" class="form-control" placeholder="Username" v-model.trim="formReg.username"
                                @blur="v$.formReg.username.$touch" >
                        <div v-if="!mode && v$.formReg.username.required.$invalid && v$.formReg.username.$dirty" class="error">
                                Обязательное поле
                        </div>
                        <p v-if="!mode && v$.formReg.username.minLength.$invalid" class="error">
                                Должно быть не менее 4 символов
                        </p>

                        <input v-if="!mode" type="text" class="form-control" placeholder="Email" v-model.trim="formReg.email">
                        <p v-if="!mode && v$.formReg.email.required.$invalid && v$.formReg.email.$dirty" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="!mode && v$.formReg.email.email.$invalid" class="error">
                                Не корректная почта
                        </p>

                        <input v-if="!mode" type="password" class="form-control" placeholder="Password" v-model.trim="formReg.password">
                        <p v-if="!mode && v$.formReg.password.required.$invalid && v$.formReg.password.$dirty" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="!mode && v$.formReg.password.minLength.$invalid && v$.formReg.password.$dirty" class="error">
                                Должно быть не менее 8 символов
                        </p>
                        <p v-if="!mode && v$.formReg.password.containsPasswordRequirement.$invalid && v$.formReg.password.$dirty" class="error">
                                Пароль должен содержать <br/> заглавные, строчные, цифры и специальные символы
                        </p>

                        <input v-if="!mode" type="password" class="form-control" placeholder="Confirm Password" v-model.trim="formReg.password_confirm">
                        <p v-if="!mode && v$.formReg.password_confirm.required.$invalid && v$.formReg.password_confirm.$dirty" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="!mode && v$.formReg.password_confirm.sameAsPassword.$invalid" class="error">
                                Пароли не совпадают
                        </p>

                        <div v-if="mode" class="d-flex justify-content-between">
                                <div><button type="submit" class="btn btn-outline-light" @click="handleSubmit(mode)">Log in</button></div>
                                <div><button @click="mode = !mode" type="submit" class="btn btn-outline-light">No account</button></div>
                        </div>
                        <div v-if="!mode">
                                <button type="submit" class="btn btn-outline-light w-100" @click="handleSubmit(mode)">Registration</button>
                                <button type="submit" class="btn btn-outline-light w-100" @click="mode = !mode">Back</button>
                        </div>
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

form>input,
button {
        font-weight: 500;
        margin-bottom: 10px;
        border-width: 3px;
        border-color: rgb(51, 182, 123);
}

#title {
        padding: 0;
        margin-bottom: 10px;
        font-weight: 700;
        font-size: xx-large;
        color: aliceblue;
}

.error {
        margin-bottom: 10px;
        font-size: small;
        color: salmon;
}

</style>