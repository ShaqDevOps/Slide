<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">


            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl"> Sign Up </h1>
                <p class="mb-6 text-gray-500">TestTestTestTestTestTestTestTestTestTest\TestTest
                    TestTestTestTestTestTestTestTestTes
                    tTestTestTestTestTestTest
                </p>
                <p class="font-bold">
                    Already have an account? <a href="/login" class="underline"> Click here</a> to log in!
                </p>
            </div>


        </div>

        <div class="main-right">


            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" v-on:submit.prevent="submitForm">
                    <div>
                        <label>Name </label><br>
                        <input type="name" v-model="form.name" placeholder="Your full name"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Username</label><br>
                        <input type="username" v-model="form.username" placeholder="Name of your page"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>E-mail</label><br>
                        <input type="email" v-model="form.email" placeholder="Your e-mail address"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Password</label><br>
                        <input type="password" v-model="form.password1" placeholder=" Your password"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>
                    <div>
                        <label>Repeat Password</label><br>
                        <input type="password" v-model="form.password2" placeholder="Repeat your password"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg">
                    </div>

                    <template v-if="errors.length">
                        <div class="bg-red-300 text-white rounded-lg p-6">

                            <p v-for="error in errors" v-bind:key="error"> {{ error }}</p>
                        </div>
                    </template>

                    <div>
                        <button class="py-4 px-6 bg-purple-600 text-white rounded-lg"> Sign Up</button>
                    </div>
                </form>

            </div>


        </div>
    </div>
</template>


<script>
import axios from 'axios'
import { useToastStore } from '@/stores/toast';
export default {
    setup() {

        const toastStore = useToastStore()
        return {
            toastStore
        }
    },
    data() {
        return {
            form: {
                email: '',
                username: '',
                name: '',
                password1: '',
                password2: '',


            },
            errors: [],

        }
    },
    methods: {
        submitForm() {
            this.errors = [];

            // Frontend validation
            if (this.form.name === '') {
                this.errors.push('Your name is missing');
            }
            if (this.form.username === '') {
                this.errors.push('Please enter a username');
            }
            if (this.form.password1 === '') {
                this.errors.push('Please enter a password');
            }
            if (this.form.email === '') {
                this.errors.push('Please enter an email');
            }
            if (this.form.password1 !== this.form.password2) {
                this.errors.push('The passwords do not match');
            }

            if (this.errors.length === 0) {
                // Include username in the payload
                const payload = {
                    name: this.form.name,
                    username: this.form.username,
                    email: this.form.email,
                    password: this.form.password1
                };

                axios.post('/auth/users/', payload)
                    .then(response => {
                        if (response.status === 201) {
                            this.toastStore.showToast(5000, 'The user is registered. Please log in', 'bg-emerald-500');

                            // Reset form
                            this.form.email = '';
                            this.form.name = '';
                            this.form.username = '';
                            this.form.password1 = '';
                            this.form.password2 = '';
                        } else {
                            this.toastStore.showToast(5000, 'Something went wrong. Please try again', 'bg-red-300');
                        }
                    })
                    .catch(error => {
                        if (error.response) {
                            const errorMessages = Object.values(error.response.data)
                                .flat()
                                .filter(msg => typeof msg === 'string');
                            this.errors.push(...errorMessages);
                        } else {
                            this.errors.push('A network error occurred. Please try again.');
                        }
                    });
            }
        }
    }


}



</script>