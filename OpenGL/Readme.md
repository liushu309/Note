## 1. 安装
    sudo apt-get install build-essential
    #sudo apt-get install libgl1-mesa-dev
    #sudo apt-get install libglu1-mesa-dev
    #sudo apt-get install mesa-common-dev libgl1-mesa-dev libglu1-mesa-dev freeglut3-dev
安装PowerVRSDKSetup-2018_R2.run-x64, 一路默认
下载地址：https://www.imgtec.com/developers/powervr-sdk-tools/installers/　　
参考　https://blog.csdn.net/c_china/article/details/86364918　　

    export LD_LIBRARY_PATH=/opt/Imagination/PowerVR_Graphics/PowerVR_Tools/PVRVFrame/Library/Linux_x86_64/

如果提示：“gl\glew.h”: No such file or directory
    sudo apt-cache search glew
    sudo apt-get install xxx

### 1.1 示例

$vi light.cpp

        /* light.c
         此程序利用GLUT绘制一个OpenGL窗口，并显示一个加以光照的球。
         */
         /* 由于头文件glut.h中已经包含了头文件gl.h和glu.h，所以只需要include 此文件*/
         # include <GL/glut.h>
         # include <stdlib.h>

         /* 初始化材料属性、光源属性、光照模型，打开深度缓冲区 */
         void init ( void )
         {
           GLfloat mat_specular [ ] = { 1.0, 1.0, 1.0, 1.0 };
             GLfloat mat_shininess [ ] = { 50.0 };
             GLfloat light_position [ ] = { 1.0, 1.0, 1.0, 0.0 };

             glClearColor ( 0.0, 0.0, 0.0, 0.0 );
             glShadeModel ( GL_SMOOTH );

             glMaterialfv ( GL_FRONT, GL_SPECULAR, mat_specular);
             glMaterialfv ( GL_FRONT, GL_SHININESS, mat_shininess);
             glLightfv ( GL_LIGHT0, GL_POSITION, light_position);

             glEnable (GL_LIGHTING);
             glEnable (GL_LIGHT0);
             glEnable (GL_DEPTH_TEST);
         }

         /*调用GLUT函数，绘制一个球*/
         void display ( void )
         {
             glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
             glutSolidSphere (1.0, 40, 50);
             glFlush ();
         }


         /* 定义GLUT的reshape函数，w、h分别是当前窗口的宽和高*/
         void reshape (int w, int h)
         {
             glViewport (0, 0, (GLsizei) w, (GLsizei) h);
             glMatrixMode (GL_PROJECTION);
             glLoadIdentity ( );
             if (w <= h)
                 glOrtho (-1.5, 1.5, -1.5 * ( GLfloat ) h / ( GLfloat ) w, 1.5 * ( GLfloat ) h / ( GLfloat ) w, -10.0, 10.0 );
             else
                 glOrtho (-1.5 * ( GLfloat ) w / ( GLfloat ) h, 1.5 * ( GLfloat ) w / ( GLfloat ) h, -1.5, 1.5, -10.0, 10.0);
             glMatrixMode ( GL_MODELVIEW );
             glLoadIdentity ( ) ;
         }


         /* 定义对键盘的响应函数 */
         void keyboard ( unsigned char key, int x, int y)
         {
             /*按Esc键退出*/
             switch (key) 
             {
                 case 27:
                 exit ( 0 );
                 break;
             }
         }


         int main(int argc, char** argv)
         {
             /* GLUT环境初始化*/
             glutInit (&argc, argv);
             /* 显示模式初始化 */
             glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH);
             /* 定义窗口大小 */
             glutInitWindowSize (300, 300);
             /* 定义窗口位置 */
             glutInitWindowPosition (100, 100);
             /* 显示窗口，窗口标题为执行函数名 */
             glutCreateWindow ( argv [ 0 ] );
             /* 调用OpenGL初始化函数 */
             init ( );
             /* 注册OpenGL绘图函数 */
             glutDisplayFunc ( display );
             /* 注册窗口大小改变时的响应函数 */
             glutReshapeFunc ( reshape );
             /* 注册键盘响应函数 */
             glutKeyboardFunc ( keyboard );
             /* 进入GLUT消息循环，开始执行程序 */
             glutMainLoop( );
             return 0;
         }

编译

    g++ light.cpp -o sample -lglut -lGL -lGLU
./sample

### 1.2 cmake工程示例
源文件
        #include <glad/glad.h>
        #include <GLFW/glfw3.h>

        #include <iostream>

        void framebuffer_size_callback(GLFWwindow* window, int width, int height);
        void processInput(GLFWwindow *window);

        // settings
        const unsigned int SCR_WIDTH = 800;
        const unsigned int SCR_HEIGHT = 600;

        int main()
        {
            // glfw: initialize and configure
            // ------------------------------
            glfwInit();
            glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
            glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
            glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);

        #ifdef __APPLE__
            glfwWindowHint(GLFW_OPENGL_FORWARD_COMPAT, GL_TRUE);
        #endif

            // glfw window creation
            // --------------------
            GLFWwindow* window = glfwCreateWindow(SCR_WIDTH, SCR_HEIGHT, "LearnOpenGL", NULL, NULL);
            if (window == NULL)
            {
                std::cout << "Failed to create GLFW window" << std::endl;
                glfwTerminate();
                return -1;
            }
            glfwMakeContextCurrent(window);
            glfwSetFramebufferSizeCallback(window, framebuffer_size_callback);

            // glad: load all OpenGL function pointers
            // ---------------------------------------
            if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress))
            {
                std::cout << "Failed to initialize GLAD" << std::endl;
                return -1;
            }    

            // render loop
            // -----------
            while (!glfwWindowShouldClose(window))
            {
                // input
                // -----
                processInput(window);

                // render
                // ------
                glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
                glClear(GL_COLOR_BUFFER_BIT);

                // glfw: swap buffers and poll IO events (keys pressed/released, mouse moved etc.)
                // -------------------------------------------------------------------------------
                glfwSwapBuffers(window);
                glfwPollEvents();
            }

            // glfw: terminate, clearing all previously allocated GLFW resources.
            // ------------------------------------------------------------------
            glfwTerminate();
            return 0;
        }

        // process all input: query GLFW whether relevant keys are pressed/released this frame and react accordingly
        // ---------------------------------------------------------------------------------------------------------
        void processInput(GLFWwindow *window)
        {
            if(glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS)
                glfwSetWindowShouldClose(window, true);
        }

        // glfw: whenever the window size changed (by OS or user resize) this callback function executes
        // ---------------------------------------------------------------------------------------------
        void framebuffer_size_callback(GLFWwindow* window, int width, int height)
        {
            // make sure the viewport matches the new window dimensions; note that width and 
            // height will be significantly larger than specified on retina displays.
            glViewport(0, 0, width, height);
        }

CMakeLists.txt

        cmake_minimum_required(VERSION 3.9.1)

        project(opengl)

        # glad
        include_directories(/usr/local/OpenGL/glad/include)
        add_library(GLAD SHARED /usr/local/OpenGL/glad/src/glad.c)

        # glfw3
        find_path(GLFW3_INCLUDE_DIR NAME "GLFW/glfw3.h")
        include_directories(GLFW3_INCLUDE_DIR)
        find_library(GLFW3_LIBRARY NAMES glfw glfw3)

        # 执行文件
        add_executable(cleargl hello_window_clear.cpp)

        # 链接文件
        target_link_libraries(cleargl GLAD ${GLFW3_LIBRARY})
