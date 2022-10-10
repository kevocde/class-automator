<script>
export default {
  data() {
    return {
      activeClass: 'active'
    }
  }
}
</script>

<template>
  <nav class="container-fluid navigator d-flex justify-content-center">
      <ul class="btn-group shadow-sm p-0 m-0 navigator-list">
        <li class="btn btn-lg fs-6 px-4 py-2 navigator-item" @click="$router.push('/')">
          <RouterLink to="/" active-class="active" class="navigator-item-link">Agendar</RouterLink>
        </li>
        <li class="btn btn-lg fs-6 px-4 py-2 navigator-item" @click="$router.push('/list')">
          <RouterLink to="/list" active-class="active" class="navigator-item-link">Visualizar</RouterLink>
        </li>
      </ul>
  </nav>
</template>

<style scoped lang="sass">
  @import "~bootstrap/scss/bootstrap-utilities.scss"

  .navigator
    .navigator-list
      list-style: none

      .navigator-item
        background-color: $white

        &:hover
          background-color: $indigo-300

          .navigator-item-link
            color: $white

        &:has(.navigator-item-link.active)
          background-color: $indigo-400

          .navigator-item-link
            color:  $white

        .navigator-item-link
          text-decoration: none
          color: $text-muted
</style>
