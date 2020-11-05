<template>
  <div class="nav">
      <nav class="desktop">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <!-- <router-link to="/rando">Rando</router-link> -->
      </nav>
      <nav class="mobile-tray">
      <div class="mobile-nav__header">
      <h1>Dgenerate!</h1>
      <button class="hamburger hamburger--collapse" type="button">
      <span class="hamburger-box">
      <span class="hamburger-inner"></span>
      </span>
      </button>
      </div>
 
      <div class="mobile-slideout">
        <div class="mobile-nav__wrapper">
        <router-link to="/">Home</router-link>
        <router-link to="/about">About</router-link>
      </div>
      <!-- <router-link to="/rando">Rando</router-link> -->
      </div>
      </nav>
  </div>
</template>

<script>
import jQuery from "jquery";
let $ = jQuery;
export default {
  name: 'home',
  data: function() {
return { 
    avgColor: ''
  };
},
	mounted() {
		$(document).on("click", ".hamburger", function () {
      $('.hamburger').toggleClass('is-active');
      $('.mobile-slideout').toggleClass('active');
		});
	},
computed: {
},
methods:  {
}
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "@/scss/_variables.scss";
@import "@/scss/_nav.scss";
@import "@/scss/third-party/hamburgers/hamburgers.scss";
</style>