<template>
  <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
    <!-- LEFT COLUMN -->
    <div class="main-left hidden lg:block">
      <PeopleYouMayKnow />
    </div>

    <!-- CENTER COLUMN -->
    <div class="main-center col-span-4 lg:col-span-2 space-y-4">
      <!-- Tabs for switching between All Posts and Friends Posts -->
      <div class="tabs flex justify-center space-x-8 mb-4">
        <button
          :class="{'text-purple-600 border-purple-600 border-b-4': activeTab === 'all'}"
          class="text-gray-600 px-4 pb-2 focus:outline-none"
          @click="fetchAllPosts"
        >
          All Posts
        </button>
        <button
          :class="{'text-purple-600 border-purple-600 border-b-4': activeTab === 'friends'}"
          class="text-gray-600 px-4 pb-2 focus:outline-none"
          @click="fetchFriendsPosts"
        >
          Friends Posts
        </button>
      </div>

      <!-- Post Form -->
      <form @submit.prevent="submitPost" class="bg-white border border-gray-200 text-center rounded-lg p-4">
        <textarea
          v-model="form.body"
          class="p-4 w-full bg-gray-100 rounded-lg"
          placeholder="What's on your mind?"
        ></textarea>
        <div class="flex justify-between items-center mt-4">
          <a href="#" class="inline-block py-4 px-6 bg-gray-600 text-white rounded-lg">Attach Image</a>
          <button type="submit" class="py-4 px-6 bg-purple-600 text-white rounded-lg">Post</button>
        </div>
      </form>

      <!-- Posts Section -->
      <div
  v-for="post in posts"
  :key="post.id"
  class="post-container bg-white rounded-lg shadow-md p-4"
>
  <!-- Post Header -->
  <div class="flex items-center space-x-3 mb-4">
    <div class="w-12 h-12 rounded-full bg-gray-300 overflow-hidden">
      <img
        :src="post.created_by.profile_picture || '/default-avatar.png'"
        alt="Profile Picture"
        class="w-full h-full object-cover"
      />
    </div>
    <p><strong>{{ post.created_by.username }}
      
    </strong></p>
  </div>

  <!-- Post Content -->
  <div
    class="aspect-ratio-1-1 bg-gray-100 rounded-lg overflow-hidden flex items-center justify-center relative shadow-lg"
  >
    <!-- Text Slide -->
    <div class="relative z-0">
      <p class="relative text-white font-extrabold text-lg sm:text-2xl md:text-3xl text-center px-4 py-2">
  {{ post.body }}
</p>

</div>

  </div>


        <!-- Post Actions -->
        <div class="flex justify-between items-center mt-4">
          <div class="flex space-x-4">
            <button @click="toggleLike(post.id)" class="text-gray-600 hover:text-red-500">
              <i class="fas fa-heart"></i> Like
            </button>
            <button class="text-gray-600 hover:text-blue-500">
              <i class="fas fa-comment"></i> Comment
            </button>
          </div>
          <button class="text-gray-600 hover:text-black">
            <i class="fas fa-ellipsis-h"></i>
          </button>
        </div>
      </div>
    </div>

    <!-- RIGHT COLUMN -->
    <div class="main-right hidden lg:block">
      <Trends />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { ref } from "vue";
import PeopleYouMayKnow from "@/components/PeopleYouMayKnow.vue";
import Trends from "@/components/Trends.vue";

export default {
  name: "FeedView",
  components: { PeopleYouMayKnow, Trends },
  data() {
    return {
      form: { body: "" },
      posts: [],
      activeTab: "all", // Track active tab
    };
  },
  methods: {
    async fetchAllPosts() {
      this.activeTab = "all"; // Highlight the 'All Posts' tab
      try {
        const response = await axios.get("/posts/");
        this.posts = response.data;
        console.log(this.posts)
      } catch (error) {
        console.error("Error fetching all posts:", error);
      }
    },
    async fetchFriendsPosts() {
      this.activeTab = "friends"; // Highlight the 'Friends Posts' tab
      try {
        const response = await axios.get("/posts/?user=friends");
        this.posts = response.data;

      } catch (error) {
        console.error("Error fetching friends posts:", error);
      }
    },
    async submitPost() {
      try {
        const response = await axios.post("/posts/", { body: this.form.body });
        this.form.body = ""; // Clear the form
        this.fetchAllPosts(); // Refresh feed
      } catch (error) {
        console.error("Error creating post:", error);
      }
    },
    toggleLike(postId) {
      console.log("Toggled like for post:", postId);
    },
  },
  mounted() {
    this.fetchAllPosts(); // Load all posts by default
  },
};
</script>

<style scoped>
.tabs button {
  border: none;
  background: none;
  font-weight: bold;
  cursor: pointer;
  padding: 8px;
}
.tabs button:focus {
  outline: none;
}
.aspect-ratio-9-16 {
  width: 100%;
  aspect-ratio: 9 / 16;
}
</style>

