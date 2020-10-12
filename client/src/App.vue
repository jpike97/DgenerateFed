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
  background-color: black;
  margin: 0;
  padding: 0rem;
}
h1, h2, h3, h4, h5, h6, p { 
  margin: 0;
}
</style>
