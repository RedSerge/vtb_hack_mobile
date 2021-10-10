<template>

  <v-window :value='window' vertical class='fill-height' touchless>
    <v-window-item value='finish' class='fill-height'>
      <v-container class='d-flex flex-column align-stretch fill-height'>
        <top-bar />

        <div class='flex-grow-1 d-flex flex-column justify-center align-center pa-4'>
          <img src='@/assets/images/winner.png' width='80%' style='border-radius: 50%'>

          <p class='mt-8 text-h5 text-center'>
            Ура! Вы прошли игру!
          </p>
        </div>

        <div class='d-flex'>
          <v-btn rounded x-large color='primary' class='ma-4 flex-grow-1' @click='isDialogVisible = true'>Играть
            дальше
          </v-btn>
        </div>

        <v-dialog
          v-model='isDialogVisible'
          max-width='290'
        >
          <v-card>
            <v-card-title class='text-h5'>

            </v-card-title>

            <v-card-text>
              <div class='text-body-2'>Чтобы получить дополнительную попытку, установи приложение</div>
              <a
                href='https://play.google.com/store/apps/details?id=ru.vtb.invest&referrer=af_tranid%3DMoX85WUPdclLeqQvZA1f5w%26shortlink%3D3bc4a15%26pid%3DQR_code%26c%3Dsite_googleplay'
                class='d-flex align-center mt-4' target='_blank'>
                <img src='@/assets/icons/vtb.svg' width='48px'>
                <span class='ml-4 text-subtitle-2'>ВТБ Мои Инвестиции</span>
              </a>
            </v-card-text>

            <v-card-actions>
              <v-spacer></v-spacer>

              <v-btn
                color='primary darken-1'
                text
                @click='isDialogVisible = false; window = "stats"'
              >
                Закрыть
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-container>
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
      window: 'main',
      isDialogVisible: false
    }
  },

  mounted() {
    this.$root.$on('change-window', this.changeWindow)
  },

  methods: {
    start() {
      window.location.href = '/welcome'
    },

    changeWindow(window) {
      this.window = window
    }

  }
}
</script>

