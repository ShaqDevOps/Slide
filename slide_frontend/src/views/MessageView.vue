<template>
    <div class="max-w-7xl mx-auto grid grid-cols-4 gap-4">
      <!-- LEFT COLUMN -->
      <div class="main-left col-span-1">
        <div class="p-4 bg-white border border-gray-200 rounded-lg">
          <h3 class="mb-6 text-xl font-bold text-gray-800"></h3>
          <div class="space-y-4">
            <!-- User Row -->
            <div class="flex items-center justify-between">
              <!-- Profile Picture and Username -->
              <div class="flex items-center space-x-3">
                <!-- Profile Picture -->
                <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden">
                  <!-- Replace with an image -->
                  <img src="../assets/cat.jpg" class="w-full h-full object-cover"> 
                </div>
                <!-- Username -->
                <p class="text-gray-800 font-medium">Username Placeholder</p>
              </div>
              <span class="text-xs text-gray-500"> 18 minutes ago</span>
 
            </div>
          </div>
        </div>
      </div>

      <!-- CENTER COLUMN -->
       <div class="main-center col-span-3 space-y-4">
        <div class="bg-white border border-gray-200 rounded-lg">
  <div class="flex flex-col flex-grow p-4">
    <!-- Chat Bubble Row -->
    <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
        <div>
      <!-- Main User Message Bubble -->
      <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
        <p class="text-sm">This is a test message from the user</p>

    </div>
        <!-- Timestamp -->
    <span class="text-xs text-gray-500 mt-1 pr-10">2 min ago</span>
      </div>
      <!-- Profile Picture -->
      <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden shrink-0">
        <img src="../assets/cat.jpg" class="mb-6 rounded-full">
      </div>

    </div>

    <!-- Chat Bubble Row -->
    <div class="flex w-full mt-2 space-x-3 max-w-md ml-auto justify-end">
        <div>
      <!-- Main User Message Bubble -->
      <div class="bg-blue-600 text-white p-3 rounded-l-lg rounded-br-lg">
        <p class="text-sm">This is a longer test message from the user testing the break of messages, to make sure they break correctly</p>

    </div>
        <!-- Timestamp -->
    <span class="text-xs text-gray-500 mt-1 pr-10">2 min ago</span>
      </div>
      <!-- Profile Picture -->
      <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden shrink-0">
        <img src="../assets/cat.jpg" class="mb-6 rounded-full">
      </div>

    </div>
    <div class="flex w-full mt-2 space-x-3 max-w-md">
              <!-- Profile Picture -->
      <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden shrink-0">
        <img src="../assets/cat.jpg" class="mb-6 rounded-full">
      </div>
        <div>
      <!-- Main User Message Bubble -->
      <div class="bg-gray-300 text-white p-3 rounded-l-lg rounded-br-lg">
        <p class="text-sm">This is a test message to the user</p>
    </div>
        <!-- Timestamp -->
    <span class="text-xs text-gray-500 mt-1 pr-10">2 min ago</span>
      </div>
      </div>

         <div class="flex w-full mt-2 space-x-3 max-w-md">
              <!-- Profile Picture -->
      <div class="w-10 h-10 rounded-full bg-gray-300 overflow-hidden shrink-0">
        <img src="../assets/cat.jpg" class="mb-6 rounded-full">
      </div>
        <div>
      <!-- Main User Message Bubble -->
      <div class="bg-gray-300 text-white p-3 rounded-l-lg rounded-br-lg">
        <p class="text-sm">This is a longer message to the user to make sure the messages are breaking correctly </p>
    </div>
        <!-- Timestamp -->
    <span class="text-xs text-gray-500 mt-1 pr-10">2 min ago</span>
      </div>
      </div>

  </div>
</div>


        <div class="bg-white border border-gray-200 text-center rounded-lg">

<div class="p-4">

    <textarea class="p-4 w-full bg-gray-100 rounded-lg" placeholder="What do you want to say?"></textarea>
</div>


    <div class="p-4 border-t border-gray-100 flex justify-between">

        <a href="#" class="py-2 px-2 bg-purple-600 text-white text-xs font-medium rounded-lg hover:bg-purple-900"> Send </a> 


</div>

    
</div>


       </div>
    </div>
  </template>