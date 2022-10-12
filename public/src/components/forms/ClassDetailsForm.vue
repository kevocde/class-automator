<script>
export default {}
</script>

<template>
  <form>
    <div class="row mb-3">
      <div class="col">
        <label for="class-lang" class="form-label">Idioma</label>
        <select id="class-lang" class="form-select">
          <option value="en">Inglés</option>
          <option value="pt">Portugués</option>
        </select>
      </div>
      <div class="col">
        <label for="class-level" class="form-label">Nivel</label>
        <select id="class-level" class="form-select"></select>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col">
        <label for="class-headquarter" class="form-label">Sede</label>
        <select id="class-headquarter" class="form-select"></select>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col">
        <label for="class-details" class="form-label">Unidad y/o avance</label>
        <textarea id="class-details" class="form-control"></textarea>
      </div>
    </div>
    <div class="mb-3 d-flex justify-content-center">
      <button class="btn btn-validate">Continuar</button>
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
