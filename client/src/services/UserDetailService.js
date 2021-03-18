import Api from '@/services/Api'

export default {
  fetchUserDetail(id) {
    return Api().get("users/" + id)
  }
}