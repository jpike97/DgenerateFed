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
