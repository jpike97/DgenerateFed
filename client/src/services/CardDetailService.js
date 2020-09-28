import Api from '@/services/Api'

export default {
  fetchCards () {
    return Api().get('cards')
  }
}