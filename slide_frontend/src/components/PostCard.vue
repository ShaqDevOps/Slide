<template>
    <div class="post-container bg-white rounded-lg shadow-md p-4 w-full">
        <!-- Post Header -->
        <div class="flex items-center space-x-3 mb-4">
            <div class="w-14 h-14 rounded-full bg-gray-300 overflow-hidden">
                <img :src="post.created_by.profile_picture || '/default-avatar.png'" alt="Profile Picture"
                    class="w-full h-full object-cover" />
            </div>
            <p class="text-gray-700 text-lg font-semibold">{{ post.created_by.username }}</p>
        </div>

        <!-- Post Content -->
        <div
            class="w-full bg-gray-100 rounded-lg overflow-hidden flex items-center justify-center aspect-video shadow-inner">
            <p class="text-gray-800 font-extrabold text-xl sm:text-2xl md:text-3xl text-center px-4 py-6">
                {{ post.body }}
            </p>
        </div>

        <!-- Post Interactions -->
        <div class="flex justify-between items-center mt-6">
            <!-- Actions: Like, Comment -->
            <div class="flex space-x-6 items-center">
                <!-- Like Button -->
                <button @click="toggleLike" class="text-gray-600 hover:text-red-500 flex items-center space-x-1">
                    <i :class="['fas', 'fa-heart', { 'text-red-500': post.liked }]"></i>
                    <span>{{ post.likes_count }} Likes</span>
                </button>

                <!-- Comment Button -->
                <button @click="openComments" class="text-gray-600 hover:text-blue-500 flex items-center space-x-1">
                    <i class="fas fa-comment"></i>
                    <span>{{ post.comments_count || 0 }} Comments</span>
                </button>
            </div>

            <!-- Menu Button -->
            <button class="text-gray-600 hover:text-black">
                <i class="fas fa-ellipsis-h"></i>
            </button>
        </div>
    </div>
</template>

<script>
export default {
    name: "PostCard",
    props: {
        post: { type: Object, required: true }, // The entire post object
    },
    methods: {
        toggleLike() {
            this.$emit("likeToggled", this.post.id);
        },
        openComments() {
            this.$emit("commentClicked", this.post.id);
        },
    },
};
</script>

<style scoped>
.post-container {
    width: 100%;
    max-width: 100%;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    /* Soft shadow for box effect */
    border: 1px solid #e2e8f0;
    /* Light gray border for structure */
}

.aspect-video {
    aspect-ratio: 16 / 9;
    /* Makes content look like a big media box */
    background-color: #f7fafc;
}

.text-red-500 {
    color: red;
}

.text-gray-600 {
    color: #4a5568;
}

.text-gray-800 {
    color: #2d3748;
}

button {
    cursor: pointer;
}
</style>
