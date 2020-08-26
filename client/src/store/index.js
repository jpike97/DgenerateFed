import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    message: 'helloThere!',
    cards: [ {
      title: 'Card 1',
      msg: 'Card1 Message' 

    },
    { 
      title: 'Card 2',
      msg: 'Card2 Message'
    },

    ]

  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
