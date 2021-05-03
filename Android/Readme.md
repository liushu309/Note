## 1. 运行时权限
android6.0以上添加了运行时权限

## 2. AndroidManifest.xm文件
    //注意后面的camera是大写的,小
    <uses-permission android:name="android.permission.CAMERA">

## 3. SnackBar
    // 注意是先setContentView,再findViewByid,才能在SnackBar中使用,不然报
        setContentView(R.layout.activity_main);
        mLayout = findViewById(R.id.main_layout);
