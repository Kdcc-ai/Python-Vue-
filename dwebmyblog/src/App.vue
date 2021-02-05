<template>
  <div id="home">
    <button v-if="loginType==false" @click="showLoginBox(1)">登录</button>
    <button v-if="loginType==false" @click="showLoginBox(2)">注册</button>
    <button v-if="loginType" @click="toHome()">首页</button>
    <button v-if="loginType" @click="toUserInfo()">个人中心</button>
    <button v-if="loginType" @click="showLoginBox(3)">修改</button>
    <div class="header">
      <h1>{{siteDate[0].title}}</h1>
      <img :src="siteDate[0].logo " />
    </div>
    <hr />
    <div class="content">
      <!-- 导航栏 -->
      <div class="menu">
        <div class="item" v-for="item in menuList" :key="item.id">
          <div v-if="item.id==choosed" style="background:#777;color: #fff">
            <a style="color:#fff">{{item.text}}</a>
          </div>
          <div v-else @click="chooseMenu(item.id)">
            <a style="color:#000">{{item.text}}</a>
          </div>
        </div>
      </div>
      <!-- 用户列表 -->
      <div class="userlist">
        <p>{{choosed_text}}</p>
        <hr />
        <router-view></router-view>
      </div>
    </div>
    <hr />
    <LoginBox v-if="boxtarget" :target="boxtarget" @childEvent="parentMethod"></LoginBox>
    <div class="foot">Copyright@ 2020Dweb工作室</div>
  </div>
</template>
<script>
import axios from "axios";
import LoginBox from "../src/components/LoginBox.vue";
export default {
  components: {
    LoginBox
  },
  data() {
    return {
      menuList: [],
      siteDate: {},
      choosed: 1,
      choosed_text: "Django后端",
      boxtarget: 0,
      loginType: false
    };
  },
  mounted() {
    this.getMenuList();
    try {
      if (window.localStorage.getItem("token").length > 0) {
        this.loginType = true;
      }
    } catch (error) {
      console.log(error);
    }
  },
  methods: {
    //跳转到个人中心
    toUserInfo() {
      this.$router.push({ path: "/userinfo" });
    },
    //跳转到首页
    toHome() {
      this.$router.push({ path: "/" });
    },
    //获取分类列表以及网站信息
    getMenuList() {
      axios({
        url: "http://127.0.0.1:9000/get-menu-list",
        type: "json",
        method: "get"
      }).then(res => {
        // console.log(res);
        // 获取课程分类列表
        this.menuList = res.data.menu_data;
        // 获取网站信息
        this.siteDate = res.data.site_data;
        console.log(this.siteDate[0]);
        // console.log(this.siteDate);
        this.siteDate[0].logo =
          "http://127.0.0.1:9000/upload/" + this.siteDate[0].logo;
      });
    },
    chooseMenu(id) {
      this.choosed = id;
      for (let i = 0; i < this.menuList.length; i++) {
        if (id == this.menuList[i].id) {
          this.choosed_text = this.menuList[i].text;
        }
      }
      //进行id传参跳转
      this.$router.push({ path: "/", query: { menuId: id } });
    },
    showLoginBox(value) {
      this.boxtarget = value;
    },
    parentMethod() {
      this.boxtarget = 0;
    }
  }
};
</script>
<style>
</style>
