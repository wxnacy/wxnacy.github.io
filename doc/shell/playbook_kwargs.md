# ansible-playbook命令向playbook.yml文件传递参数
> 在playbook.yml配置文件实际应用中，很多情况需要通过外部命令行向文件中传值，以达到业务需求

现在有一个playbook.yml文件，想要完成进入某个目录并完成部署任务，host和执行命令中的参数tag_name 需要外部传值
```bash
- hosts: '{{host}}'
  tasks:
  - name: deploy
    shell: ./deploy_api.sh '{{tag_name}}'
    args:
      chdir: ~/path

```

现在可以通过三种方式进行传值：
- key=value
```bash
ansible-playbook playbook.yml --extra-vars "host=xxx tag_name=xxx"
```

- json格式
```bash
ansible-playbook playbook.yml --extra-vars "{'host':'xxx','tag_name':'xxx'}"
```
- jaon文件
```bash
ansible-playbook playbook.yml --extra-vars "kwargs.json"
```

