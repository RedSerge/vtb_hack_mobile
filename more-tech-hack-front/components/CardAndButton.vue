<template>
  <div class='d-flex flex-column fill-height flex-nowrap' :class='$style.root'>
    <v-card class='flex-grow-1 ma-4 mt-8 pa-8' :class='$style.card'>
      <v-card-text class='text-center'>
        Купить акции компании "ЭнерджиСолюшен"?
      </v-card-text>

      <v-slider
        v-model="slider"
        class="align-center"
        :max="100"
        :min="10"
        hide-details
      >
        <template #append>
          <v-text-field
            v-model="slider"
            class="mt-0 pt-0"
            hide-details
            single-line
            type="number"
            style="width: 60px"
          ></v-text-field>
        </template>
      </v-slider>
    </v-card>

    <div
      v-touch='{
        up: () => $emit("change-window", "stats")
      }'
      class='d-flex justify-space-between px-4 pt-8 pb-8'
      :class='$style.actions'
    >
      <v-btn color='primary' rounded x-large :class='$style.action'>Продать</v-btn>
      <v-btn color='primary' rounded x-large :class='$style.action'>Купить</v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CardAndButton',

  props: {
    actions: {
      type: Array,
      default: () => [],
    }
  },

  data() {
    return {
      slider: 0
    }
  },

  methods: {
    swipeUp() {
      console.log('swipe down')
    }
  }
}
</script>

<style lang='scss' module>
@import "~vuetify/src/styles/settings/variables";

.root {
  padding: $container-padding-x;
}

.card {
  border-radius: 12 * $spacer !important;
}

.actions {
  gap: $grid-gutter;
}

.action {
  flex-grow: 1;
}
</style>
