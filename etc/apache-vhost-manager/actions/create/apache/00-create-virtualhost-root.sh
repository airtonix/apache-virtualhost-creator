sudo mkdir $VIRTUALHOST_ROOT -p

cd $VIRTUALHOST_ROOT

sudo mkdir public_html/img -p
sudo mkdir public_html/js -p
sudo mkdir public_html/css -p

sudo chown $VIRTUALHOST_OWNER_USER:$VIRTUALHOST_OWNER_GROUP ./ -R

