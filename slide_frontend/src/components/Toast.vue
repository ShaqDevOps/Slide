<script setup>
import { useToastStore } from '@/stores/toast';

const store = useToastStore();
</script>

<template>
    <div v-if="store.isVisible" :class="['px-6 py-6 fixed top-full right-8 rounded-xl shadow-xl', store.classes]"
        class="transition ease-in-out duration-500 transform">

        {{ store.message }}
    </div>
</template>
