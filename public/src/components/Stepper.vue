<script>
const ACTIVE_CLASS = 'active'

export default {
  data() {
    return {
      steps: []
    }
  },
  methods: {
    activeStep(key) {
      this.steps.forEach(({ activator, content, active }, step_key) => {
        let action = (key !== step_key) ? 'remove' : 'add'

        activator.classList[action](ACTIVE_CLASS)
        content.classList[action](ACTIVE_CLASS)
      })
    },
    loadSteps() {
      const activators = document.querySelectorAll('.stepper .stepper-header .stepper-header-item')
      const contents = document.querySelectorAll('.stepper .stepper-content .stepper-content-option')

      activators.forEach((value, key) => {
        value.addEventListener('click', () => { this.activeStep(key) })

        this.steps.push({
          activator: value,
          content: contents[key],
          active: false
        })
      })
    },
    loadDefaultStep() {
      /** @todo Add url interaction, for example: when the url contains "#step-1", active the step 1  */
      this.activeStep(0)
    }
  },
  mounted() {
    this.loadSteps()
    this.loadDefaultStep()
  }
}
</script>

<template>
  <div class="stepper">
    <ul class="d-flex gap-1 w-100 stepper-header">
      <li class="flex-fill py-2 d-flex align-items-center justify-content-center stepper-header-item">
        <div class="rounded-circle d-flex justify-content-center align-items-center fs-5 fw-bold header-item-circle"><span>1</span></div>
        <div class="ps-4 header-item-label"><span>Información de usuario</span></div>
      </li>
      <li class="flex-fill py-2 d-flex align-items-center justify-content-center stepper-header-item">
        <div class="rounded-circle d-flex justify-content-center align-items-center fs-5 fw-bold header-item-circle"><span>2</span></div>
        <div class="ps-4 header-item-label"><span>Detalles de clase</span></div>
      </li>
      <li class="flex-fill py-2 d-flex align-items-center justify-content-center stepper-header-item">
        <div class="rounded-circle d-flex justify-content-center align-items-center fs-5 fw-bold header-item-circle"><span>3</span></div>
        <div class="ps-4 header-item-label"><span>Agendamiento</span></div>
      </li>
    </ul>
    <div class="d-flex stepper-content">
      <div class="stepper-content-option">First step content</div>
      <div class="stepper-content-option">Second step content</div>
      <div class="stepper-content-option">Third step content</div>
    </div>
  </div>
</template>

<style scoped lang="sass">
@import "~bootstrap/scss/bootstrap-utilities.scss"

.stepper
  width: 100%

  .stepper-header
    list-style: none

    .stepper-header-item
      text-align: center
      cursor: pointer

      .header-item-circle
        width: 4rem
        height: 4rem
        background-color: $gray-400
        color: $white

      .header-item-label
        color: $gray-400

      &.active
        .header-item-circle
          background-color: $pink-400

        .header-item-label
          color: $secondary

  .stepper-content
    .stepper-content-option
      display: none

      &.active
        display: block
        width: 100%

</style>
