#include <GL/glew.h>  
#include <GLFW/glfw3.h>  
#include <vector>
#include <iostream>

// 顶点着色器源代码  R:可以不用写换行符\
const GLchar* vertexShaderSource = R"glsl(  
#version 330 core  
layout (location = 0) in vec3 aPos;  
layout (location = 1) in vec3 aColor;  
out vec3 ourColor;  
  
void main()  
{  
    gl_Position = vec4(aPos, 1.0);  
    ourColor = aColor;  
}  
)glsl";

// 片段着色器源代码  
const GLchar* fragmentShaderSource = R"glsl(  
#version 330 core  
out vec4 FragColor;  
in vec3 ourColor;  
  
void main()  
{  
    FragColor = vec4(ourColor, 1.0);  
}  
)glsl";

// 创建着色器  
GLuint createShader(const GLchar* shaderSource, GLenum shaderType) {
	GLuint shader = glCreateShader(shaderType);
	glShaderSource(shader, 1, &shaderSource, NULL);
	glCompileShader(shader);

	int success;
	GLchar infoLog[512];
	glGetShaderiv(shader, GL_COMPILE_STATUS, &success);
	if (!success) {
		glGetShaderInfoLog(shader, 512, NULL, infoLog);
		std::cerr << "Shader compilation failed: " << infoLog << std::endl;
		glDeleteShader(shader);
		return 0;
	}

	return shader;
}

// 链接着色器程序  
GLuint linkShader(GLuint vertexShader, GLuint fragmentShader) {
	GLuint shaderProgram = glCreateProgram();
	glAttachShader(shaderProgram, vertexShader);
	glAttachShader(shaderProgram, fragmentShader);
	glLinkProgram(shaderProgram);

	int success;
	GLchar infoLog[512];
	glGetProgramiv(shaderProgram, GL_LINK_STATUS, &success);
	if (!success) {
		glGetProgramInfoLog(shaderProgram, 512, NULL, infoLog);
		std::cerr << "Shader linking failed: " << infoLog << std::endl;
		glDeleteProgram(shaderProgram);
		return 0;
	}

	glDeleteShader(vertexShader);
	glDeleteShader(fragmentShader);
	return shaderProgram;
}

int main() {
	// 初始化GLFW  
	if (!glfwInit()) {
		std::cerr << "Failed to initialize GLFW" << std::endl;
		return -1;
	}

	glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3);
	glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3);
	glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE);
	glfwWindowHint(GLFW_RESIZABLE, GL_FALSE);

	GLFWwindow* window = glfwCreateWindow(800, 600, "OpenGL with GLFW and GLEW", NULL, NULL);
	if (!window) {
		std::cerr << "Failed to create GLFW window" << std::endl;
		glfwTerminate();
		return -1;
	}
	glfwMakeContextCurrent(window);

	// 初始化GLEW  
	if (glewInit() != GLEW_OK) {
		std::cerr << "Failed to initialize GLEW" << std::endl;
		return -1;
	}

	// 创建着色器  
	GLuint vertexShader = createShader(vertexShaderSource, GL_VERTEX_SHADER);
	GLuint fragmentShader = createShader(fragmentShaderSource, GL_FRAGMENT_SHADER);
	GLuint shaderProgram = linkShader(vertexShader, fragmentShader);

	// 获取着色器中变量的位置  
	GLint posAttribLocation = glGetAttribLocation(shaderProgram, "aPos");
	GLint colAttribLocation = glGetAttribLocation(shaderProgram, "aColor");

	// 创建并绑定VAO  
	GLuint VAO;
	glGenVertexArrays(1, &VAO);
	glBindVertexArray(VAO);

	// 创建并填充顶点缓冲  
	std::vector<GLfloat> vertices = {
		-0.5f, -0.5f,0.0f, 1.0f, 0.0f, 0.0f,
		0.5f, -0.5f, 0.0f, 0.0f, 1.0f, 0.0f,
		0.0f, 0.5f, 0.0f, 0.0f, 0.0f, 1.0f
	};

	GLuint VBO;
	glGenBuffers(1, &VBO);
	glBindBuffer(GL_ARRAY_BUFFER, VBO);
	glBufferData(GL_ARRAY_BUFFER, vertices.size() * sizeof(GLfloat), &vertices[0], GL_STATIC_DRAW);

	// 设置顶点属性指针  
	glEnableVertexAttribArray(posAttribLocation);
	glVertexAttribPointer(posAttribLocation, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), (GLvoid*)0);
	glEnableVertexAttribArray(colAttribLocation);
	glVertexAttribPointer(colAttribLocation, 3, GL_FLOAT, GL_FALSE, 6 * sizeof(GLfloat), (GLvoid*)(3 * sizeof(GLfloat)));



	// 主循环  
	while (!glfwWindowShouldClose(window)) {
		// 处理输入  
		if (glfwGetKey(window, GLFW_KEY_ESCAPE) == GLFW_PRESS) {
			glfwSetWindowShouldClose(window, GL_TRUE);
		}

		// 清除屏幕和深度缓冲区  
		glClearColor(0.2f, 0.3f, 0.3f, 1.0f);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

		// 使用着色器程序  
		glUseProgram(shaderProgram);

		// 绘制三角形  
		glBindVertexArray(VAO);
		glDrawArrays(GL_TRIANGLES, 0, 3);

		// 交换缓冲区  
		glfwSwapBuffers(window);

		// 处理事件  
		glfwPollEvents();
	}

	// 清理  
	glDeleteVertexArrays(1, &VAO);
	glDeleteBuffers(1, &VBO);
	glDeleteProgram(shaderProgram);

	glfwTerminate();
	return 0;
}
