<template>
  <div id="login">
    <div id="loginbox">
      <div class="form">
        <div class="item">
          <div v-if="target==3" class="span">网站名:</div>
          <input v-if="target==3" v-model="sitename" type="text" placeholder="请输入网站名" />
        </div>
        <div v-if="target==1||target==2" class="item">
          <div class="span">用户名:</div>
          <input v-model="username" type="text" placeholder="请输入用户名" />
        </div>
        <div v-if="target==1||target==2" class="item">
          <div class="span">密码:</div>
          <input v-model="password" type="text" placeholder="请输入密码" />
        </div>
        <div class="item">
          <div v-if="target==2" class="span">确认密码:</div>
          <input v-if="target==2" v-model="password2" type="text" placeholder="请输入密码" />
        </div>
        <div class="item">
          <div v-if="target==3" class="span">图片</div>
          <input
            v-if="target==3"
            id="uploadLogo"
            @change="ImgChange($event)"
            type="file"
            style="width:70px"
          />
        </div>
        <div>
          <img v-if="target==3" :src="testlogo" />
        </div>
        <button v-if="target==1" @click="toLogin">登录</button>
        <button v-if="target==2" @click="toRegistor">注册</button>
        <button v-if="target==3" @click="toUpload">确定</button>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import Qs from "qs";
export default {
  name: "LoginBox",
  props: ["target"],
  data() {
    return {
      username: "",
      password: "",
      password2: "",
      sitename: "",
      testlogo: "",
      loginType: false
    };
  },
  mounted() {
    console.log(this.target);
  },
  methods: {
    //缓存logo
    ImgChange(e) {
      var logo = e.target.files[0];
      var formdata = new FormData();
      formdata.append("logo", logo);
      // 上传图片
      axios({
        url: "http://127.0.0.1:9000/uploadlogo/",
        method: "post",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        data: formdata
      }).then(res => {
        if (res.data) {
          this.testlogo = "http://127.0.0.1:9000/upload/" + res.data.img;
        }
      });
    },
    //上传sitename
    toUpload() {
      // 网站名称修改
      var sitename = this.sitename;
      var logo = this.testlogo;
      if (sitename.length > 0 && logo.length > 0) {
        axios({
          url: "http://127.0.0.1:9000/uploadlogo/",
          method: "put",
          headers: { "Content-Type": "application/x-www-form-urlencoded" },
          data: Qs.stringify({
            sitename,
            logo
          })
        }).then(res => {
          if (res.data == "ok") {
            window.location.reload();
          }
        });
      } else {
        alert("没有新的标题或图片");
      }
    },
    //登录
    toLogin() {
      var username = this.username;
      var password = this.password;
      if (username.length > 0 && password.length > 0) {
        axios({
          url: "http://127.0.0.1:9000/login/",
          type: "json",
          data: Qs.stringify({
            username,
            password
          }),
          method: "post",
          headers: { "Content-Type": "application/x-www-form-urlencoded" }
        }).then(res => {
          console.log(res);
          switch (res.data) {
            case "none":
              alert("无用户");
              break;
            case "密码错误":
              alert("密码错误");
              break;
            default:
              // 储存token
              window.localStorage.setItem("token", res.data.token);
              //储存vuex中的用户信息
              // window.localStorage.setItem("userinfo", res.data.userinfo);
              //储存vuex中的用户信息
              var userinfo = res.data.userinfo;
              this.$store.commit("editUserinfo", userinfo);
              alert("登录成功");
              if (this.$route.path != "/userinfo") {
                this.$router.push({ path: "/userinfo" });
              }
            // 刷新页面
            // window.location.reload();
          }
        });
      } else {
        alert("用户名或密码为空");
      }
      this.$emit("childEvent");
    },
    //注册
    toRegistor() {
      var username = this.username;
      var password = this.password;
      var password2 = this.password2;
      if (username.length > 0 && password.length > 0 && password2.length > 0) {
        if (password != password2) {
          alert("两次输入密码不一致");
        } else {
          axios({
            url: "http://127.0.0.1:9000/registor/",
            type: "json",
            data: Qs.stringify({
              username,
              password,
              password2
            }),
            method: "post",
            headers: { "Content-Type": "application/x-www-form-urlencoded" }
          }).then(res => {
            console.log(res);
            switch (res.data) {
              case "same":
                alert("存在同名用户");
                break;
              case "ok":
                alert("注册成功");
                break;
            }
          });
        }
      } else {
        alert("输入存在空值");
      }
      this.$emit("childEvent");
    }
  }
};
</script>
<style>
#login {
  position: absolute;
  top: 0;
  width: 700px;
  height: 100vw;
  display: flex;
  justify-content: center;
  align-items: center;
}
#loginbox {
  width: 300px;
  height: 300px;
  border: 1px solid #000;
  background: #00000090;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #fff;
}
#loginbox .form .item {
  font-weight: 700;
  margin: 10px auto;
}
#loginbox .form .item .span {
  float: left;
  width: 80px;
}
</style>