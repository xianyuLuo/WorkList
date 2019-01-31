# 任务分配系统
Docker镜像地址： xianyuluo/worklist:{version}

# 快速启动
docker-compose编排
```yaml
version: '2'
services:
  worklist:
    image: xianyuluo/worklist:1.0.0
    network_mode: host
    entrypoint:
      - /worklist/entrypoint.sh
    restart: always
    environment:
      - DATABASE_NAME=worklist
      - DATABASE_USER=root
      - DATABASE_PASSWORD=xxxxx
      - DATABASE_HOST=127.0.0.1
      - DATABASE_PORT=3306  
```

# 需求列表
* 邮件通知
  
  定时查看归属于自己的job，如果没完成的，邮件通知

* 任务转交（伪需求 ）

  a用户把任务转交给b用户

* 权限控制（伪需求 ）

   每个人只能看见自己创建的任务