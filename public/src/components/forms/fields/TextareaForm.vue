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
};
</script>

<template>
  <label class="form-label" :for="id" v-bind="labelAttrs">{{ label }}</label>
  <textarea
    class="form-control"
    :id="id"
    :value="model"
    @input="$emit('update:model', $event.target.value)"
    v-bind="$attrs"
  />
  <div class="invalid-feedback">{{ invalidMsg }}</div>
  <div class="valid-feedback">{{ validMsg }}</div>
</template>

<style scoped lang="sass"></style>
