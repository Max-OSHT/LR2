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
                                                login: this.formLog.login,
                                                password: this.formLog.password
                                        };
                                        const response = await axios.post('log', data);
                                        console.log(response);
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
                                                password: this.formReg.password,
                                                password_confirm: this.formReg.password_confirm
                                        };
                                        const response = await axios.post('reg', data);
                                        console.log(response);
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
                                login: { required, minLength: minLength(4) },
                                password: { 
                                        required, 
                                        minLength: minLength(8),
                                        containsPasswordRequirement: helpers.withMessage(
                                                () => `The password requires an uppercase, lowercase, number and special character`,
                                                (value) => /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])/.test(value)
                                        ),
                                },
                        },
                        formReg: {
                                username: { required, minLength: minLength(4) },
                                email: { required, email },
                                password: { 
                                        required,
                                        minLength: minLength(8),
                                        containsPasswordRequirement: helpers.withMessage(
                                                () => `The password requires an uppercase, lowercase, number and special character`,
                                                (value) => /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])/.test(value)
                                        ),
                                },
                                password_confirm: { required, sameAsPassword: sameAs(this.formReg.password) }
                        }
                }
        },
        setup: () => ({ v$: useVuelidate() }),
        // validationConfig: {
        //         $error: true
        // }
}
</script>

<template>
        <div class="home">
                <div id="title">Log Profile</div>
                <form @submit.prevent="">

                        <!-- Log in -->
                        <input v-if="mode" type="text" class="form-control" placeholder="Login" v-model.trim="formLog.login">
                        <p v-if="mode && v$.formLog.login.required.$invalid" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="mode && v$.formLog.login.minLength.$invalid" class="error">
                                Должно быть не менее 4 символов
                        </p>

                        <input v-if="mode" type="password" class="form-control" placeholder="Password" v-model.trim="formLog.password">
                        <p v-if="mode && v$.formLog.password.required.$invalid" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="mode && v$.formLog.password.minLength.$invalid" class="error">
                                Должно быть не менее 8 символов
                        </p>
                        <p v-if="mode && v$.formLog.password.containsPasswordRequirement.$invalid" class="error">
                                Пароль должен содержать заглавные, строчные, цифры и специальные символы
                        </p>

                        <!-- Registration -->
                        <input v-if="!mode" type="text" class="form-control" placeholder="Username" v-model.trim="formReg.username"
                                @blur="v$.formReg.username.$touch">
                        <div v-if="!mode && v$.formReg.username.required.$invalid" class="error">
                                Обязательное поле
                        </div>
                        <p v-if="!mode && v$.formReg.username.minLength.$invalid" class="error">
                                Должно быть не менее 4 символов
                        </p>

                        <input v-if="!mode" type="text" class="form-control" placeholder="Email" v-model.trim="formReg.email">
                        <p v-if="!mode && v$.formReg.email.required.$invalid" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="!mode && v$.formReg.email.email.$invalid" class="error">
                                Не корректная почта
                        </p>

                        <input v-if="!mode" type="password" class="form-control" placeholder="Password" v-model.trim="formReg.password">
                        <p v-if="!mode && v$.formReg.password.required.$invalid" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="!mode && v$.formReg.password.minLength.$invalid" class="error">
                                Должно быть не менее 8 символов
                        </p>
                        <p v-if="!mode && v$.formReg.password.containsPasswordRequirement.$invalid" class="error">
                                Пароль должен содержать заглавные, строчные, цифры и специальные символы
                        </p>

                        <input v-if="!mode" type="password" class="form-control" placeholder="Confirm Password" v-model.trim="formReg.password_confirm">
                        <p v-if="!mode && v$.formReg.password_confirm.required.$invalid" class="error">
                                Обязательное поле
                        </p>
                        <p v-if="!mode && v$.formReg.password_confirm.sameAsPassword.$invalid" class="error">
                                Пароли не совпадают
                        </p>

                        <div v-if="mode" class="d-flex justify-content-between">
                                <div><button type="submit" class="btn btn-outline-light" @click="handleSubmit(mode)">Log
                                                in</button></div>
                                <div><button @click="mode = !mode" type="submit" class="btn btn-outline-light">No
                                                account</button></div>
                        </div>
                        <div v-if="!mode"><button type="submit" class="btn btn-outline-light w-100"
                                        @click="handleSubmit(mode), mode = !mode">Registration</button></div>
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
        font-size: small;
        color: salmon;
}

</style>