<script>
import { useClassStore } from "@/stores/class";

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

      if (event.target.checkValidity()) {
        this.stepper.activeStep(1);
      }
    },
  },
};
</script>

<template>
  <form @submit.prevent="validateForm" novalidate>
    <div class="mb-3">
      <label for="url-platform" class="form-label">Url Plataforma</label>
      <input
        type="url"
        class="form-control"
        id="url-platform"
        v-model="classModel.userInformation.platform"
        required
      />
      <div class="invalid-feedback">This field is required</div>
    </div>
    <div class="mb-3">
      <label for="user-platform" class="form-label">Usuario</label>
      <input
        type="text"
        class="form-control"
        id="user-platform"
        v-model="classModel.userInformation.user"
        required
      />
      <div class="invalid-feedback">This field is required</div>
    </div>
    <div class="mb-3">
      <label for="pass-platform" class="form-label">Contraseña</label>
      <input
        type="password"
        class="form-control"
        id="pass-platform"
        v-model="classModel.userInformation.password"
        required
      />
      <div class="invalid-feedback">This field is required</div>
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
