<script>
export default {}
</script>

<template>
  <form>
    <div class="mb-3">
      <label for="url-platform" class="form-label">Url Plataforma</label>
      <input type="url" class="form-control" id="url-platform" />
    </div>
    <div class="mb-3">
      <label for="user-platform" class="form-label">Usuario</label>
      <input type="text" class="form-control" id="user-platform" />
    </div>
    <div class="mb-3">
      <label for="pass-platform" class="form-label">Contraseña</label>
      <input type="password" class="form-control" id="pass-platform" />
    </div>
    <div class="mb-3 d-flex justify-content-center">
      <button class="btn btn-validate">Validar</button>
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
