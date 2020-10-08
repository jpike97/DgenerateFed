<template>
	<div class="card-detail-blah">
		<span>testing testing testing</span>
		<p>{{card.ticker}}</p>
		<a href="/cards/NIO">Link link</a>
    </div>
</template>
<script>
import "@/scss/_variables.scss";
import CardDetailService from "@/services/CardDetailService";

export default {
	name: "carddetail",
	data: function () {
		return {
			card: {}
		};
	},
	mounted() {
		this.getCardDetail();
	},
	methods: {
		async getCardDetail() {
			let cardID = this.$route.params.id;
			cardID = cardID.toUpperCase();
			const response = await CardDetailService.fetchCardDetail(cardID);
			this.card = response.data;
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
