import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_php_cli_is_installed(host):
    distribution = host.system_info.distribution
    package_name = "php71u-cli"

    if distribution == "debian" or distribution == "ubuntu":
        package_name = "php7.1-cli"

    php_cli = host.package(package_name)

    assert php_cli.is_installed
    assert php_cli.version.startswith("7.1")


def test_php_fpm_is_installed(host):
    distribution = host.system_info.distribution
    package_name = "php71u-fpm"

    if distribution == "debian" or distribution == "ubuntu":
        package_name = "php7.1-fpm"

    php_fpm = host.package(package_name)

    assert php_fpm.is_installed
    assert php_fpm.version.startswith("7.1")


def test_php_config_contains(host):
    distribution = host.system_info.distribution
    file_path = "/etc/php.ini"

    if distribution == "debian" or distribution == "ubuntu":
        file_path = "/etc/php/7.1/cli/php.ini"

    host.file(file_path).contains("upload_max_filesize = 64M")
