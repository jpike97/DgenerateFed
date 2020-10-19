<template>
  <div class="home">
    <div class="testing" style="background-color: white;">
    <home />
    </div>
    <cardgrid />
  </div>
</template>

<script>
// @ is an alias to /src
//TODO: get rid of home component doesn't make a lot of sense
import cardgrid from '@/components/cardgrid.vue'
import home from '@/components/home.vue'

export default {
  name: 'Home',
  components: {
    cardgrid,
    home
  }
}
</script>
