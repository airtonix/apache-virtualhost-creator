#!/bin/sh
echo "Attempting to disable apache virtualhost : $DOMAIN_FQDN"
VHOST_ENABLED_CONF_PATH="/etc/apache2/sites-enabled/$DOMAIN_FQDN"
VHOST_AVAILABLE_CONF_PATH="/etc/apache2/sites-available/$DOMAIN_FQDN"

if [ -f $VHOST_ENABLED_CONF_PATH ]; then
	sudo a2dissite $DOMAIN_FQDN
	sudo service apache2 restart
	sudo rm $VHOST_ENABLED_CONF_PATH
fi

if [ -f $VHOST_AVAILABLE_CONF_PATH ]; then
	sudo rm $VHOST_AVAILABLE_CONF_PATH
fi

