## 1. 安装
官网下载nodejs，配置好PATH环境变量好，即可以使用node与npm
    
    node -v
    npm -v

## 2. node安装vue包
    
    npm install -g @vue/cli

## 3. 创建一个工程 

    vue create [工程名]

选择相关的选项即可

## 4. vue项目
MVC: M:App{data:{}, function:{}}, V: "el" or "#app", C: Vue，createApp? 

## 5. 组件的使用
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
