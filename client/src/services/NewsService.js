import Api from '@/services/Api'

export default {
  fetchNewsByID(id) {
    return Api().get("news/" + id)
  }
}