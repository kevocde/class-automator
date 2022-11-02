import { defineStore } from "pinia";

export const useClassStore = defineStore("class", {
  state() {
    return {
      userInformation: {
        platform: "",
        user: "",
        password: "",
      },
      classDetails: {
        lang: "",
        level: "",
        headquarter: "",
        studentCode: "",
        unitOther: "",
      },
      schedule: {
        date: "",
        time: "",
        recurring: false,
        times: 1,
      },
    };
  },
  actions: {
    validateUserInformation() {
      console.log("Validating user information");
    },
    validateClassDetails() {
      console.log("Validating class details");
    },
    validateSchedule() {
      console.log("Validating schedule");
    },
    send() {
      console.log("Sending class");
    },
  },
});
