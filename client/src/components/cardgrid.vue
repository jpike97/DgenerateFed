<template>
	<div class="cardgrid">
		<h1>Card Grid Test</h1>
		<div class="card__wrapper" v-for="card in cards" :key="card.id">
      <div class="card__header">
       <img src="@/assets/logo.png" />
	   <div class="card__header-info">
       <h2>{{card.ticker}}</h2>
	   <h3>{{card.currentPrice}}</h3>
	   </div>
	</div>
	<div class="card__comments">
		
	</div>
	</div>
	</div>
</template>
<script>
import "@/scss/_variables.scss";
import PostsService from "@/services/CardsService";
import jQuery from 'jquery'
let $ = jQuery

console.log($(".flip-container"));



export default {
	name: "cardgrid",
	data: function () {
		return {
			cards: []
		};
	},
	mounted() {
    this.getCards();
    $(document).on("click",".flip-container", function() {
        console.log(this);
        $(this).toggleClass('flip-container-clicked');
    });
    
	},
	methods: {
		async getCards() {
			const response = await PostsService.fetchCards();
			this.cards = response.data;
		}
	}
};
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
.card {
	&-test {
    position: relative;
		@media (min-width: $screen-md) {
			border: 1xp solid red;
		}
	}
}


</style>
