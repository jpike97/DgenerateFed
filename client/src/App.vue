<template>
  <div id="app">
    <Navigation></Navigation>
    <router-view/>
  </div>
</template>

<script>
import nav from './components/nav'
export default {
  name: 'app',
  components: {
    'Navigation': nav
  }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

body { 
  background-color: #090003;
  margin: 0;
  padding: 1rem;
}
</style>
