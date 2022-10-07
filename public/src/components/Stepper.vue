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
      this.steps.forEach(({ activator, content }, step_key) => {
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
          content: contents[key]
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
      <li class="flex-fill py-2 text-center stepper-header-item">1</li>
      <li class="flex-fill py-2 text-center stepper-header-item">2</li>
      <li class="flex-fill py-2 text-center stepper-header-item">3</li>
    </ul>
    <div class="d-flex stepper-content">
      <div class="stepper-content-option">First step content</div>
      <div class="stepper-content-option">Second step content</div>
      <div class="stepper-content-option">Third step content</div>
    </div>
  </div>
</template>

<style scoped lang="sass">
.stepper
  width: 100%

  .stepper-header
    list-style: none

    .stepper-header-item
      text-align: center
      cursor: pointer

  .stepper-content
    .stepper-content-option
      display: none

      &.active
        display: block
        width: 100%

</style>
