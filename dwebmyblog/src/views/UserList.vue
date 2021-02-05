<template>
  <div id="userlist">
    <div v-for="item in imgList" :key="item.pk" class="user">
      <img :src="apiurl+'upload/'+item.headImg" alt />
      <p>{{item.nickName}}</p>
      <button @click="deleteUser(item.id)">删除</button>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Qs from "qs";
export default {
  data() {
    return {
      apiurl: "http://127.0.0.1:9000/",
      imgList: [],
      menuId: 1
    };
  },
  //用户在看到页面之前,最后vue提供的一次函数执行
  mounted() {
    this.getUserList(this.menuId);
  },
  watch: {
    $route(to) {
      console.log(to);
      this.menuId = to.query.menuId;
      this.getUserList(this.menuId);
    }
  },
  methods: {
    //开始获取学生分类列表
    getUserList(id) {
      axios({
        url: "http://127.0.0.1:9000/get-user-list",
        type: "json",
        params: { id },
        method: "get"
      }).then(res => {
        this.imgList = res.data;
      });
    },
    deleteUser(id) {
      axios({
        url: "http://127.0.0.1:9000/get-user-list",
        type: "json",
        data: Qs.stringify({ id }),
        method: "delete",
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
      }).then(res => {
        if (res.data == "ok") {
          this.getUserList(this.menuId);
        }
        console.log(res);
      });
    }
  }
};
</script>
<style>
</style>