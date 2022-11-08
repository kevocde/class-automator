<script>
import SelectForm from "@/components/forms/fields/SelectForm.vue";
import InputForm from "@/components/forms/fields/InputForm.vue";
import CheckboxForm from "@/components/forms/fields/CheckboxForm.vue";
import { useClassStore } from "@/stores/class";

export default {
  props: ["stepper"],
  data() {
    return {
      classModel: useClassStore(),
    };
  },
  methods: {
    initDatepickers() {
      this.classModel.getDatesEnabled().then((dates) => {
        $("#schedule-date").datepicker({
          gotoCurrent: true,
          beforeShowDay: (date) => {
            return [
              dates.some(
                (value) =>
                  `${date.getMonth()+1}/${date.getDate()}/${date.getFullYear()}` ===
                  value
              ),
              "",
              "",
            ];
          },
          onSelect: (value) => {
            this.classModel.schedule.date = value;
          },
        });
      });
    },
    validateForm(event) {
      event.target.classList.add("was-validated");

      if (event.target.checkValidity()) {
        this.stepper.activeStep(2);
      }
    },
  },
  mounted() {
    this.initDatepickers();
  },
  components: { CheckboxForm, SelectForm, InputForm },
};
</script>

<template>
  <form @submit.prevent="validateForm" novalidate>
    <div class="row mb-3">
      <div class="col">
        <InputForm
          required
          readonly
          label="Fecha"
          id="schedule-date"
          invalid-msg="This field is required"
          :model="classModel.schedule.date"
          @update:model="(value) => (classModel.schedule.date = value)"
        />
      </div>
      <div class="col">
        <SelectForm
          required
          label="Hora"
          id="schedule-time"
          invalid-msg="This field is required"
          :model="classModel.schedule.time"
          @update:model="(value) => (classModel.schedule.time = value)"
        >
          <option value="" selected>Seleccione</option>
          <option value="1">6-8 am</option>
          <option value="2">8-10 am</option>
          <option value="3">10-12 am</option>
          <option value="4">1-3 pm</option>
          <option value="5">3-5 pm</option>
          <option value="6">5-7 pm</option>
          <option value="7">7-9 pm</option>
        </SelectForm>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col d-flex justify-content-center">
        <CheckboxForm
          label="Agendar de manera recurrente"
          id="schedule-recurring"
          invalid-msg="This field is required"
          :model="classModel.schedule.recurring"
          @update:model="(value) => (classModel.schedule.recurring = value)"
        />
      </div>
    </div>
    <div class="row mb-3" v-show="classModel.schedule.recurring">
      <div class="col">
        <InputForm
          type="number"
          :required="this.classModel.schedule.recurring"
          label="¿Cúantas clases desea agendar con mismo día y hora?"
          id="schedule-times"
          invalid-msg="This field is required"
          :model="classModel.schedule.times"
          @update:model="(value) => (classModel.schedule.times = value)"
        />
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
