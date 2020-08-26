<template>
  <div class="cardgrid">
      <h1>Card Grid Test</h1>
    <div class="card-test" v-for="card in cards" :key="card.id">
        {{card.name}}
    </div>
    </div>
</template>
<script>
import '@/scss/_variables.scss';
import PostsService from '@/services/CardsService'

export default {
  name: 'cardgrid',
  data: function () {
    return {
      cards: []
    }
  },
  mounted () {
    this.getCards()
  },
  methods: {
    async getCards () {
      const response = await PostsService.fetchCards()
      this.cards = response.data
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import '@/scss/_variables.scss';
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
.card { 
  &-test { 
      @media(min-width: $screen-md) { 
        border: 1xp solid red;
      }
  }
}
</style>
