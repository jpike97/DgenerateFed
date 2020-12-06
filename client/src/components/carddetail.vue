<template>
	<div class="card-detail">
		<div class="card-detail__currentprice">
		<h2>Current Price</h2>
		<p>{{ card.currentPrice }}</p>
		</div>
		<div class="news">
			<h2>News</h2>
			<div class="news__wrapper" v-for="newsArticle in news" :key="newsArticle.id">
				<h3>
				<a target="_blank" :href='newsArticle.link'> {{ newsArticle.title }} </a>
				</h3>
			</div>
		</div>
	</div>
</template>
<script>
import "@/scss/_variables.scss";
import CardDetailService from "@/services/CardDetailService";
import NewsService from "@/services/NewsService";
//TODO: run ajax after page load? prevent spinny
import jQuery from "jquery";
let $ = jQuery;

export default {
	name: "carddetail",
	data: function () {
		return {
			card: {},
			news: [],
			newsLoaded: false
		};
	},
	mounted() {
		this.getCardDetail();
		let self = this;
		//trick to look faster? fade in news?
		setTimeout(function(){ 
		console.log("blah");
		self.getCardNews();
		self.newsLoaded = true;
		}, 1500);
		
	},
	methods: {
		async getCardDetail() {
			let cardID = this.$route.params.id;
			console.log(cardID);
			//cardID = cardID.toUpperCase();
			const response = await CardDetailService.fetchCardDetail(cardID);
			console.log(response);
			this.card = response.data.card[0];
			this.card.currentPrice = this.card.currentPrice.toFixed(2);
		},
		async getCardNews() {
			let self = this;
			let cardID = this.$route.params.id;
			NewsService.fetchNews(cardID, function (result, data) {
				if (result == true) {
					console.log("success!");
					console.log(data.items);
					self.news = data.items;
					self.newsLoaded = true;
					//show the loaded news
					$('.news').addClass('newsLoaded');
				}
			});
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
	color: $white;
	text-decoration: none;
	&:hover { 
		text-decoration: underline;
	}
}
.card-detail {

	.news { 
		opacity: 0;
		padding-top: 40px;
		&.newsLoaded  { 
			opacity: 1;
			transition: opacity .5s ease-in-out;
		}
	}
}
</style>
