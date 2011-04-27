#!/usr/bin/env python
from distutils.core import setup
from utils import copytree, read_file
import os

here_path = os.path.abspath(os.path.dirname(__file__))

def main():
	conf_path_list = os.path.join("etc", "apache-vhost-manager")
	etc_config_path_src =	os.path.join( here_path, conf_path_list )
	etc_config_path_dst = os.path.join( "/", conf_path_list )


	setup(
		name='apache_vhost_manager',
		version='0.0.3',
		author="airtonix",
		maintainer="Airtonix",
		maintainer_email="airtonix@gmail.com",
		url="airtonix.net/projects/apache_vhost_creator",
		scripts = [
			'usr/bin/apache-vhost-manager'
		],
		license = read_file('LICENSE.md'),
		description='A helper script to manage apache subdomain based virtualhosts. It inserts BIND dns records, sets up django projects and LDAP authentication directives.',
		long_description = read_file('README.md')
	)
	copytree( etc_config_path_src,  etc_config_path_dst)

if __name__ == "__main__" :
	main()

