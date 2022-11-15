<script>
import SelectForm from "@/components/forms/fields/SelectForm.vue";
import InputForm from "@/components/forms/fields/InputForm.vue";
import TextareaForm from "@/components/forms/fields/TextareaForm.vue";
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
        this.stepper.activeStep(2);
      }
    },
  },
  components: { TextareaForm, SelectForm, InputForm },
};
</script>

<template>
  <form @submit.prevent="validateForm" novalidate>
    <div class="row mb-3">
      <div class="col">
        <SelectForm
          required
          label="Idioma"
          id="class-lang"
          invalid-msg="This field is required"
          :model="classModel.classDetails.lang"
          @update:model="(value) => (classModel.classDetails.lang = value)"
        >
          <option value="" selected>Seleccione</option>
          <option value="en">Inglés</option>
          <option value="fr">Francés</option>
        </SelectForm>
      </div>
      <div class="col">
        <SelectForm
          required
          label="Nivel"
          id="class-level"
          invalid-msg="This field is required"
          :model="classModel.classDetails.level"
          @update:model="(value) => (classModel.classDetails.level = value)"
        >
          <option value="" selected>Seleccione</option>
          <option value="A1">A1</option>
          <option value="A2">A2</option>
          <option value="B1">B1</option>
          <option value="B1+">B1+</option>
          <option value="B2">B2</option>
          <option value="C1">C1</option>
          <option value="C2">C2</option>
        </SelectForm>
      </div>
    </div>
    <div class="row mb-3">
      <div class="col">
        <SelectForm
          required
          label="Sede"
          id="class-headquarter"
          invalid-msg="This field is required"
          :model="classModel.classDetails.headquarter"
          @update:model="
            (value) => (classModel.classDetails.headquarter = value)
          "
        >
          <option value="" selected>Seleccione</option>
          <option value="1">Cr 5 Nº 37-76 Ibagué</option>
          <option value="2">Centro 11 con 4ta Ibagué</option>
          <option value="3">CC Mercurio/jumbo Soacha</option>
          <option value="4">CC Ventura Terreros local 2-40 Soacha</option>
          <option value="5">Carrera 13 # 45A-31 Chapinero Bogotá</option>
        </SelectForm>
      </div>
      <div class="col">
        <InputForm
          required
          label="Código de estudiante"
          id="class-studentCode"
          invalid-msg="This field is required"
          :model="classModel.userInformation.studentCode"
          @update:model="
            (value) => (classModel.userInformation.studentCode = value)
          "
        />
      </div>
    </div>
    <div class="row mb-3">
      <div class="col">
        <TextareaForm
          required
          label="Unidad y/o avance"
          id="class-unitOther"
          invalid-msg="This field is required"
          :model="classModel.classDetails.unitOther"
          @update:model="(value) => (classModel.classDetails.unitOther = value)"
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
