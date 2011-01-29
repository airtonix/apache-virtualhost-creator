#!/bin/sh
sudo mkdir $VIRTUALHOST_ROOT -p
cd $VIRTUALHOST_ROOT

sudo django-admin startproject project

sudo mkdir ./cgi-bin
sudo touch ./cgi-bin/django.wsgi

sudo mkdir ./db
sudo touch ./db/database.sqlite3
sudo chmod 775 ./db/database.sqlite3

sudo mkdir ./logs/django -p
sudo touch ./logs/django/errors.log
sudo touch ./logs/django/debug.log
sudo touch ./logs/django/access.log
sudo touch ./logs/django/requests.log


sudo chown $VIRTUALHOST_OWNER_USER:$VIRTUALHOST_OWNER_GROUP ./ -R

