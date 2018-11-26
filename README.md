memoryleak.php
=========

Role for installing and managing recent PHP versions.

Requirements
------------

None

Role Variables
--------------
```php_install_version: 7.2
```
```php_install_extensions:
# - bcmath
  - gd
# - intl
# - json
# - mbstring
# - mysqlnd
# - opcache
# - pdo
# - pspell
# - recode
# - soap
# - xml
# - xmlrpc
# for pecl extensions on RedHat platforms use pecl prefix:
#   - pecl-mongodb
#   - pecl-redis
```
```php_install_fpm: true
```
```php_install_cli: true
```
```php_ini_config:
  - name: memory_limit
    value: 256M

  - name: date.timezone
    value: UTC

  - name: post_max_size
    value: 64M

  - name: upload_max_filesize
    value: 64M
```
```php_fpm_config:
  - name: daemonize
    value: "yes"
```
```php_fpm_pools:
  www:
    - name: user
      value: www-data

    - name: group
      value: www-data

    - name: listen
      value: 0.0.0.0:9000

    - name: listen.owner
      value: www-data

    - name: listen.group
      value: www-data

    - name: pm
      value: dynamic

    - name: pm.start_servers
      value: 2

    - name: pm.min_spare_servers
      value: 1

    - name: pm.max_children
      value: 5

    - name: pm.max_spare_servers
      value: 3
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
