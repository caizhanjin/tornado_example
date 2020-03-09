# 项目说明

```
pip install -r requirements.txt

python server.py
```

## 项目结构
tornado项目实践方案
有参考：[github地址](https://github.com/baqmxdsny/tornado_demo)

```
│  README.md               # 项目说明
│  requirements.txt        # 所需依赖库
│  server.py               # 运行入口
│  setting.py              # 配置
│  urls.py                 # 项目路由设置
├─handlers                 # ***处理逻辑和路由映射，C控制层
│      base.py             # 处理基类
├─libs                     # 库文件，中间层的封装（解耦合）
│  └─db
├─logs                     # 日志文件存放
├─models                   # ***M模型层，包括：数据库，文件系统，第三放服务
├─media                    # 一些媒体资源
└─utils                    # 工具类，比如：验证码生成、IP地址转换

```

根据项目需要，可能还包含文件夹：
+ docs（项目文档/说明）
+ static（静态文件，存放js 、css 、html、img）
+ templates（模板，放html页面）
