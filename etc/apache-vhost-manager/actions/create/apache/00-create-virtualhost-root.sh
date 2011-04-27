sudo mkdir $VIRTUALHOST_ROOT -p

cd $VIRTUALHOST_ROOT

sudo mkdir static -p

sudo chown $VIRTUALHOST_OWNER_USER:$VIRTUALHOST_OWNER_GROUP ./ -R

