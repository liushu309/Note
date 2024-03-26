# 配置
1. ## 安装glfw和glew
右键项目->属性->VC++目录->包含目录写，库目录写  
链接器->输入->附加依赖项->glfw3.lib  
glfw3_mt.lib  
glfw3dll.lib  
glew32.lib  
glew32s.lib  
opengl32.lib  
注意，最后一定要单独加上opengl32.lib

## 2. 简单用例流程

             glBufferData              glVertexAttribPointer        glBindVertexArray
CPU Data--------------------->GPU VBO------------------------->VAO---------------------->Shader  
  glUseProgram  
-------------------> glDrawArrays------->CPU glfwSwapBuffers


