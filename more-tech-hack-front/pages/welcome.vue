<template>
  <v-container class='d-flex flex-column align-stretch fill-height'>
    <top-bar />

    <div class='flex-grow-1 d-flex flex-column justify-center pa-4'>
      <p class='text-h3'>
        Привет!
      </p>

      <img src='@/assets/images/welcome.png' width='80%' class='my-2'>

      <p>
        В этой игре ты научишься управлять своими
        финансами и не бояться ивестировать
      </p>
    </div>

    <div class='d-flex'>
      <v-btn x-large color='primary' rounded class='ma-4 flex-grow-1' @click='$router.push("/game")'>Начать</v-btn>
    </div>
  </v-container>
</template>

<script>
export default {}
</script>

