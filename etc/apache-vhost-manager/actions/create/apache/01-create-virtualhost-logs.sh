#!/bin/sh
sudo mkdir $VIRTUALHOST_ROOT/logs -p

sudo touch $VIRTUALHOST_ROOT/logs/static-errors.log
sudo touch $VIRTUALHOST_ROOT/logs/static-requests.log
sudo touch $VIRTUALHOST_ROOT/logs/static-authentications.log

sudo chown $VIRTUALHOST_OWNER_USER:$VIRTUALHOST_OWNER_GROUP $VIRTUALHOST_ROOT -R

