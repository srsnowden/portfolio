This is a public duplicate of a private project from early 2023.  The primary goal of this project was to manage system configuration/deployment and automate a few tasks on a home network; this was done mostly with Ansible with a couple Python scripts included.  

The repo was intended to be as self-contained as possible - it includes a bootstrapper script, python/fabfile.py, that can be run from any computer with Python installed (and the fabric library).  This script connects to a Linux computer on the network to install Ansible, sync the repo, and run the playbook to configure itself as the "hub" server for the network from which all future Ansible playbooks would run.

Almost all of the Ansible tasks were written in roles, the playbooks primarily execute a sequence of those roles.  A brief description of the roles is below, and a system inventory below that.

### Ansible Roles
- avahi - installs avahi to the hub server and configures it as a multicast DNS repeater
- c_cert - cron job to renew SSL certificate
- cert -  obtains a valid SSL certificate signed by LetsEncrypt
- d_cats - deploys a copy of the cats website from the file server
- d_mailcert - deploys SSL certificate to the mail server
- d_mediacert - deploys SSL certificate to the media server
- d_proxycert - deploys SSL certificate to the web server
- fw_default - configures iptables with the default rules
- hub - congiguration for the hub server
- iptables - installs iptables
- m_cats - sends mail when cats site updates
- media - firewall rules for media server
- pihole - firewall rules for pihole server
- proxhost - configuration specific to proxmox host servers
- proxy - configuration for the web server
- raspi - configuration specific to raspberry pis
- samba - installs samba and configures file server
- sshd - ssh configuration
- syncthing - installs and configures syncthing
- user - user setup
- python/cats-update.py - python script to update cats site with new pictures

### System Inventory
- Nexus: raspberry pi, hub - ran Ansible, and was also a file server/multicast DNS repeater
- Palantir: raspberry pi, web server - hosted webpage with pictures of my cats
- Boxy/Cubey: intel NUCs, proxmox cluster - hosted Proxmox virtualization platform, mainly used for running debian containers
- Mikro: Mikrotik hEX S, router
- Switch: Cisco SG350-10
- Trident: TP Link router acting as wireless AP
