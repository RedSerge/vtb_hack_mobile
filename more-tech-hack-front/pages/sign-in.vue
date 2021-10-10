<template>
  <v-container fluid class='fill-height'>
    <v-row justify='center'>
      <v-col class='ma-8'>
        <v-img :src='logoPath' max-width='180px' class='mx-auto mb-12' />

        <v-alert v-show='error' type='error'>
          {{ error }}
        </v-alert>

        <v-text-field v-model='email' outlined label='Email' />

        <v-text-field v-model='password' type='password' outlined label='Пароль' />

        <v-btn block x-large color='primary' @click='signIn'>Войти</v-btn>

        <div class='text-center ma-4'>
          <NuxtLink to='/sign-up'>
            Создать аккаунт
          </NuxtLink>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import logo from '@/assets/images/logo.png'

export default {
  layout: 'guest',

  data() {
    return {
      email: 'demo',
      password: 'demo',
      error: null,
      logoPath: logo
    }
  },

  methods: {
    async signIn() {
      try {
        const token = await this.$api.userSignIn({
          email: this.email,
          password: this.password
        })

        this.$store.commit('setUserToken', token)
        await this.$router.push('/welcome')
      } catch (e) {
        this.error = e.message
      }
    }
  }
}
</script>

