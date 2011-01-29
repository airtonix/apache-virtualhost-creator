#!/bin/sh
cd /etc/apache2/sites-enabled

sudo ln  /etc/apache2/sites-available/$DOMAIN_FQDN.d/ -s

