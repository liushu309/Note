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
    
### 6.2 

