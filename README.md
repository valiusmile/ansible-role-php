[![Build Status](https://travis-ci.org/memoryleak/ansible-role-php.svg?branch=v3)](https://travis-ci.org/memoryleak/ansible-role-php)

memoryleak.php
=========

Role for installing and managing recent PHP versions.

Requirements
------------

None

Role Variables
--------------
```
php_el8_module: php:7.3
php_selinux_support: true
php_ini_path: /etc/php.ini
php_ini_dir_path: /etc/php.d
php_ini_config: []
# - name: date.timezone
#   value: UTC

php_fpm_conf_path: /etc/php-fpm.conf
php_fpm_pool_path: /etc/php-fpm.d
php_fpm_pool_files: []
# www:
#   user: nginx


php_fpm_service_enabled: true
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

    - hosts: all
      roles:
        - role: memoryleak.php

License
-------

BSD

Author Information
------------------

Haydar Ciftci, <haydar.ciftci@gmail.com>
