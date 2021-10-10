<template>
  <v-app>
    <v-main>
      <Nuxt />
    </v-main>
  </v-app>
</template>

<script>
export default {
  middleware({ store, redirect }) {
    if (store.state.user.token) {
      redirect('/')
    }
  }
}
</script>
