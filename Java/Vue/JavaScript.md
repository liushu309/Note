## 1. 箭头函数  
1. 可能javascript写函数的时候，与一般的语言，如C++，java相比，会多用到一个关键字function。所以箭头函数看起来主要省略了function这个关键字  

        // 箭头函数
        let fun = (name) => {
            // 函数体
            console.log(name)
        };
        // 等同于
        let fun = function (name) {
            // 函数体
            console.log(name)
        };

2. 关于箭头函数的参数  
如果箭头函数没有参数，直接写一个空括号即可  
若参数只有一个，也可以省去包裹参数的括号  
若有多个参数，将参数依次用“，”隔开，包裹在括号中即可  

        // 没有参数
        let fun1 = () => {
            console.log(666);
        };
        // 只有一个参数，可以省去参数括号
        let fun2 = name => {
            console.log(`Hello ${name} !`)
        };
        // 有多个参数
        let fun3 = (val1, val2, val3) => {
            return [val1, val2, val3];
        };

3. 关于箭头函数的函数体  
如果函数体只有一句代码，简单的返回某个变量或者返回一个简单的js表达式，可以省去大括号{}

        let f = val => val;
        // 等同于
        let f = function (val) { return val };

        let sum = (num1, num2) => num1 + num2;
        // 等同于
        let sum = function(num1, num2) {
          return num1 + num2;

4. 如果函数体只有一条语句并且不需要返回值（如：调用一个函数），可以给这个语句前面加一个void关键字

        let fn = () => void doesNotReturn();
