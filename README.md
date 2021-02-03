memoryleak.php
=============

A role to install and configure PHP.


Requirements
------------

If you need any PHP version from a non-standard repository then you'd need to make sure these are enabled and configured (e.g. remi).

Role Variables
--------------

See [defaults/main.yml](defaults/main.yml)

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: memoryleak.php }

License
-------

MIT

Author Information
------------------

Haydar Ciftci <haydar.ciftci@gmail.com>
