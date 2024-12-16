<template>
    <div v-if="loading" class="text-center mt-8">

    </div>

    <div v-else class="max-w-4xl mx-auto mt-8 p-6 bg-white shadow-lg rounded-lg">
        <!-- PostCard Component -->
        <PostCard v-if="post.id" :post="post" @likeToggled="toggleLike" />

        <!-- Comments Section -->
        <div class="mt-8">
            <h3 class="text-lg font-semibold mb-4">Comments</h3>

            <!-- Comment List -->
            <div v-if="post.comments && post.comments.length > 0" class="space-y-4">
                <div v-for="comment in post.comments" :key="comment.id"
                    class="flex items-start space-x-4 p-4 bg-gray-100 rounded-lg shadow">
                    <!-- Comment Avatar Linked to Profile -->
                    <router-link :to="{ name: 'profile', params: { id: comment.created_by?.id } }"
                        class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden">
                        <img :src="comment.created_by?.profile_picture || '/default-avatar.png'" alt="Profile Picture"
                            class="w-full h-full object-cover" />
                    </router-link>

                    <!-- Comment Content -->
                    <div>
                        <p class="text-gray-800 font-semibold">{{ comment.created_by?.name || 'Anonymous' }}</p>
                        <p class="text-gray-600 text-sm">{{ comment.body }}</p>
                        <p class="text-xs text-gray-500 mt-1">{{ comment.created_at }}</p>
                    </div>
                </div>
            </div>
            <p v-else class="text-gray-500">No comments yet. Be the first to comment!</p>

            <!-- Comment Form -->
            <form @submit.prevent="submitComment" class="mt-6">
                <textarea v-model="commentBody" placeholder="Write a comment..."
                    class="w-full p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"></textarea>
                <button type="submit"
                    class="mt-2 py-2 px-4 bg-blue-500 text-white rounded-lg hover:bg-blue-600 transition duration-200">
                    Post Comment
                </button>
            </form>
        </div>

    </div>
</template>

<script>
import axios from "axios";
import PostCard from "@/components/PostCard.vue";

export default {
    name: "PostDetail",
    components: {
        PostCard,
    },
    data() {
        return {
            post: {}, // Default post data
            commentBody: "", // New comment input
            loading: true, // Loading state
        };
    },
    methods: {
        async fetchPost() {
            try {
                const postId = this.$route.params.id;
                const response = await axios.get(`/posts/${postId}/`);
                this.post = response.data;
            } catch (error) {
                console.error("Error fetching post details:", error);
            } finally {
                this.loading = false; // End loading
            }
        },
        async toggleLike() {
            try {
                const postId = this.post.id;
                const response = await axios.post(`/posts/${postId}/like/`);
                this.post.likes_count = response.data.likes_count;
                this.post.liked = response.data.liked;
            } catch (error) {
                console.error("Error toggling like:", error);
            }
        },
        async submitComment() {
            try {
                const postId = this.post.id;
                const response = await axios.post(`/posts/${postId}/comment/`, {
                    body: this.commentBody,
                });

                // Append the new comment to the list
                this.post.comments.push(response.data.comment);
                this.post.comments_count = response.data.comments_count;

                // Clear the input field
                this.commentBody = "";
            } catch (error) {
                console.error("Error posting comment:", error);
            }
        },
    },
    mounted() {
        this.fetchPost();
    },
};
</script>

<style scoped>
.text-red-500 {
    color: red;
}
</style>