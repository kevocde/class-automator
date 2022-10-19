<script>
import { useClassStore } from "@/stores/class";

export default {
  data() {
    return {
      classModel: useClassStore()
    };
  }
}
</script>

<template>
  <form @submit.prevent="classModel.validateUserInformation()">
    <div class="mb-3">
      <label for="url-platform" class="form-label">Url Plataforma</label>
      <input type="url" class="form-control" id="url-platform" v-model="classModel.userInformation.platform" />
    </div>
    <div class="mb-3">
      <label for="user-platform" class="form-label">Usuario</label>
      <input type="text" class="form-control" id="user-platform" v-model="classModel.userInformation.user" />
    </div>
    <div class="mb-3">
      <label for="pass-platform" class="form-label">Contraseña</label>
      <input type="password" class="form-control" id="pass-platform" v-model="classModel.userInformation.password" />
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
