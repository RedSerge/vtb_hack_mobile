<template>
  <v-window :value='window' vertical class='fill-height' touchless>
    <v-window-item value='main' class='fill-height'>
      <window-game />
    </v-window-item>

    <v-window-item value='stats' class='fill-height'>
      <window-stats />
    </v-window-item>
  </v-window>
</template>

<script>
export default {
  data() {
    return {
      window: 'main'
    }
  },

  mounted() {
    this.$root.$on('change-window', this.changeWindow)
  },

  methods: {
    changeWindow(window) {
      this.window = window
    }
  }
}
</script>
