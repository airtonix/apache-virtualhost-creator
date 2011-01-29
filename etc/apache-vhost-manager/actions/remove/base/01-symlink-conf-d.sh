#!/bin/sh
echo "Attempting to disable apache virtualhost : $DOMAIN_FQDN"
VHOST_EXTRAS_PATH="/etc/apache2/sites-enabled/$DOMAIN_FQDN.d/"
VHOST_CONF_PATH="/etc/apache2/sites-enabled/$DOMAIN_FQDN"

if [ -d $VHOST_EXTRAS_PATH ]; then
	sudo rm $VHOST_EXTRAS_PATH
fi

if [ -f $VHOST_CONF_PATH ]; then
	sudo a2dissite $DOMAIN_FQDN
	sudo service apache2 restart
fi

