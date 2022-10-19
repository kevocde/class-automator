<script setup></script>

<template>
  <form>
    <div class="row mb-3">
      <div class="col">
        <label for="schedule-date" class="form-label">Fecha</label>
        <input type="date" class="form-control" id="schedule-date" />
      </div>
      <div class="col">
        <label for="schedule-time" class="form-label">Hora</label>
        <select id="schedule-time" class="form-select">
          <option value="" selected>Seleccione</option>
          <option value="">6-8 am</option>
          <option value="">8-10 am</option>
          <option value="">10-12 am</option>
          <option value="">1-3 pm</option>
          <option value="">3-5 pm</option>
          <option value="">5-7 pm</option>
          <option value="">7-9 pm</option>
        </select>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col d-flex justify-content-center">
        <div class="form-check">
          <input class="form-check-input" type="checkbox" value="" id="schedule-recurring">
          <label class="form-check-label" for="schedule-recurring">
            Agendar de manera recurrente
          </label>
        </div>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col">
        <label for="schedule-times" class="form-label">
          ¿Cúantas clases desea agendar con mismo día y hora?
        </label>
        <input type="number" class="form-control" id="schedule-times" />
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
