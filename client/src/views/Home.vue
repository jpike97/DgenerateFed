<template>
  <div class="home">
    <div class="testing" style="background-color: white;">
    </div>
    <usergrid />
  </div>
</template>

<script>
// @ is an alias to /src
//TODO: get rid of home component doesn't make a lot of sense
import usergrid from '@/components/usergrid.vue'

export default {
  name: 'Home',
  components: {
    usergrid
  }
}
</script>
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
.avgImg { 
  height: 500px;
  width: 100%;
  max-width: 600px;
}
</style>