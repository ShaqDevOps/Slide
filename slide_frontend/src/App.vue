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
      <a href="/feed" class="flex flex-col items-center hover:text-blue-500">
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

        <div @click="handleProfileClick">
          <RouterLink :to="{ name: 'profile', params: { id: userStore.user.id } }">
            <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden">

            </div>
          </RouterLink>

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
    // Initialize the store and set the default Authorization header
    this.userStore.initStore();

    const token = this.userStore.user?.access;
    if (token) {
      axios.defaults.headers.common["Authorization"] = "JWT " + token;
    } else {
      axios.defaults.headers.common["Authorization"] = "";
    }
  },

  methods: {
    handleProfileClick() {
      const profileRoute = { name: "profile", params: { id: this.userStore.user.id } };

      if (this.$route.name === "profile" && this.$route.params.id === this.userStore.user.id) {
        // Force a reload of the same route
        this.$router.replace({
          path: '/posts/?user=me'
        }).then(() => {
          this.$router.replace(profileRoute);
        });
      } else {
        // Navigate to the profile route normally
        this.$router.push(profileRoute);
      }
    },
  },
};
</script>
