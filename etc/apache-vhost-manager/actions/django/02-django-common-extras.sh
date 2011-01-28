#!/bin/sh
cd $VIRTUALHOST_ROOT/project

sudo ./manage.py startapp common

sudo touch ./common/forms.py

sudo mkdir ./common/templates/

sudo mkdir ./common/template_tags/
sudo touch ./common/template_tags/__init__.py

sudo mkdir ./common/utils/
sudo touch ./common/utils/__init__.py

