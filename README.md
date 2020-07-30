memoryleak.php
==============

Role for installing and configuring PHP.

Requirements
------------

None

Role Variables
--------------

```
php_el8_module: php:7.3
php_selinux_support: false
php_ini_path: /etc/php.ini
php_ini_dir_path: /etc/php.d
php_ini_config: []
php_fpm_conf_path: /etc/php-fpm.conf
php_fpm_pool_path: /etc/php-fpm.d
php_fpm_pool_files: []
php_fpm_service_enabled: false
php_fpm_service_name: php-fpm
php_fpm_config: []
php_install_packages:
  - php-fpm
  - php-cli
  - php-bcmath
  - php-common
  - php-enchant
  - php-gd
  - php-gmp
  - php-intl
  - php-json
  - php-ldap
  - php-mbstring
  - php-mysqlnd
  - php-opcache
  - php-pdo
  - php-pear
  - php-process
  - php-recode
  - php-snmp
  - php-soap
  - php-xml
  - php-xmlrpc

```

Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
	    - name: memoryleak.php

License
-------

BSD

Author Information
------------------

Haydar Ciftci <haydar.ciftci@gmail.com>
