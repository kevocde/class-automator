<script>
import UserInformationForm from "@/components/forms/UserInformationForm.vue";
import ClassDetailsForm from "@/components/forms/ClassDetailsForm.vue";
import ScheduleForm from "@/components/forms/ScheduleForm.vue";

const ACTIVE_CLASS = "active";

export default {
  name: "Stepper",
  data() {
    return {
      steps: [],
    };
  },
  methods: {
    activeStep(key) {
      this.steps.forEach(({ activator, content }, step_key) => {
        let action = key !== step_key ? "remove" : "add";

        activator.classList[action](ACTIVE_CLASS);
        content.classList[action](ACTIVE_CLASS);
      });
    },
    loadSteps() {
      const activators = document.querySelectorAll(
        ".stepper .stepper-header .stepper-header-item"
      );
      const contents = document.querySelectorAll(
        ".stepper .stepper-content .stepper-content-option"
      );

      activators.forEach((value, key) => {
        this.steps.push({
          activator: value,
          content: contents[key],
          interaction: !value.classList.contains("no-interact"),
          active: value.classList.contains("active"),
        });

        this.steps[key].activator.addEventListener("click", () => {
          if (this.steps[key].interaction) {
            this.steps[key].active = true;

            this.activeStep(key);
          }
        });
      });
    },
    loadDefaultStep() {
      /** @todo Add url interaction, for example: when the url contains "#step-1", active the step 1  */
      this.activeStep(0);
    },
  },
  mounted() {
    this.loadSteps();
    this.loadDefaultStep();
  },
  components: { ScheduleForm, UserInformationForm, ClassDetailsForm },
};
</script>

<template>
  <div class="stepper">
    <ul class="d-flex gap-1 w-100 stepper-header">
      <li
        class="flex-fill d-flex align-items-center justify-content-center stepper-header-item no-interact"
      >
        <div
          class="rounded-circle d-flex justify-content-center align-items-center fs-5 fw-bold header-item-circle"
        >
          <span>1</span>
        </div>
        <div class="ps-4 header-item-label">
          <span>Información de usuario</span>
        </div>
      </li>
      <li
        class="flex-fill d-flex align-items-center justify-content-center stepper-header-item no-interact"
      >
        <div
          class="rounded-circle d-flex justify-content-center align-items-center fs-5 fw-bold header-item-circle"
        >
          <span>2</span>
        </div>
        <div class="ps-4 header-item-label">
          <span>Detalles de la clase</span>
        </div>
      </li>
      <li
        class="flex-fill d-flex align-items-center justify-content-center stepper-header-item no-interact"
      >
        <div
          class="rounded-circle d-flex justify-content-center align-items-center fs-5 fw-bold header-item-circle"
        >
          <span>3</span>
        </div>
        <div class="ps-4 header-item-label"><span>Agendamiento</span></div>
      </li>
    </ul>
    <div class="d-flex stepper-content">
      <div class="stepper-content-option">
        <div class="d-flex justify-content-center py-2">
          <UserInformationForm class="w-25" :stepper="this" />
        </div>
      </div>
      <div class="stepper-content-option">
        <div class="d-flex justify-content-center py-2">
          <ClassDetailsForm class="w-50" :stepper="this" />
        </div>
      </div>
      <div class="stepper-content-option">
        <div class="d-flex justify-content-center py-2">
          <ScheduleForm class="w-50" :stepper="this" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="sass">
@import "~bootstrap/scss/bootstrap-utilities.scss"

.stepper
  width: 100%

  .stepper-header
    list-style: none

    .stepper-header-item
      text-align: center
      cursor: pointer

      .header-item-circle
        width: 4rem
        height: 4rem
        background-color: $gray-400
        color: $white

      .header-item-label
        color: $gray-400

      &.active
        .header-item-circle
          background-color: $pink-400

        .header-item-label
          color: $secondary

  .stepper-content
    .stepper-content-option
      display: none !important

      &.active
        display: block !important
        width: 100%
</style>
