# ansible和playbook简单配置进行远程操作
## 安装ansible
- 环境 python 3.5.0
- 命令 
```python
pip install ansible
```
- 配置hosts /etc/ansible/hosts
```bash
[wxnacy]
100.201.193.62 ansible_ssh_pass=your_pass ansible_ssh_user=your_name #use password
[prod]
prod.server.org ansible_ssh_user=your_name ansible_ssh_private_key_file=key_path # use ssh private key
```
## 配置playbook
配置deploy.yml完成进入远程服务器的某个目录并执行git pull操作
```bash
- hosts: wxnacy # 在/etc/ansible/hosts 中配置的服务器名
  remote_user: login_name # 登陆用户
  tasks:
  - name: cd path and git pull # 命令名称
    shell: git pull # 执行命令
    args:
      chdir: /www/wxnacy.github.io # 进入目录
```

## 运行
```bash
ansible-playbook deploy.yml
```

