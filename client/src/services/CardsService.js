import Api from '@/services/Api'

export default {
  fetchCardDetail(id) {
    return Api().get("cards/" + id)
  }
}