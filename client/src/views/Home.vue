<template>
  <div class="home">
    <cardgrid />
  </div>
</template>

<script>
// @ is an alias to /src
//TODO: get rid of home component doesn't make a lot of sense
import cardgrid from '@/components/cardgrid.vue'
export default {
  name: 'Home',
  components: {
    cardgrid,
  }
}
</script>
