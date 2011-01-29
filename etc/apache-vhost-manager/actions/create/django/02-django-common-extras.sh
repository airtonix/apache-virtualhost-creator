#!/bin/sh
DJANGO_PROJECT_ROOT="${VIRTUALHOST_ROOT}project"
echo "Changing Directory to : $DJANGO_PROJECT_ROOT"

cd $DJANGO_PROJECT_ROOT

sudo chmod +x ./manage.py

sudo ./manage.py startapp common

sudo touch ./common/forms.py

sudo mkdir ./common/templates/

sudo mkdir ./common/template_tags/
sudo touch ./common/template_tags/__init__.py

sudo mkdir ./common/utils/
sudo touch ./common/utils/__init__.py

