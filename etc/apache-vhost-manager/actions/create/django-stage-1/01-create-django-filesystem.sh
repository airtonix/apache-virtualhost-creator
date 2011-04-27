#!/bin/sh
sudo mkdir $VIRTUALHOST_ROOT -p
cd $VIRTUALHOST_ROOT

sudo mkdir $VIRTUALHOST_ROOT/cgi-bin
sudo touch $VIRTUALHOST_ROOT/cgi-bin/django.wsgi

sudo mkdir $VIRTUALHOST_ROOT/db
sudo touch $VIRTUALHOST_ROOT/db/database.sqlite3
sudo chmod 775 $VIRTUALHOST_ROOT/db/database.sqlite3

sudo touch $VIRTUALHOST_ROOT/logs/django-errors.log
sudo touch $VIRTUALHOST_ROOT/logs/django-debug.log
sudo touch $VIRTUALHOST_ROOT/logs/django-access.log
sudo touch $VIRTUALHOST_ROOT/logs/django-requests.log

sudo mkdir $VIRTUALHOST_ROOT/static -p
sudo mkdir $VIRTUALHOST_ROOT/files -p

sudo virtualenv --no-site-packages --distribute environ
sudo pip install -E environ yolk
sudo pip install -E environ django
sudo pip install -E environ south
sudo pip install -E environ pygments

sudo django-admin startproject project

sudo chown $VIRTUALHOST_OWNER_USER:$VIRTUALHOST_OWNER_GROUP ./ -R
ln $VIRTUALHOST_ROOT/environ/lib/python2.6/site-packages/django/contrib/admin/media $VIRTUALHOST_ROOT/static/admin -s

