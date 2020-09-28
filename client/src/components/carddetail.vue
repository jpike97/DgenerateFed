<template>
	<div class="card-detail">
    </div>
</template>
<script>
import "@/scss/_variables.scss";
import CardsService from "@/services/CardsService";
import jQuery from "jquery";
let $ = jQuery;

export default {
	name: "carddetail",
	data: function () {
		return {
			card: {}
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
		async getCardDetail() {
			const response = await CardDetailService.fetchCards();
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
