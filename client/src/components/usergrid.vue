<template>
	<div class="usergrid">
		<h1>What's Trending?</h1>
		<div class="usergrid__users">
			<div
				class="user__wrapper"
				v-for="user in users"
				:key="user.id"
			>
			<h1>{{user.id}}</h1>
			<p>{{user.units}}</p>
			</div>
		</div>
	</div>
</template>
<script>
import "@/scss/_variables.scss";
import UsersService from "@/services/UsersService";

export default {
	name: "usergrid",
	data: function () {
		return {
			users: []
		};
	},
	mounted() {
		this.getUsers();
	},
	methods: {
		async getUsers() {
			const response = await UsersService.fetchUsers();
			this.users = response.data.users;
		}
	}
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang="scss" scoped>
@import "@/scss/_variables.scss";
</style>
