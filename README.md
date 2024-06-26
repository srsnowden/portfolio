Public duplicate of a private project from early 2023.  The primary goal of this project was to manage system configuration/deployment and automate a few tasks on a home network; this is done mostly with Ansible, with a couple Python scripts included.  Everything was personally written with the exception of config/ansible/roles/cert/tasks/main.yml which was largely based off of an online sample.

The basic intent was for python/fabfile.py to serve as a bootstrapper - it could be run from any computer with Python (and the fabric library) to connect to a local linux system, install Ansible, and sync this repo; that devive would then be used as the system "hub" to run further Ansible playbooks.

### System Components
- Nexus: raspberry pi, hub - ran Ansible, and was also a file server/multicast DNS repeater.
- Palantir: raspberry pi, web server - hosted webpage with pictures of my cats. 
- Boxy/Cubey: intel NUCs, proxmox cluster - hosted Proxmox virtualization platform, mainly used for running debian containers.
- Mikro: Mikrotik hEX S, router
- Switch: Cisco SG350-10
- Trident: TP Link router acting as wireless AP
