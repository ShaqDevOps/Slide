<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <!-- LEFT COLUMN -->
        <div class="main-left col-span-1">
            <div class="p-6 bg-white border border-gray-200 text-center rounded-lg shadow-md">
                <!-- Profile Picture -->
                <div class="w-24 h-24 mx-auto rounded-full overflow-hidden border-2 border-gray-300">
                    <img :src="userStore.user.profile_picture || '../assets/cat.jpg'" alt="Profile Picture"
                        class="w-full h-full object-cover">
                </div>

                <!-- Username -->
                <div class="mt-4">
                    <p class="text-lg font-semibold">{{ profile.username }}</p>
                </div>

                <!-- Followers and Posts -->
                <div class="mt-4 flex justify-around text-gray-500">
                    <RouterLink :to="{ name: 'friends', params: { id: $route.params.id } }" class="text-sm">
                        <strong>{{ profile.friends_count }}</strong>
                        friends
                    </RouterLink>
                    <p class="text-sm">
                        <strong>{{ posts.length }}</strong> posts
                    </p>
                </div>
                <div v-if="isNotFriend">

                    <div class="mt-6" v-if="isNotOwnProfile">
                        <button class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"
                            @click="sendFriendRequest">Add Friend</button>
                    </div>

                </div>
                <div class="mt-6" v-if="isOwnProfile">
                    <button class="inline-block py-4 px-6 bg-red-600 text-white rounded-lg"
                        @click="logout">Logout</button>
                </div>

            </div>
        </div>

        <!-- CENTER COLUMN -->
        <div class="main-center col-span-2 space-y-4">
            <div class="bg-white border border-gray-200 text-center rounded-lg">
                <form @submit.prevent="submitPost" class="space-y-6">
                    <!-- Textarea for the post content -->
                    <div class="p-4">
                        <textarea v-model="form.body" class="p-4 w-full bg-gray-100 rounded-lg"
                            placeholder="What's on your mind?"></textarea>
                    </div>

                    <!-- Buttons and other actions -->
                    <div class="p-4 border-t border-gray-100 flex justify-between">
                        <!-- Attach Image Button -->
                        <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">
                            Attach Image
                        </a>

                        <!-- Submit Button -->
                        <div>
                            <button type="submit"
                                class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
                        </div>
                    </div>
                </form>

                <div class="p-4 bg-white border border-gray-200 text-center rounded-lg" v-for="post in posts"
                    :key="post.id">
                    <div class="mb-6 flex items-center justify-between">
                        <div class="flex items-center space-x-3">
                            <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden">
                                <img :src="post.created_by.profile_picture" alt="Profile Picture"
                                    class="mb-6 rounded-full w-full h-full object-cover">
                            </div>
                            <p><strong>{{ post.created_by.username }}</strong></p>
                        </div>
                        <p class="text-gray-600">{{ post.created_at_formatted }}</p>
                    </div>

                    <p>{{ post.body }}</p>

                    <div class="my-6 flex items-center justify-between">
                        <!-- Like Button -->
                        <div class="flex items-center space-x-6">
                            <div class="flex items-center space-x-1 cursor-pointer" @click="toggleLike(post.id)">
                                <svg xmlns="http://www.w3.org/2000/svg" fill="currentColor" viewBox="0 0 24 24"
                                    :class="liked ? 'text-red-500' : 'text-gray-500'"
                                    class="w-5 h-5 transition-colors duration-200 ease-in-out">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                        d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z" />
                                </svg>
                                <span class="text-gray-500 text-xs">{{ liked ? 1 : 0 }} likes</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- RIGHT COLUMN -->
        <div class="main-right col-span-1 space-y-4">
            <PeopleYouMayKnow />
            <Trends />
        </div>
    </div>
</template>

<script>
import axios from 'axios';
import { ref } from 'vue';
import PeopleYouMayKnow from '@/components/PeopleYouMayKnow.vue';
import Trends from '@/components/Trends.vue';
import { useUserStore } from "@/stores/user";
import { useToastStore } from '@/stores/toast';

