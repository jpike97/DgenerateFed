<template>
	<div class="user-detail">
   <h1>{{user.id}}</h1>
   <p>{{user.units}}</p>
	</div>
</template>
<script>
import "@/scss/_variables.scss";
import UserDetailService from "@/services/UserDetailService";
//TODO: run ajax after page load? prevent spinny

export default {
	name: "UserDetail",
	data: function () {
		return {
			user: {}
		};
	},
	mounted() {
		this.getUserDetail();
	},
	methods: {
		async getUserDetail() {
			let userID = this.$route.params.id;
			console.log(userID);
			//userID = userID.toUpperCase();
			const response = await UserDetailService.fetchUserDetail(userID);
			console.log(response);
			this.user = response.data.user[0];
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
</style>