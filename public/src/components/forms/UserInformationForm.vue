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

      if (
        event.target.checkValidity() &&
        this.classModel.validateUserInformation()
      ) {
        this.stepper.activeStep(1);
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
        type="url"
        required
        label="Url Plataforma"
        id="url-platform"
        invalid-msg="This field is required"
        :label-attrs="{ for: 'url-platform' }"
        :model="classModel.userInformation.platform"
        @update:model="(value) => (classModel.userInformation.platform = value)"
      />
    </div>
    <div class="mb-3">
      <InputForm
        type="text"
        required
        label="Usuario"
        id="user-platform"
        invalid-msg="This field is required"
        :model="classModel.userInformation.user"
        @update:model="(value) => (classModel.userInformation.user = value)"
      />
    </div>
    <div class="mb-3">
      <InputForm
        type="password"
        required
        label="Contraseña"
        id="pass-platform"
        invalid-msg="This field is required"
        :model="classModel.userInformation.password"
        @update:model="(value) => (classModel.userInformation.password = value)"
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
