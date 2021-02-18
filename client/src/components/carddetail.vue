<template>
	<div class="card-detail">
		<div class="card-detail__currentprice">
		<h2>Current Mentions</h2>
		<p>{{card.numMentions}}</p>
		<p>{{card.previousNumMentions}}</p>
		</div>
		<div class="news">
			<h2>News</h2>
			<div class="news__wrapper" v-for="newsArticle in news" :key="newsArticle.id">
				<h3>
				<a target="_blank" :href='newsArticle[1]'> {{ newsArticle[0] }} </a>
				</h3>
				<h3 v-if="news == undefined">
					No News... woah
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

export default {
	name: "carddetail",
	data: function () {
		return {
			card: {},
			news: []
		};
	},
	mounted() {
		this.getCardDetail();
		this.getCardNews();//trick to look faster? fade in news?
		
		
	},
	methods: {
		async getCardDetail() {
			let cardID = this.$route.params.id;
			console.log(cardID);
			//cardID = cardID.toUpperCase();
			const response = await CardDetailService.fetchCardDetail(cardID);
			console.log(response);
			this.card = response.data.card[0];
		},
		async getCardNews() {
			let cardID = this.$route.params.id;
			const response = await NewsService.fetchNewsByID(cardID);
			this.news = response.data.news;
			console.log("this is news");
			console.log(this.news);
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
		padding-top: 40px;
	}
}
</style>
