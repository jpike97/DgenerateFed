<template>
  <div class="nav">
      <nav class="desktop">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/rando">Rando</router-link>
      </nav>
      <nav class="mobile-tray">
      <h1>DGENERATE!</h1>
      <div class="mobile-slideout">
      <router-link to="/">Home</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/rando">Rando</router-link>
      </div>
      </nav>
  </div>
</template>

<script>

export default {
  name: 'home',
  data: function() {
return { 
    avgColor: ''
  };
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
nav { 
  padding: 1rem 0rem;

  &.desktop { 
    display: none;
    @media (min-width: $screen-lg) { 
      display: block;
    }
  a { 
    margin-right: 6rem;
    font-family: 'F37 Ginger',Helvetica,Arial,sans-serif;
    font-weight: 700;
    letter-spacing: .3px;
    position: relative;
    text-decoration: none;
    font-size: 1.75rem;
    color: $white;


        &:after {
          content: '';
          position: absolute;
          bottom: -0.5rem;
          left: 50%;
          transform: translateX(-50%);
          width: 0%;
          height: 2px;
          background: $white;
          transition: width 0.25s $ease-in-quad;
        }

        &:hover,
        &:active,
        &:focus,
        &.active,
        &.router-link-exact-active {
          &:after {
            width: 100%;
            transition: width 0.25s $ease-out-quad;
          }
        }

    &:last-of-type { 
      margin-right: 0;
    }
  }
}
&.mobile-tray { 
  display: block;
  @media (min-width: $screen-lg) { 
    display: none;
  }
  h1 { 
    color: $white;
    margin: 0rem;
  }
  .mobile-slideout { 
    position: absolute;
    z-index: 1;
    display: block;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    visibility: hidden;
    padding-top: 4rem;
    background-color: black;
    transform: translateX(-100%);
    transition: transform 0.25s $ease-in-quad, visibility .25s;
    &.active { 
      visibility: visible;
      transform: translateX(0%);
      transition: transform 0.25s $ease-out-quad, visibility .25s ease 0s;
      -webkit-overflow-scrolling: touch;
    }
  }
}

}
</style>