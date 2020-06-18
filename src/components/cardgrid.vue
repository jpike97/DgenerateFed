<template>
  <div class="cardgrid">
      <h1>Card Grid Test</h1>
    <div class="card" v-for="card in cards" :key="card.title">
        {{card.msg}}
    </div>
    </div>
</template>

<script>
import store from '@/store/index.js'

export default {
  name: 'cardgrid',
  data: function () {
    return {
      cardTitle: ''
    }
  },
  computed:  {  
    count() { 
      return store.state.message;
    },
    cards() { 
        return store.state.cards;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
