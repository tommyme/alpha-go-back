- model 转换成json
  - 可以调用values方法 但是不实用
  - 自定义model 然后 _meta.fields

- get sanic app instance

## 账号和密码
- admin:root
- aaa:root

## 发送websocket 
- 读取cookie sessid 拿到用户信息
- 读取发送目标 也就是消息发向谁

## cookie注意事项
- axios需要配置
- 如果要使用cookie的话, 跨域头不能是*
- login的时候 axios 不配置credEnable 就设置不了cookie
- get message的时候 axios不配置 cred 就发送不出去cookie
- 切换到别的页面 ws还是有心跳包

内置 配置 cors
https://sanic.dev/en/plugins/sanic-ext/configuration.html#manual-extend
config.cors = True 表示使用cors机制


## 数据库迁移指南
```shell
# 初始化 使用这条命令来建立数据库，而不是使用tortoise
aerich init-db
# migrate
aerich migrate --name test
# upgrade
aerich upgrade
# downgrade
aerich downgrade
```

## 数据库初始化指南
- 插入文章
- 插入bilibili账号 2051617240 525952604 526645204
- 添加{userId: index, userName: "官方客服", password: "not available"} 账号