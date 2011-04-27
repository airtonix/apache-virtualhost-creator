#!/bin/sh
DJANGO_PROJECT_ROOT="${VIRTUALHOST_ROOT}/project"
echo "Changing Directory to : $DJANGO_PROJECT_ROOT"
cd $DJANGO_PROJECT_ROOT

#sudo ./manage.py collectstatic
sudo ./manage.py syncdb

cd ${VIRTUALHOST_ROOT}
sudo chown $VIRTUALHOST_OWNER_USER:$VIRTUALHOST_OWNER_GROUP ./ -R

cd ${VIRTUALHOST_ROOT}/static

