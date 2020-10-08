<template>
  <div class="carddetail">
  <cardgrid />
  </div>
</template>

<script>
// @ is an alias to /src
import cardgrid from '@/components/carddetail.vue'
export default {
  name: 'Home',
  components: {
    cardgrid
  }
}
</script>
