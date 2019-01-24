Ansible: Mysql Prometheus Exporter
=========

Ansible role to install MySQL prometheus exporter on Linux

Requirements
------------

MySQL is installed on the target host. 

Role Variables
--------------
Available variables with default values (see defaults/main.yml):

Variable defines whether to install golang runtime or not, set to false if already nstalled:
    
    golang_install: true
    
Variable defines whether to install supervisord or not, set to false if already installed:

    supervisor_install: true    
    
Location for GOPATH environment variable:

    golang_gopath_home: "/root/go"

Golang SDK installation directory: 

    golang_install_path: "/usr/local/go"

Whether MySQL Daemon is restarted automatically after installation:

    mysql_restart: true

MySQL daemon on the server: 
    
    mysql_deamon: mariadb

To disable user and client statistics collection turn the following variable to false:
    
    mysql_enable_userstat: true

Installation directory for mysql exporter 

    mysqld_exporter_home: "{{ golang_gopath_home }}/bin"
   
MySQL user/password the exporter will use to connect to MySQL, change password to something more secure: 

    mysqld_exporter_user: "exporter"
    mysqld_exporter_pass: "exporter"
    
MySQL host exporter connects to: 

    mysqld_exporter_host: "localhost"
    
MySQL exporter privileges, consider adding SUPER to reserve connection for exporter client on heavily loaded servers:

    mysqld_exporter_priv: "*.*:PROCESS,REPLICATION CLIENT,SELECT"
    
Additional flags for the exporter. Disable userstats and clientstats if you turned off the previous variable.
The full list of availible flags is [here](https://github.com/prometheus/mysqld_exporter#collector-flags):
    
    mysqld_exporter_extra_flags: "--collect.info_schema.tablestats --collect.info_schema.userstats --collect.info_schema.clientstats"

IP and Port on which mysql exporter listens on the host. Change IP to a desirable value e.g. `{{ ansible_eth0.ipv4.address }}` 
to listen on a specific interface:

    mysqld_exporter_port: 9104
    mysqld_exporter_ip: "0.0.0.0"
    

Dependencies
------------

To install MySQL use e.g.: geerlingguy.mysql
The role also imports `geerlingguy.supervisor` to install supervisord and `gantsign.golang` to install GoLang SDK. 


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