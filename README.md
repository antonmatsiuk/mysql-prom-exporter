Ansible: Mysql Prometheus Exporter
=========

Ansible role to install mysql prometheus exporter on Linux

Requirements
------------

MySQL is installed on the target host. 

Role Variables
--------------
Available variables with default values (see defaults/main.yml):

Installation directory for mysql exporter 

    mysql_exporter_home

MySQL user/pass the exporter will use to connect to MySQL, change password to something more secure: 

    mysql_exporter_user: "exporter"
    mysql_exporter_pass: "exporter"
    
To disable user and client statistics collection turn the following variable to false:
    
    mysql_enable_userstat: true

Additional flags for the exporter. Disable userstats and clientstats if you turned off the previous variable.
The full list of availible flags is [here](https://github.com/prometheus/mysqld_exporter#collector-flags)
    
    mysql_exporter_extra_flags: "--collect.info_schema.tablestats --collect.info_schema.userstats --collect.info_schema.clientstats"

IP and Port on which mysql exporter listens. Change IP to an appropriate value e.g. `{{ ansible_eth0.ipv4.address }}` 
to listen on a specific interface:

    mysql_exporter_port: 9100
    mysql_exporter_ip: "0.0.0.0"
    

Dependencies
------------

Install mysql with any available role e.g.: geerlingguy.mysql

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

MIT / BSD

Author Information
------------------

DevOps / SRE / Cloud Engineer [Anton Matsiuk](https://github.com/antonmatsiuk)