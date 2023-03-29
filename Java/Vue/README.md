## 1. 安装
官网下载nodejs，配置好PATH环境变量好，即可以使用node与npm
    
    node -v
    npm -v
### 1.1 没有node_modeles，安装依赖文件
    
    npm i (or npm install)

## 2. node安装vue包
    
    npm install -g @vue/cli

## 3. 创建一个工程 

    vue create [工程名]

选择相关的选项即可

## 4. vue项目
MVC: M:App{data:{}, function:{}}, V: "el" or "#app", C: Vue，createApp? 

## 5. 组件的使用
### 5.1 在xxx.vue文件中进行局部注册
在<script>标签下，需要导入和注册两个步骤：

    <script>
    // 在对应的文件夹下「导入」组件，components
    import HelloWorld from './components/HelloWorld.vue'
    // script里面必需要有export。与外面的import是对应的
    export default {
      // 当前文件组件名
      name: 'App',
      // 
      props:['titles']
      // 注册组件名，已经写好的组件名称
      components: {
        HelloWorld
      },
      data:function(){
        return:{
                title:"小金刚"
            }
      },
      methons{
          
        }
        
    }
    </script>

### 5.2 在main.js文件中进行全局注册  
    一般在使用第三方成熟的组件的时候，可以使用全局注册，只需要使用app.use就可以了
    
    // main.ts
    import { createApp } from 'vue'
    import ElementPlus from 'element-plus'
    import 'element-plus/dist/index.css'
    import App from './App.vue'

    const app = createApp(App)
    // 
    app.use(ElementPlus)
    app.mount('#app')
    
## 6. elements-ui使用
### 6.1 安装
-S: 表示将安装的信息记录到package.json
    npm i element-ui -S
    
### 6.2 全局注册
    //vue 3.x
    app.use(ElementPlus)
    //vue 2.x
    Vue.use(ElementPlus)


## 7. VueRouter
Vue适合做单页面的项目，VueRouter用来控制不同组件的显示，比如components目录下的xxx.vue文件，设定不同组件和路径的映射
### 7.1 安装
    npm install vue-router@3

### 7.2 使用简介
    App.vue
    <!-- 声明路由链接 -->
    <router-link to="/discover">发现音乐</router-link>
    <!-- 声明路由占位标签 -->
    <router-view></router-view>
    
    ├── components
    │   └── HelloWorld.vue
    └── router
        └── index.js
    router文件中的index.js
    import VueRouter from "Vue-router";
    import Vue from "vue";
    import Discover from "../components/Discover.vue"
    Vue.use(VueRouter)
    
    // 2. 定义路由
    // 每个路由应该映射一个组件。 其中"component" 可以是
    // 通过 Vue.extend() 创建的组件构造器，
    // 或者，只是一个组件配置对象。
    // 我们晚点再讨论嵌套路由。
    const routes = new VueRouter(
        routers:[
            { path: '/discover', component: Discover },
            <!-- 重定向 -->
            { path: '/', redirect: Discover}
        ]
    )

    export default router
    
    
    
    <!-- main.js -->
    import Vue from 'vue'
    import App from './App.vue'
    import router from "./router"

    Vue.config.productionTip = false

    new Vue({
      render: h => h(App),
      <!-- 添加了这一行 -->
      router:router 
    }).$mount('#app')

