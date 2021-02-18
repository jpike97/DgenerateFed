<template>
	<div class="cardgrid">
		<h1>What's Trending?</h1>
		<div class="cardgrid__cards">
			<div
				class="card__wrapper"
				:class="card.numMentions > 100 ? 'wow' : ''"
				v-for="card in cards"
				:key="card.id"
			>
				<a :href="'/cards/' + card.ticker" class="card__header">
					<div class="card__header-info">
						<h2>{{ card.ticker }}</h2>
						<h3>{{ card.numMentions }} mentions</h3>
						<h3 class="percent" :class="calculatePercentChange(card.previousNumMentions, card.numMentions) > 0 ? 'positive' : ''">{{calculatePercentChange(card.previousNumMentions, card.numMentions)}}% change</h3>
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
			this.cards = response.data.cards;
		},
		calculatePercentChange(prevMentions, currentMentions) { 
			var change = prevMentions - currentMentions;
			var perChange = (change / prevMentions) * 100;
			return perChange.toFixed(2);
		}
	}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "@/scss/_variables.scss";
h3 {
	margin: 40px 0 0;
	&.percent { 
	color: red;
	&.positive { 
		color: green;
	}
	}

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
	h1 {
		margin-top: 20px;
	}
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
		border-radius: 15px;
		border: 1px solid #1a1a19;
		transition: transform 0.25s ease-in-out;
		&:hover {
			transform: scale(1.1);
			transition: transform 0.25s ease-in-out;
			border: 1px solid #42b983;
		}

		&.wow {
			animation: pulse 5s infinite;

		}
	}
	&__header {
		&-info {
			padding: 2rem 0;
			h3 {
			}
		}
	}
}

@keyframes pulse {
	0% {
		border: 2px solid red
	}

	50% {
		border: 2px solid blue;
	}

	100% {
		border: 2px solid red;
	}
}
</style>
