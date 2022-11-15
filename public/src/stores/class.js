import { defineStore } from "pinia";
import axios from "axios";

export const useClassStore = defineStore("class", {
  state() {
    return {
      userInformation: {
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
    async validateUserInformation() {
      let valid = await axios
        .post("/user-information", this.userInformation)
        .catch(() => false);

      return valid !== false;
    },
    async getDatesEnabled() {
      return await axios
        .get("/dates-enabled")
        .then((res) => res.data.datesEnabled)
        .catch(() => []);
    },
    async doSchedule() {
      return await axios
        .post("/schedules", {
          userInformation: this.userInformation,
          classDetails: this.classDetails,
          schedule: this.schedule,
        })
        .catch(() => false);
    },
    resetForm() {
      this.$reset();
    },
    send() {
      console.log("Sending class");
    },
  },
});
