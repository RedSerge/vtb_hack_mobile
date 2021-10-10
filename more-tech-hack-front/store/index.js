export const state = () => ({
  user: {
    token: localStorage.getItem('user-token'),
    status: {
      money: 0,
      statistics: [],
      history: []
    }
  }
})

export const getters = {
  userToken(state) {
    return state.user.token
  }
}

export const mutations = {
  setUserToken(state, payload) {
    state.user.token = payload
    localStorage.setItem('user-token', payload)
  },

  setUserStatus(state, payload) {
    state.user.status = {
      ...state.user.status,
      ...payload
    }
  }
}
