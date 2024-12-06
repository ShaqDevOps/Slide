<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
        <!-- LEFT COLUMN -->
        <div class="main-left col-span-1">
</div>
      
        <!-- CENTER COLUMN -->
        <div class="main-center col-span-2 space-y-4">

   


        <!-- Friend Requests -->
<div v-for="request in requests" v-bind:key="request.id">
    <div class="p-3 bg-white border border-gray-200 text-center rounded-lg shadow-md max-w-sm mx-auto">
        <!-- Profile Picture -->
        <div class="w-16 h-16 mx-auto rounded-full overflow-hidden border-2 border-gray-300">
            <img :src="userStore.user.profile_picture || '../assets/cat.jpg'" alt="Profile Picture"
                class="w-full h-full object-cover">
        </div>
        <strong>
            <p>{{ request.sender.username }}</p>
        </strong>

        <div class="mt-4 flex space-x-4 justify-around">
            <p class="text-xs text-gray-500">{{ request.receiver.friends_count }} friends</p>
            <p class="text-xs text-gray-500">120 Posts</p>
        </div>

        <div class="mt-4 flex justify-center space-x-4">
            <button class="py-2 px-4 bg-purple-600 text-white rounded-lg"
                @click="sendRequestResponse('accept', request.id)">Accept</button>
            <button class="py-2 px-4 bg-red-600 text-white rounded-lg"
                @click="sendRequestResponse('reject', request.id)">Ignore</button>
        </div>
    </div>
</div>

<!-- Friends -->
<div v-for="friend in friends" v-bind:key="friend.id">
    <div class="p-3 bg-white border border-gray-200 text-center rounded-lg shadow-md max-w-sm mx-auto">
        <!-- Profile Picture -->
        <div class="w-16 h-16 mx-auto rounded-full overflow-hidden border-2 border-gray-300">
            <RouterLink :to="{ name: 'profile', params: { id: friend.id } }">
                <img src="../assets/cat.jpg" alt="Profile Picture" class="w-full h-full object-cover">
            </RouterLink>
        </div>
        <strong>
            <RouterLink :to="{ name: 'profile', params: { id: friend.id } }">
                <p>{{ friend.username }}</p>
            </RouterLink>
        </strong>

        <div class="mt-4 flex space-x-4 justify-around">
            <p class="text-xs text-gray-500">{{friend.friends_count}}  </p>
            <p class="text-xs text-gray-500">120 Posts</p>
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




export default {
    name: 'FriendsView',
    components: {
        PeopleYouMayKnow,
        Trends,
    },
    setup() {
        const userStore = useUserStore();
        
        return { userStore };
    },

    data() {
        return {
            requests: [],
            friends: []

        }
    },


    mounted() {


        const userIdFromUrl = this.$route.params.id; //store the id passed by vue Router


        this.getFriends(userIdFromUrl)


    },
    methods: {




        async getFriends(userId) {

            try {
                const response = await axios.get(`profiles/${userId}/friends`)
                this.friends = response.data.friends
                this.requests = response.data.requests
                console.log(response.data)
            } catch (error) {
                console.error('Error fetching profile: ', error)
            }
        },




        async sendFriendRequest() {
            axios.post(`profiles/${this.$route.params.id}/friends/request/send/`).then(response => {
                console.log('data', response.data)
            }).catch(error => {
                console.log('error', error)


            })
        },



        async sendRequestResponse(request_status, requestId) {
            axios.patch(`profiles/friends/request/response/`, { id: requestId, request_status }).then(response => {
                console.log('data', response.data)
            }).catch(error => {
                console.log('error', error)
            })

        },


    }

};



</script>
