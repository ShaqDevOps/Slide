<template>
  <Toast />

  <header class="bg-white shadow-md p-4 flex justify-between items-center">
    <div class="menu-left">
      <!-- App Name on the Left -->
      <div class="text-2xl font-bold">
        <span>Slide</span>
      </div>


    </div>
    <!-- Centered Navigation Links -->
    <nav class="menu-center flex space-x-12" v-if="userStore.user.isAuthenticated">
      <a href="#" class="flex flex-col items-center hover:text-blue-500">
        <i class="fas fa-home text-xl"></i>
        <span class="text-sm">Home</span>
      </a>
      <a href="/messages" class="flex flex-col items-center hover:text-blue-500">
        <i class="fas fa-message text-xl"></i>

        <span class="text-sm">Messages</span>
      </a>
      <a href="#" class="flex flex-col items-center hover:text-blue-500">
        <i class="fas fa-bell text-xl"></i>
        <span class="text-sm">Notifications</span>
      </a>
      <a href="/search" class="flex flex-col items-center hover:text-blue-500">
        <i class="fas fa-search text-xl"></i>
        <span class="text-sm">Search</span>
      </a>
    </nav>

    <!-- Profile Picture Placeholder on the Right -->
    <div class="menu-right">
      <template v-if="userStore.user.isAuthenticated">

        <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden">
          <!-- Replace with an image -->
          <img src="./assets/cat.jpg" class="w-full h-full object-cover">
        </div>
      </template>

      <template v-else>
        <a href='/login' class="mr-4 py-4 px-6 bg-gray-600 text-white rounded-lg"> Log In</a>
        <a href='/signup' class="py-4 px-6 bg-purple-600 text-white rounded-lg"> Sign Up</a>

      </template>



    </div>
  </header>

  <main class="px-8 py-6 bg-gray-100">
  </main>



  <RouterView />

</template>

<style scoped></style>


<script>
import axios from "axios";
import { RouterView } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import Toast from "@/components/Toast.vue";
import { useUserStore } from "@/stores/user";

export default {
  components: {
    Toast,
    RouterView,
  },
  setup() {
    const userStore = useUserStore();
    return { userStore };
  },

  beforeCreate() {
    this.userStore.initStore();

    const token = this.userStore.user?.access;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "JWT " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },
};
</script>
