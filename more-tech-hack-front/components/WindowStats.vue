<template>
  <v-container class='d-flex flex-column align-stretch'>
    <div class='flex-grow-1 d-flex justify-center pa-4'>
      <v-btn @click='$root.$emit("change-window", "main")'>
        вернуться к игре
      </v-btn>
    </div>

    <div>
      <v-subheader>Изменения капитала</v-subheader>

      <v-sparkline
        fill
        smooth
        show-labels
        :value='user.status.statistics'
      />
    </div>

    <div>
      <v-subheader>История</v-subheader>

      <div :class='$style.history' class='d-flex flex-column pa-2'>
        <div
          v-for='item in user.status.history'
          :key='item.text'
          :class='$style["history-item"]'
          class='d-flex'
        >
          <span :class='$style.date'>{{ item.date }}</span>
          <span>{{ item.text }}</span>
        </div>
      </div>
    </div>

    <div>
      <v-subheader>Продукты</v-subheader>
      <div class='d-flex flex-column' :class='$style.cards'>

        <v-card elevation='4' class='px-4 py-6' :class='$style["bg-one"]'>
          <a href='https://school.vtb.ru/materials/courses/pervye-shagi-na-birzhe/' target='_blank'
             class='white--text text-decoration-none'>
            Онлайн курс по инвестициям
          </a>
        </v-card>

        <v-card elevation='2' class='px-4 py-6' :class='$style["bg-two"]'>
          <a href='https://www.vtb.ru/personal/investicii/akcii/' target='_blank'
             class='black--text text-decoration-none'>
            Выгодная покупка акций
          </a>
        </v-card>

        <v-card elevation='2' class='px-4 py-6' :class='$style["bg-three"]'>
          <a href='https://www.vtb.ru/personal/investicii/iis/' target='_blank'
             class='white--text text-decoration-none'>
            Особый счёт для инвестиций
          </a>
        </v-card>
      </div>
    </div>

  </v-container>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'WindowStats',

  computed: {
    ...mapState(['user'])
  }
}
</script>

<style lang='scss' module>
@import "~vuetify/src/styles/settings/variables";

.history {
  gap: 4 * $spacer;
}

.history-item {
  gap: 4 * $spacer;
}

.date {
  color: darkgrey;
  flex-basis: 15%;
}

.cards {
  padding: 2 * $spacer;
  gap: 4 * $spacer;
}

.bg-one {
  background: #136a8a; /* fallback for old browsers */
  background: linear-gradient(to left, #267871, #136a8a); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}

.bg-two {
  background: #DAD299; /* fallback for old browsers */
  background: linear-gradient(to left, #B0DAB9, #DAD299); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

}

.bg-three {
  background: #c21500;  /* fallback for old browsers */
  background: linear-gradient(to left, #ffc500, #c21500); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
}
</style>
