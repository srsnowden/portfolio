# fabfile.py
Python script for first-time setup of Raspberry Pi used as hub server.

### Requirements
- Pyton and fabric installed on local computer
- Raspberry pi set up with user aragorn
- Public ssh key for human user
- Private ssh key for git repo

### Output
- Updates packages
- Adds user /.local/bin to $PATH
- Installs Ansible
- Creates user .ssh directory and copies keys
- Mounts external drive to /mnt/ark01
- Creates /repos/serenity and clones repo
- Creates /etc/ansible and populates with config from repo folder
- Runs nexus-refresh playbook
- Restarts pi
