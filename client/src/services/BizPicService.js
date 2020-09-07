import Api from '@/services/Api'

export default {
  fetchBizPic () {
    return Api().get('bizpic')
  }
}