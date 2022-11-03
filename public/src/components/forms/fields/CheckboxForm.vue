<script>
export default {
  props: {
    id: {
      type: String,
      required: true,
    },
    label: {
      type: String,
      default: "",
    },
    labelAttrs: {
      type: Object,
    },
    invalidMsg: String,
    validMsg: String,
    model: {},
  },
  emits: ["update:model"],
  // mounted() {
  //   document.getElementById(this.$props.id).addEventListener("change", (evt) => {
  //     console.log(evt.target.checked);
  //   });
  // },
};
</script>

<template>
  <div class="form-check">
    <input
      type="checkbox"
      class="form-check-input"
      :id="id"
      :value="model"
      @change="$emit('update:model', $event.target.checked)"
      v-bind="$attrs"
    />
  </div>
  <label class="form-check-label" :for="id" v-bind="labelAttrs">
    {{ label }}
  </label>
  <div class="invalid-feedback">{{ invalidMsg }}</div>
  <div class="valid-feedback">{{ validMsg }}</div>
</template>

<style scoped lang="sass"></style>
