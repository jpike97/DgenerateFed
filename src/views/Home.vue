<template>
  <div class="home">
    <home />
    <cardgrid />
  </div>
</template>

<script>
// @ is an alias to /src
import home from '@/components/home.vue'
import cardgrid from '@/components/cardgrid.vue'

export default {
  name: 'Home',
  components: {
    home, 
    cardgrid
  }
}
</script>
