<template>
  <div id="userinfo">
    <h1>我的信息</h1>
    <img :src="'http://127.0.0.1:9000/upload/'+userinfo.headImg" alt />
    <div>{{ changeNickName}}</div>
    <div>身份:管理员</div>
    <input v-model=" changeNickName" />
    <button @click="ChangeEvent">修改</button>
  </div>
</template>

<script>
import { eventBus } from "../main.js";
export default {
  data() {
    return {
      userinfo: {},
      changeNickName: ""
    };
  },
  mounted() {
    this.getUserinfo();
  },
  methods: {
    getUserinfo() {
      console.log("开始获取用户信息");
      this.userinfo = this.$store.state.userinfo;
    },
    ChangeEvent() {
      this.userinfo.nickName = this.changeNickName;
      eventBus.$emit("changeTestName", this.changeNickName);
    }
  }
};
</script>
<style>
#userinfo {
  margin-bottom: 10px;
}
</style>