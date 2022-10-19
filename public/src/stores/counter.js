import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', {
  state: () => {
    return {
      count: 0
    };
  },
  actions: {
    increment() {
      this.count ++;
    }
  },
  computed: {
    doubleCount() {
      return this.count.value * 2
    }
  }
})
