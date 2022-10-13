<script setup></script>

<template>
  <form>
    <div class="row mb-3">
      <div class="col">
        <label for="class-lang" class="form-label">Idioma</label>
        <select id="class-lang" class="form-select">
          <option value="" selected>Seleccione</option>
          <option value="en">Inglés</option>
          <option value="pt">Francés</option>
        </select>
      </div>
      <div class="col">
        <label for="class-level" class="form-label">Nivel</label>
        <select id="class-level" class="form-select">
          <option value="" selected>Seleccione</option>
          <option value="1">A1</option>
          <option value="2">A2</option>
          <option value="3">B1</option>
          <option value="4">B1+</option>
          <option value="5">B2</option>
          <option value="6">C1</option>
          <option value="7">C2</option>
        </select>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col">
        <label for="class-headquarter" class="form-label">Sede</label>
        <select id="class-headquarter" class="form-select">
          <option value="" selected>Seleccione</option>
          <option value="">Cr 5 Nº 37-76 Ibagué</option>
          <option value="">Centro 11 con 4ta Ibagué</option>
          <option value="">CC Mercurio/jumbo Soacha</option>
          <option value="">CC Ventura Terreros local 2-40 Soacha</option>
          <option value="">Carrera 13 # 45A-31 Chapinero Bogotá</option>
        </select>
      </div>
      <div class="col">
        <label for="student-code" class="form-label">
          Código de estudiante
        </label>
        <input type="text" class="form-control" id="student-code" />
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
