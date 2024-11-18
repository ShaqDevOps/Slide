import { defineStore } from "pinia";
import axios from "axios";

export const useUserStore = defineStore({
  id: "user",

  state: () => ({
    user: {
      isAuthenticated: false,
      id: null, // Ensure this remains a string to prevent issues with large integers
      name: null,
      username: null,
      email: null,
      access: null,
      refresh: null,
    },
  }),

  actions: {
    // Initialize the store with data from localStorage
    initStore() {
      console.log("initStore");
      if (localStorage.getItem("user.access")) {
        console.log("User has access");
        this.user.access = localStorage.getItem("user.access");
        this.user.refresh = localStorage.getItem("user.refresh");
        this.user.id = localStorage.getItem("user.id").toString(); // Store as string
        this.user.name = localStorage.getItem("user.name");
        this.user.username = localStorage.getItem("user.username");
        this.user.email = localStorage.getItem("user.email");
        this.user.isAuthenticated = true;

        axios.defaults.headers.common[
          "Authorization"
        ] = `JWT ${this.user.access}`;

        // Optionally refresh the token on initialization
        this.refreshToken();

        console.log("Initialized user: ", this.user);
      }
    },

    // Set the authentication token
    setToken(data) {
      console.log("setToken", data);

      this.user.access = data.access;
      this.user.refresh = data.refresh;
      this.user.isAuthenticated = true;

      localStorage.setItem("user.access", data.access);
      localStorage.setItem("user.refresh", data.refresh);

      axios.defaults.headers.common["Authorization"] = `JWT ${data.access}`;
    },

    // Clear all authentication and user information
    removeToken() {
      console.log("removeToken");

      this.user.refresh = null;
      this.user.access = null;
      this.user.isAuthenticated = false;
      this.user.id = null;
      this.user.name = null;
      this.user.username = null;
      this.user.email = null;

      localStorage.removeItem("user.access");
      localStorage.removeItem("user.refresh");
      localStorage.removeItem("user.id");
      localStorage.removeItem("user.name");
      localStorage.removeItem("user.username");
      localStorage.removeItem("user.email");

      delete axios.defaults.headers.common["Authorization"];
    },

    // Set the user information in the store and localStorage
    setUserInfo(user) {
      console.log("setUserInfo", user);

      this.user.id = String(user.id); // Ensure ID is stored as a string
      console.log("user_id", user.id);
      this.user.name = user.name;
      this.user.username = user.username;
      this.user.email = user.email;

      localStorage.setItem("user.id", this.user.id);
      localStorage.setItem("user.name", this.user.name);
      localStorage.setItem("user.username", this.user.username);
      localStorage.setItem("user.email", this.user.email);

      console.log("User updated: ", this.user);
    },

    // Refresh the JWT access token
    refreshToken() {
      console.log("Refreshing token...");
      axios
        .post("/auth/jwt/refresh", {
          refresh: this.user.refresh,
        })
        .then((response) => {
          this.user.access = response.data.access;
          localStorage.setItem("user.access", response.data.access);

          axios.defaults.headers.common["Authorization"] =
            "JWT " + response.data.access;

          console.log("Token refreshed successfully");
        })
        .catch((error) => {
          console.error("Error refreshing token: ", error);
          this.removeToken();
        });
    },
  },
});
