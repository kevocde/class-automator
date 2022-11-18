import { defineStore } from "pinia";
import axios from "axios";

export const useClassStore = defineStore("class", {
  state() {
    return {
      user_information: {
        user: "",
        password: "",
      },
      class_details: {
        lang: "",
        level: "",
        headquarter: "",
        student_code: "",
        unit_other: "",
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
        .post("/user-information", this.user_information)
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
          user_information: this.user_information,
          class_details: this.class_details,
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
