## 初始化数据
### 将数据写入redis geo指定的key中
> python -m Server initinit

## 启动服务
### 启动web服务
> python -m Server run

### 访问地址
> http://127.0.0.1:8080/api/report?latitude=-112.073843&longitude=33.447999&radius=1

> http://127.0.0.1:8080/api/report/park?latitude=-112.073843&longitude=33.447999&radius=1