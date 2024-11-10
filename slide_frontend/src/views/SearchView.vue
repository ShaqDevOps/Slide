<script>
import PeopleYouMayKnow from '../components/PeopleYouMayKnow.vue';
import Trends from '../components/Trends.vue';

export default {name: 'SearchView',
    components:{PeopleYouMayKnow, Trends}

}; 


</script>


<template>

    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4 ">

        <div class="main-left col-span-3 space-y-4">
            <div class="bg-white border border-gray-200 rounded-lg">
            <div class="p-4 flex space-x-4">
                <input type="search" class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What are you looking for?">
                <a href="#" class="inline-block py-4 px-6 bg-purple-600 text-white rounded-lg"> Search </a>

                </div>


            </div>


                
                <div class="p-4 bg-white border border-gray-200 rounded-lg grid grid-cols-4 gap-4">
            <div class="p-4 text-center bg-gray-100 rounded-lg">

        <img src="../assets/cat.jpg" class="mb-6 rounded-full">

      <p><strong> Username Placeholder</strong></p>
 

<div class="mt-6 flex space-x-8 justify-around">
                <p class="text-xs text-gray-500">180 Followers</p>
                <p class="text-xs text-gray-500">120 Posts</p>

            </div>


        </div>


        <div class="p-4 text-center bg-gray-100 rounded-lg ">

<img src="../assets/cat.jpg" class="mb-6 rounded-full">

<p><strong> Username Placeholder</strong></p>


<div class="mt-6 flex space-x-8 justify-around">
        <p class="text-xs text-gray-500">180 Followers</p>
        <p class="text-xs text-gray-500">120 Posts</p>

    </div>


</div>


<div class="p-4 text-center bg-gray-100 rounded-lg ">

<img src="../assets/cat.jpg" class="mb-6 rounded-full">

<p><strong> Username Placeholder</strong></p>


<div class="mt-6 flex space-x-8 justify-around">
        <p class="text-xs text-gray-500">180 Followers</p>
        <p class="text-xs text-gray-500">120 Posts</p>

    </div>


</div>
<div class="p-4 text-center bg-gray-100 rounded-lg ">

<img src="../assets/cat.jpg" class="mb-6 rounded-full">

<p><strong> Username Placeholder</strong></p>


<div class="mt-6 flex space-x-8 justify-around">
        <p class="text-xs text-gray-500">180 Followers</p>
        <p class="text-xs text-gray-500">120 Posts</p>

    </div>


</div>
<div class="p-4 text-center bg-gray-100 rounded-lg ">

<img src="../assets/cat.jpg" class="mb-6 rounded-full">

<p><strong> Username Placeholder</strong></p>


<div class="mt-6 flex space-x-8 justify-around">
        <p class="text-xs text-gray-500">180 Followers</p>
        <p class="text-xs text-gray-500">120 Posts</p>

    </div>


</div>
<div class="p-4 text-center bg-gray-100 rounded-lg ">

<img src="../assets/cat.jpg" class="mb-6 rounded-full">

<p><strong> Username Placeholder</strong></p>


<div class="mt-6 flex space-x-8 justify-around">
        <p class="text-xs text-gray-500">180 Followers</p>
        <p class="text-xs text-gray-500">120 Posts</p>

    </div>


</div>




    </div>
    <div class="p-4 bg-white border border-gray-200 text-center rounded-lg">
                <div class="mb-6 flex items-center justify-between">
                    <div class="flex items-center space-x-3">
      <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden">

        <img src="../assets/cat.jpg" class="mb-6 rounded-full">
      </div>
      <p>Username Placeholder</p>
      </div>
      <p class="text-gray-600"> 18 minutes ago</p>

                </div>
                <p>An Image/video would go here </p>



                <div class="my-6 flex items-center justify-between">
  <!-- Left Side: Like and Comment Buttons -->
  <div class="flex items-center space-x-6">
    <!-- Like Button -->
    <div class="flex items-center space-x-1 cursor-pointer" @click="toggleLike">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="currentColor"
        viewBox="0 0 24 24"
        :class="liked ? 'text-red-500' : 'text-gray-500'"
        class="w-5 h-5 transition-colors duration-200 ease-in-out"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"
        />
      </svg>
      <span class="text-gray-500 text-xs">{{ liked ? 1 : 0 }} likes</span>
    </div>

    <!-- Comment Button -->
    <div class="flex items-center space-x-1 cursor-pointer">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        class="w-5 h-5 text-gray-500"
      >
        <path
          stroke-linecap="round"
          stroke-linejoin="round"
          stroke-width="2"
          d="M8 10h.01M12 10h.01M16 10h.01M21 10.5A8.38 8.38 0 0112.5 19 8.38 8.38 0 014 10.5C4 5.81 7.81 2 12.5 2S21 5.81 21 10.5z"
        />
      </svg>
      <span class="text-gray-500 text-xs">0 comments</span>
    </div>
  </div>

  <!-- Right Side: Three-Dot Menu -->
  <div class="relative">
    <!-- Three Dots Icon -->
    <div class="cursor-pointer" @click="toggleMenu">
      <svg
        xmlns="http://www.w3.org/2000/svg"
        fill="none"
        viewBox="0 0 24 24"
        stroke="currentColor"
        class="w-6 h-6 text-gray-500"
      >
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6h.01M12 12h.01M12 18h.01" />
      </svg>
    </div>

    <!-- Dropdown Menu -->
    <div
      v-if="showMenu"
      class="absolute right-0 mt-2 w-40 bg-white border rounded-md shadow-lg"
    >
      <ul class="py-1">
        <li>
          <a
            href="#"
            class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100"
            @click="toggleMenu"
          >
            Report Post
          </a>
        </li>
        <!-- Add more menu items here in the future -->
      </ul>
    </div>
  </div>
</div>
</div>
 

        </div>




        <div class="main-right col-span-1">

<PeopleYouMayKnow>

</PeopleYouMayKnow>

<Trends>

</Trends>
           

</div>

</div>





</template>

