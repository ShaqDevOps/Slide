<template>
    <div class="max-w-7xl mx-auto grid grid-cols-2 gap-4">
        <div class="main-left">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <h1 class="mb-6 text-2xl">Log In</h1>
                <p class="mb-6 text-gray-500">
                    Test Test Test Test Test Test Test Test Test Test Test Test Test Test
                </p>
                <p class="font-bold">
                    Don't have an account? <a href="/signup" class="underline">Click here</a> to create one!
                </p>
            </div>
        </div>

        <div class="main-right">
            <div class="p-12 bg-white border border-gray-200 rounded-lg">
                <form class="space-y-6" @submit.prevent="submitForm">
                    <div>
                        <label>Username</label><br />
                        <input type="username" v-model="form.username" placeholder="Your username"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
                    </div>
                    <div>
                        <label>Password</label><br />
                        <input type="password" v-model="form.password" placeholder="Your password"
                            class="w-full mt-2 py-4 px-6 border border-gray-200 rounded-lg" />
                    </div>

                    <template v-if="errors.length">
                        <div class="bg-red-300 text-white rounded-lg p-6">
                            <p v-for="error in errors" :key="error">{{ error }}</p>
                        </div>
                    </template>
                    <div>
                        <button type="submit" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Log In</button>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from "axios";
import { useUserStore } from "@/stores/user";

export default {
    setup() {
        const userStore = useUserStore();
        return { userStore };
    },

    data() {
        return {
            form: {
                username: "",
                password: ""
            },
            errors: []
        };
    },

    methods: {
        async submitForm() {
            this.errors = [];

            // Validate input
            if (this.form.username === "") {
                this.errors.push("Please enter your username.");
            }
            if (this.form.password === "") {
                this.errors.push("Password is required.");
            }

            // Only proceed if no errors
            if (this.errors.length === 0) {
                try {
                    // Send login request
                    const payload = {
                        username: this.form.username,
                        password: this.form.password
                    };

                    const response = await axios.post("auth/jwt/create", payload);

                    if (response.status === 200) {
                        // Save tokens
                        this.userStore.setToken(response.data);
                        axios.defaults.headers.common["Authorization"] = "JWT " + response.data.access;

                        // Fetch user info
                        const userResponse = await axios.get("/me");
                        this.userStore.setUserInfo(userResponse.data);

                        // Redirect to feed
                        this.$router.push("/feed");
                    } else {
                        this.errors.push("Something went wrong. Please try again.");
                    }
                } catch (error) {
                    if (error.response) {
                        // Handle server-side validation errors
                        const errorMessages = Object.values(error.response.data)
                            .flat()
                            .filter((msg) => typeof msg === "string");
                        this.errors.push(...errorMessages);
                    } else {
                        this.errors.push("A network error occurred. Please try again.");
                    }
                }
            }
        }
    }
};
</script>
