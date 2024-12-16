import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import FeedView from "@/views/FeedView.vue";
import MessageView from "@/views/MessageView.vue";
import SearchView from "@/views/SearchView.vue";
import ProfileView from "@/views/ProfileView.vue";
import FriendsView from "@/views/FriendsView.vue";
import PostDetailView from "@/views/PostDetailView.vue"; // Import the PostDetail component

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/profile/:id",
      name: "profile",
      component: ProfileView,
    },
    {
      path: "/profile/:id/friends/",
      name: "friends",
      component: FriendsView,
    },
    {
      path: "/search",
      name: "search",
      component: SearchView,
    },
    {
      path: "/messages",
      name: "messages",
      component: MessageView,
    },
    {
      path: "/feed",
      name: "feed",
      component: FeedView,
    },
    {
      path: "/posts/:id", // New route for post details
      name: "post-detail",
      component: PostDetailView,
    },
    {
      path: "/login",
      name: "login",
      component: LogInView,
    },
    {
      path: "/signup",
      name: "signup",
      component: SignUpView,
    },
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/about",
      name: "about",
      component: () => import("../views/AboutView.vue"),
    },
  ],
});

export default router;
