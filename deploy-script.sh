#!/bin/bash
apt update
apt install -y python3-pip unzip
pip3 install flask

# Скачиваем проект из Object Storage
aws --endpoint-url=https://storage.yandexcloud.net \
  s3 cp s3://my-bucket/project.zip project.zip
unzip project.zip -d /home/ubuntu/project
cd /home/ubuntu/project

# Устанавливаем зависимости и запускаем приложение
pip3 install -r requirements.txt
nohup python3 app.py &
