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
    // 1. 在对应的文件夹下「导入」组件，components
    import HelloWorld from './components/HelloWorld.vue'
    // script里面必需要有export。与外面的import是对应的
    export default {
      // 当前文件组件名
      name: 'App',
      // 
      props:['titles']
      // 2. 注册组件名，已经写好的组件名称
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
声明式调用
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
            { path: '/discover', component: Discover, children: {
                path:'xxx', component:'child_name'}},
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


编程式调用

    router.push(...)
    ...
        this.$router.push('movie/${id}')
    ...


## 8 Vuex
    用于组件之间数据的转递。父组件和子组件可以通过props传递，但是兄弟组件不可以这样。
### 8.1 安装
    
    npm install vuex@next

### 8.2 使用
每个Vuex核心都是一个store全局对象  

    // Vue store主要由以下机制组成：
    // 1. State：存储应用程序的状态数据。
    // 2. Getters：从state中派生出一些状态，类似于计算属性。
    // 3. Mutations：修改state的唯一途径，且必须是同步函数。
    // 4. Actions：用于提交mutations，可以包含任意异步操作。
    // 5. Modules：将store分割成模块，每个模块拥有自己的state、getters、mutations和actions。
  
    // 首先，导入Vue和Vuex
    import Vue from 'vue'
    import Vuex from 'vuex'

    // 然后，通过调用Vue.use(Vuex)来使用Vuex
    Vue.use(Vuex)

    // 创建一个新的store实例
    const store = new Vuex.Store({
      state: {
        count: 0
      },
      mutations: {
        increment (state) {
          state.count++
        }
      },
      actions: {
        incrementAsync ({ commit }) {
          setTimeout(() => {
            commit('increment')
          }, 1000)
        }
      },
      getters: {
        doubleCount: state => {
          return state.count * 2
        }
      }
    })

    // 可以通过调用this.$store从任何组件访问存储
    // 例如，要增加计数，可以调用this.$store.commit('increment')
    // 要异步增加计数，可以调用this.$store.dispatch('incrementAsync')
    // 要获取双倍计数，可以调用this.$store.getters.doubleCount

    // 请注意，mutations必须是同步的，而actions可以是异步的。 
    // 还要注意，可以使用模块将存储拆分为更小、更可管理的部分。



    // commit是Vuex中一个用于提交mutation的方法，它的主要作用是修改state中的数据。 
    // commit接收一个mutation的type作为参数，以及一个可选的payload，它会同步地修改state中的数据。 

    // dispatch是Vuex中一个用于分发action的方法，它的主要作用是触发action中的异步操作，最终提交mutation来修改state。 
    // dispatch接收一个action的type作为参数，以及一个可选的payload，它会返回一个Promise，可以在异步操作完成后进行处理。 

    // getters是Vuex中一个用于从state中派生出一些状态的方法，类似于计算属性。 
    // getters接收state作为第一个参数，可以接收其他getter作为第二个参数，以及根state作为第三个参数。 
    // getters可以被用于计算state的派生状态，以及在组件中进行数据筛选和计算。

    // 以下是一个Vue Store中的modules使用例子：
    const moduleA = {
      state: { count: 0 },
      mutations: {
        increment (state) {
          state.count++
        }
      },
      actions: {
        incrementAsync ({ commit }) {
          setTimeout(() => {
            commit('increment')
          }, 1000)
        }
      },
      getters: {
        doubleCount (state) {
          return state.count * 2
        }
      }
    }

    const moduleB = {
      state: { message: 'Hello' },
      mutations: {
        updateMessage (state, newMessage) {
          state.message = newMessage
        }
      },
      actions: {
        updateMessageAsync ({ commit }, newMessage) {
          setTimeout(() => {
            commit('updateMessage', newMessage)
          }, 1000)
        }
      },
      getters: {
        upperCaseMessage (state) {
          return state.message.toUpperCase()
        }
      }
    }

    const store = new Vuex.Store({
      modules: {
        a: moduleA,
        b: moduleB
      }
    })

    // 在组件中使用moduleA的双倍计数getter：
    this.$store.getters['a/doubleCount']

    // 在组件中使用moduleB的大写消息getter：
    this.$store.getters['b/upperCaseMessage']

    // 在组件中分发moduleA的异步操作：
    this.$store.dispatch('a/incrementAsync')

    // 在组件中提交moduleB的同步操作：
    this.$store.commit('b/updateMessage', 'New message')

## 9 Mock
    // 使用mockjs来模拟数据
    const Mock = require('mockjs');

    // 定义数据模板
    const data = Mock.mock({
    'list|1-10': [{
        'id|+1': 1,
        'name': '@name',
        'age|18-60': 1,
        'gender|1': ['男', '女'],
        'email': '@email'
    }]
    });

    // 输出模拟数据
    console.log(data); 

    // 在请求数据时，使用axios或fetch等工具发送请求，并将返回的数据替换为模拟数据即可完成前端mock的使用

### 9.1 Mock.js和XHRHttpRequest的区别
Mock.js和XHRHttpRequest在前端开发中有着不同的作用。  

Mock.js是一款前端数据模拟工具，可以帮助开发者模拟数据接口，快速进行前端开发和调试。而XHRHttpRequest是一个内置的JavaScript函数，用于创建XMLHttpRequest对象，可以向服务器发送HTTP请求并接收响应。通常用于异步数据交换，如使用AJAX技术更新网页内容而不刷新整个页面，从而提高用户体验、性能和响应时间。  

在实际开发中，我们可以使用Mock.js模拟数据接口，然后使用XHRHttpRequest发送HTTP请求获取模拟数据，从而进行前端开发和调试。这样可以避免直接请求后端接口，提高开发效率和安全性。  

### 9.2 XHRHttpRequest的使用步骤
    
1. 创建一个XHR对象，使用open()方法指定HTTP请求的类型、URL和是否异步处理请求。  
2. 发送请求，使用send()方法向服务器发送请求。  
3. 监听XHR对象的readyState和status属性变化，以便在接收到响应时采取适当的操作。  
4. 处理响应，使用responseText、responseXML或response属性访问服务器响应的数据。  

    
            // 创建一个XMLHttpRequest对象
            var xhr = new XMLHttpRequest(); 

            // 指定请求方式和请求地址
            xhr.open('GET', '/api/data', true);

            // 发送请求
            xhr.send();

            // 监听请求状态变化
            xhr.onreadystatechange = function() {
                if (xhr.readyState === 4 && xhr.status === 200) {
                    // 请求成功后的操作
                    console.log(xhr.responseText);
                }
            };

