import Api from '~/api/Api'

export default function({ $axios, store }, inject) {
  inject('api', new Api($axios, store.getters.userToken))
}
