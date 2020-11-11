<template>
	<div class="cardgrid">
		<h1>Card Grid Test</h1>
		<div class="cardgrid__cards">
			<div class="card__wrapper" v-for="card in cards" :key="card.id">
				<a :href="'/cards/' + card.ticker" class="card__header">
					<div class="card__header-info">
						<h2>{{ card.ticker }}</h2>
						<h3>{{ card.currentPrice.toFixed(2) }}</h3>
						<h3>{{ card.numMentions }}</h3>
					</div>
				</a>
			</div>
		</div>
	</div>
</template>
<script>
import "@/scss/_variables.scss";
import CardsService from "@/services/CardsService";
import jQuery from "jquery";
let $ = jQuery;

export default {
	name: "cardgrid",
	data: function () {
		return {
			cards: []
		};
	},
	mounted() {
		this.getCards();
		$(document).on("click", ".flip-container", function () {
			console.log(this);
			$(this).toggleClass("flip-container-clicked");
		});
	},
	methods: {
		async getCards() {
			const response = await CardsService.fetchCards();
			console.log(response);
			this.cards = response.data.cards.filter(function (card) {
				return card.currentPrice != null;
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
	color: #42b983;
	text-decoration: none;
}
.cardgrid {
	&__cards {
		display: flex;
		flex-flow: wrap;
		justify-content: center;
		align-items: center;
		max-width: 1160px;
		margin: 0 auto;
		text-align: center;
		margin-top: 3rem;
	}
}
.card {
	&-test {
		position: relative;
		@media (min-width: $screen-md) {
			border: 1xp solid red;
		}
	}
	&__wrapper {
		background-color: #1a1a19;
		color: #d4d3cd;
		width: 350px;
		margin: 0px 1rem;
		margin-bottom: 3rem;
		cursor: pointer;
	}
	&__header { 
		&-info { 
			padding: 2rem 0;
		}
	}
}
</style>
