FROM jenkins/jenkins:lts

USER root

# Установка необходимых пакетов
RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg2 \
    software-properties-common

# Добавление ключа и репозитория Docker
RUN curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    apt-key fingerprint 0EBFCD88 && \
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"

# Установка Docker CLI
RUN apt-get update && apt-get install -y docker-ce-cli

# Переключение на пользователя Jenkins
USER jenkins

# Установка плагинов Jenkins
RUN jenkins-plugin-cli --plugins "blueocean docker-workflow"