export default {
    name: 'FeedView',
    components: {
        PeopleYouMayKnow,
        Trends,
    },
    setup() {
        const userStore = useUserStore();
        const toastStore = useToastStore();


        return {
            userStore,
            toastStore
        };

    },
    data() {
        return {

            form: {
                body: "",
            },

            profile: '',
            posts: [],
            liked: false, // like functionality
            showMenu: false, // dropdown menu on posts
            errors: [], // error handling
        };
    },
    mounted() {


        const userIdFromUrl = this.$route.params.id; //store the id passed by vue Router
        this.fetchPosts(userIdFromUrl);

        this.getProfile(userIdFromUrl)


    },

    computed: {
        loggedInUserId() {
            // Retrieve the logged-in user's ID from localStorage or Vuex store
            return localStorage.getItem('user.id') || this.$store.state.UserStore.id;
        },
        isNotOwnProfile() {
            // Determine if the current profile is not the logged-in user's profile
            return this.profile && this.profile.id !== this.loggedInUserId;
        },

        isOwnProfile() {
            return this.profile && this.profile.id === this.loggedInUserId;
        },
        isNotFriend() {
            return (
                this.profile &&
                !this.profile.friends.some((friend) => friend.id === this.loggedInUserId)
            );
        },

    },
    methods: {




        async fetchPosts(userId) {
            try {
                const loggedInUserId = this.userStore.user.id

                if (userId === loggedInUserId) {

                    await this.getMyPosts();
                } else {

                    await this.getUserPosts(userId);

                }

            } catch (error) {
                console.error("Error determining which posts fetch", error);
            }

        },

        async getUserPosts(userId) {
            try {


                const response = await axios.get(`/posts/?user=${userId}`);
                this.posts = response.data;
                console.log(this.posts)
            } catch (error) {
                console.error('Error fetching posts: ', error);
            }
        },





        async getMyPosts() {
            try {
                const response = await axios.get('/posts/?user=me'); // Backend filters for user posts
                this.posts = response.data;
                console.log(this.posts)
            } catch (error) {
                console.error('Error fetching posts:', error);
            }
        },


        async getProfile(userId) {

            try {
                const response = await axios.get(`profiles/${userId}`)
                console.log(response.data)
                this.profile = response.data
                console.log(this.profile)
            } catch (error) {
                console.error('Error fetching profile: ', error)
            }
        },




        async submitPost() {
            this.errors = []; // Clear errors before submitting
            try {
                const payload = {
                    body: this.form.body,
                };
                const response = await axios.post('/posts/', payload); // Send new post
                this.getMyPosts(); // Refresh posts after submission
                this.form.body = ""; // Clear form
            } catch (error) {
                if (error.response) {
                    this.errors.push(error.response.data);
                } else {
                    console.error('Error submitting post:', error);
                }
            }
        },



        async logout() {
            this.errors = []
            try {
                const response = await axios.post('/logout/');
                console.log(response.data)
                this.userStore.removeToken()
                this.$router.push('/login/')
            } catch (error) {
                if (error.response) {
                    this.errors.push(error.response.data)
                }
            }


        },

        toggleLike(postId) {
            // Logic for toggling like status
            this.liked = !this.liked;
            console.log(`Toggled like for post ID: ${postId}`);
        },
        toggleMenu() {
            this.showMenu = !this.showMenu;
        },


        sendFriendRequest() {
            axios.post(`profiles/${this.$route.params.id}/friends/request/send/`).then(response => {
                console.log('data', response.data)


                if (response.data.message == 'Request already sent') {
                    this.toastStore.showToast(5000, 'The request has already been sent', 'bg-red-300');
                }
                else {
                    this.toastStore.showToast(5000, 'Friend request was sent', 'bg-green-300');


                }
            }).catch(error => {
                console.log('error', error)


            })
        }

    },




};



</script>
