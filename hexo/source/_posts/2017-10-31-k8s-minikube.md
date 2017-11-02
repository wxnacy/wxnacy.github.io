---
title: k8s-minikube
date: 2017-10-31 11:32:57
tags:
---

## 安装
### macOS
```bash
brew cask install minikube
```
### Linux
```bash
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
    && chmod +x minikube \
    && sudo mv minikube /usr/local/bin/
```

## xhyve 驱动
```bash
brew install docker-machine-driver-xhyve
sudo chown root:wheel $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
sudo chmod u+s $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve
```

## kubectl
```bash
brew install kubectl
```



