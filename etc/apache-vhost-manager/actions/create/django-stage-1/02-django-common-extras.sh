#!/bin/sh
DJANGO_PROJECT_ROOT="${VIRTUALHOST_ROOT}/project"
echo "Changing Directory to : $DJANGO_PROJECT_ROOT"

sudo chmod +x ${VIRTUALHOST_ROOT}/project/manage.py

cd $DJANGO_PROJECT_ROOT
sudo ./manage.py startapp base

