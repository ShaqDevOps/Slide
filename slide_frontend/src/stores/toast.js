import { defineStore } from "pinia";

export const useToastStore = defineStore({
  id: "toast",

  state: () => ({
    ms: 0,
    message: "", // Fixed name from `messages` to `message`
    classes: "",
    isVisible: false,
  }),

  actions: {
    showToast(ms, message, classes) {
      console.log("showToast Triggered:", { ms, message, classes });

      this.ms = parseInt(ms);
      this.message = message;
      this.classes = classes + " transition transform";
      this.isVisible = true;

      setTimeout(() => {
        console.log("Applying translate-y");
        this.classes += " -translate-y-28";
      }, 10);

      setTimeout(() => {
        console.log("Removing translate-y");
        this.classes = this.classes.replace("-translate-y-28", "");
      }, this.ms - 500);

      setTimeout(() => {
        console.log("Hiding toast");
        this.isVisible = false;
      }, this.ms);
    },
  },
});
