

<template>
  <header class="bg-white shadow-md p-4 flex justify-between items-center">
    <!-- App Name on the Left -->
    <div class="text-2xl font-bold">
      <span>Slide</span>
    </div>

    <!-- Centered Navigation Links -->
    <nav class="flex space-x-8">
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
    <div class="flex items-center space-x-2">
      <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden">
        <!-- Replace this div with an img tag for an actual profile picture -->
        <!-- <img src="profile.jpg" alt="Profile Picture" class="w-full h-full object-cover"> -->
      </div>
    </div>
  </header>

  <main class="px-8 py-6 bg-gray-100">

    <RouterView/> 
     </main>
</template>
