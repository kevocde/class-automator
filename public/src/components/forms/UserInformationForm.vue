<script>
import { useClassStore } from "@/stores/class";
import InputForm from "@/components/forms/fields/InputForm.vue";

export default {
  props: ["stepper"],
  data() {
    return {
      classModel: useClassStore(),
    };
  },
  methods: {
    validateForm(event) {
      event.target.classList.add("was-validated");
      event.target.querySelector('[type="submit"]').disabled = true;

      if (event.target.checkValidity()) {
        this.classModel
          .validateUserInformation()
          .then((res) => {
            if (res) {
              this.stepper.activeStep(1);
            }
          })
          .finally(() => {
            event.target.querySelector('[type="submit"]').disabled = false;
          });
      } else {
        event.target.querySelector('[type="submit"]').disabled = false;
      }
    },
  },
  components: { InputForm },
};
</script>

<template>
  <form @submit.prevent="validateForm" novalidate>
    <div class="mb-3">
      <InputForm
        type="text"
        required
        label="Usuario"
        id="user-platform"
        invalid-msg="This field is required"
        :model="classModel.user_information.user"
        @update:model="(value) => (classModel.user_information.user = value)"
      />
    </div>
    <div class="mb-3">
      <InputForm
        type="password"
        required
        label="Contraseña"
        id="pass-platform"
        invalid-msg="This field is required"
        :model="classModel.user_information.password"
        @update:model="
          (value) => (classModel.user_information.password = value)
        "
      />
    </div>
    <div class="mb-3 d-flex justify-content-center">
      <button class="btn btn-validate" type="submit">Validar</button>
    </div>
  </form>
</template>

<style scoped lang="sass">
@import "~bootstrap/scss/bootstrap-utilities.scss"

.btn-validate
  background-color: $indigo-400
  color: $indigo-100

  &:hover, &:focus
    background-color: $indigo-500
    color: $indigo-100
</style>
