<template>
  <v-app>
    <v-main>
      <Nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  middleware: ['check-auth'],

  async created() {
    this.$store.commit('setUserStatus', await this.$api.userStatus())

    this.$root.$on(
      'update-status',
      async () => this.$store.commit('setUserStatus', await this.$api.userStatus())
    )
  }
}
</script>
