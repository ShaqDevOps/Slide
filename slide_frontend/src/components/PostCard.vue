<template>
    <div class="post-container bg-white rounded-lg shadow-md p-4 w-full">
        <!-- Post Header -->
        <div class="flex items-center space-x-3 mb-4">
            <!-- Profile Picture Linked to Profile -->
            <router-link :to="{ name: 'profile', params: { id: post.created_by?.id } }"
                class="w-14 h-14 rounded-full bg-gray-300 overflow-hidden">
                <img :src="post.created_by?.profile_picture || '/default-avatar.png'" alt="Profile Picture"
                    class="w-full h-full object-cover" />
            </router-link>

            <!-- Username -->
            <p class="text-gray-800 font-semibold">{{ post.created_by?.username || 'Anonymous' }}</p>
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
                    <span>{{ post.likes_count }}</span>
                </button>

                <!-- Comment Button -->
                <router-link :to="{ name: 'post-detail', params: { id: post.id } }"
                    class="text-gray-600 hover:text-blue-500 flex items-center space-x-1">
                    <i class="fas fa-comment"></i>
                    <span>{{ post.comments_count || 0 }}</span>
                </router-link>
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
    },
};
</script>

<style scoped>
.post-container {
    width: 100%;
    max-width: 100%;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    border: 1px solid #e2e8f0;
}

.aspect-video {
    aspect-ratio: 16 / 9;
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
