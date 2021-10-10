export default function({ store, redirect, route }) {
  if (!store.state.user.token) {
    redirect('/sign-in')
  }
}
