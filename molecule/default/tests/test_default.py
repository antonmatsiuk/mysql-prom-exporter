import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_supervisord_running_and_enabled(host):
    mysql_exporter = host.service('supervisord')
    assert mysql_exporter.is_enabled


def test_mysql_exporter_running(host):
    ansible_vars = \
        host.ansible("include_vars",
                     "file=../../defaults/main.yml")["ansible_facts"]
    mysql_exporter_port = ansible_vars["mysql_exporter_port"]
    socket = host.socket('tcp://%s:%s' % (mysql_exporter_ip, mysql_exporter_port))
    assert socket.is_listening