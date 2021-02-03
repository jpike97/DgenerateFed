<template>
  <div class="hello">
    <!-- <h1>{{ msg }}</h1>
    <div class="avgImg" v-bind:style="{backgroundColor: avgColor}">
    </div>-->
  </div>
</template>

<script>
import store from '@/store/index.js'
import BizPicService from "@/services/BizPicService";
export default {
  name: 'home',
  data: function () {
    return {
      msg: 'testing 123',
      bizPic: {},
      avgColor: ''
    }
  },
  computed:  {  
    count() { 
      return store.state.message;
    }
  }, 
  mounted() { 
    console.log("ah la la");
    this.getBizImage();
  },
  methods: {
      getAvgColors(bizPicData) {
      let h = bizPicData.HSVavg[0];
      let s = bizPicData.HSVavg[1];
      let v = bizPicData.HSVavg[2];
      this.avgColor = "hsl(" + h + ", " + s + "%, " + v + "%)";
    },
    async getBizImage() {
      console.log("Getting biz image");
      const response = await BizPicService.fetchBizPic();
      console.log(response);
      this.bizPic = response.data.snap[0];
      console.log(this.bizPic);
      this.getAvgColors(response.data.snap[0]);
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

