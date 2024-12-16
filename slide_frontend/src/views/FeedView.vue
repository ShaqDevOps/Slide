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
        <button :class="{ 'text-purple-600 border-purple-600 border-b-4': activeTab === 'all' }"
          class="text-gray-600 px-4 pb-2 focus:outline-none" @click="fetchAllPosts">
          All Posts
        </button>
        <button :class="{ 'text-purple-600 border-purple-600 border-b-4': activeTab === 'friends' }"
          class="text-gray-600 px-4 pb-2 focus:outline-none" @click="fetchFriendsPosts">
          Friends Posts
        </button>
      </div>

      <!-- Posts Section -->
      <PostCard v-for="post in posts" :key="post.id" :post="post" @likeToggled="handleLikeToggle"
        @commentClicked="handleCommentClick" />
    </div>

    <!-- RIGHT COLUMN -->
    <div class="main-right hidden lg:block">
      <Trends />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PostCard from "@/components/PostCard.vue";
import PeopleYouMayKnow from "@/components/PeopleYouMayKnow.vue";
import Trends from "@/components/Trends.vue";

export default {
  components: { PostCard, PeopleYouMayKnow, Trends },
  data() {
    return {
      posts: [],
      activeTab: "all",
    };
  },
  methods: {
    async fetchAllPosts() {
      this.activeTab = "all";
      try {
        const response = await axios.get("/posts/");
        this.posts = response.data;
      } catch (error) {
        console.error("Error fetching posts:", error);
      }
    },
    async fetchFriendsPosts() {
      this.activeTab = "friends";
      try {
        const response = await axios.get("/posts/?user=friends");
        this.posts = response.data;
      } catch (error) {
        console.error("Error fetching friends posts:", error);
      }
    },
    async handleLikeToggle(postId) {
      try {
        const response = await axios.post(`/posts/${postId}/like/`);
        this.posts = this.posts.map((post) =>
          post.id === postId
            ? { ...post, likes_count: response.data.likes_count, liked: response.data.liked }
            : post
        );
      } catch (error) {
        console.error("Error toggling like:", error);
      }
    },
    handleCommentClick(postId) {
      console.log(`Open comments for post: ${postId}`);
      // Implement a modal or redirection for comments here
    },
  },
  mounted() {
    this.fetchAllPosts();
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
</style>
