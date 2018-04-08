nudorm.php
=========

A role for installing and configuring PHP.

Requirements
------------

No particular requirement.

Role Variables
--------------

```
# Use a particular repository: ius|remi
rhel_repository: ius

# Install this list of packages.
default_packages:
  - php7.1
  - ...

# If and which FPM package(s) to install.
fpm_packages:
  - php7.1-fpm
  - ...

# Custom PHP-FPM configuration.
fpm_conf_config:

php_ini_config:
  - name: memory_limit
    value: 256M

  - name: date.timezone
    value: UTC

  - name: post_max_size
    value: 64M

  - name: upload_max_filesize
    value: 64M

# Configure the PHP ini path.
php_ini_path: /etc/php/7.1/cli/php.ini

# Configure the PHP conf path.
php_conf_path: /etc/php/7.1/cli/php.ini

# Configure the default pool directory
php_pool_path: /etc/php/7.1/fpm/pool.d
```

Dependencies
------------

No dependency.

Example Playbook
----------------

```
---
- hosts: php
  roles:
    - name: nudorm.php
```

License
-------

BSD

Author Information
------------------
Haydar Ciftci <haydar.ciftci@gmail.com>
