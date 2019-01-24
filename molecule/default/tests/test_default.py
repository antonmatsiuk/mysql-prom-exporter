import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_supervisord_running_and_enabled(host):
    mysqld_exporter = host.service('supervisord')
    assert mysqld_exporter.is_enabled


def test_mysqld_exporter_running(host):
    ansible_vars = \
        host.ansible("include_vars",
                     "file=../../defaults/main.yml")["ansible_facts"]
    mysqld_exporter_port = ansible_vars["mysqld_exporter_port"]
    mysqld_exporter_ip = ansible_vars["mysqld_exporter_ip"]
    socket = host.socket('tcp://%s:%s' % (mysqld_exporter_ip,
                                          mysqld_exporter_port))
    assert socket.is_listening
