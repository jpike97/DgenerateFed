<template>
  <div class="stock-graph">
    <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
      <defs>
        <filter id="shadow" height="600" width="600" filterUnits="userSpaceOnUse">
          <feGaussianBlur in="SourceAlpha" stdDeviation="3" result="coloredBlur" />
          <feOffset dx="2" dy="2" result="offsetblur" />
          <feMerge>
            <feMergeNode in="coloredBlur" />
            <feMergeNode in="SourceGraphic" />
          </feMerge>
        </filter>
      </defs>
      <line class="key-anim1" x1="0" y1="25" x2="25" y2="15" stroke="green" filter="url(#shadow)" />

      <!-- If you do not specify the stroke
      color the line will not be visible-->
    </svg>
  </div>
</template>

<script>
//import jQuery from "jquery";
//let $ = jQuery;
export default {
  name: 'stockgraph',
  data: function() {
},
	mounted() {
	},
computed: {
},
methods:  {
}
}
</script>
<style lang="scss" scoped>
@import "@/scss/_variables.scss";

.stock-graph {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.key-anim1 {
  -webkit-animation: Drawpath 1s linear forwards;
  animation: Drawpath 1s linear forwards;
  stroke-dasharray: 0, 100;
}
.key-anim2 {
  -webkit-animation: Drawpath 1s linear 1s forwards;
  animation: Drawpath 1s linear 1s forwards;
  stroke-dasharray: 0, 100;
}
.key-anim3 {
  -webkit-animation: Drawpath 1s linear 2s forwards;
  animation: Drawpath 1s linear 2s forwards;
  stroke-dasharray: 0, 100;
}

@-webkit-keyframes Drawpath {
  from {
    stroke-dasharray: 0, 100;
  }
  to {
    stroke-dasharray: 100, 100;
  }
}
@keyframes Drawpath {
  from {
    stroke-dasharray: 0, 100;
  }
  to {
    stroke-dasharray: 100, 100;
  }
}
</style>


