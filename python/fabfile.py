from fabric import Connection

addr = input('Enter IP address: ')
username = "aragorn"
userpass = input('Enter user password: ')
userkey = input('Filename for user\'s public ssh key: ')
userkeypath = "/home/" + username + "/.ssh/authorized_keys"
gitkey = input('Filename for git key: ')
gitkeypath = "/home/" + username + "/.ssh/sybil"

ctx = Connection(host=addr, user=username, connect_kwargs={"password":userpass})

ctx.sudo('apt-get update')
ctx.sudo('apt-get upgrade -y')
ctx.run('export PATH="/home/' + username + '/.local/bin:$PATH"')
ctx.run('python3 -m pip install --user ansible  --no-warn-script-location')
ctx.sudo('mkdir /repos')
ctx.sudo('mkdir /repos/serenity')
ctx.sudo('mkdir /etc/ansible')
ctx.run('mkdir /home/' + username + '/.ssh')
ctx.put(gitkey, remote=gitkeypath)
ctx.put(userkey, remote=userkeypath)
ctx.run('sudo mount LABEL="ark01" /mnt/ark01')
ctx.run('/home/' + username + '/.local/bin/ansible localhost -m ansible.builtin.git -a "repo=git@github.com:srsnowden/serenity.git clone=yes dest=/repos/serenity key_file=' + gitkeypath + ' accept_newhostkey=true" -b')
ctx.run('/home/' + username + '/.local/bin/ansible localhost -m ansible.posix.synchronize -a "src=/repos/serenity/config/ansible/ dest=/etc/ansible/" -b')
ctx.run('/home/' + username + '/.local/bin/ansible-playbook /repos/serenity/playbooks/nexus-refresh.yml --extra-vars "rebuild=full"')
print("Deployment completed, restarting to apply networking changes...")
ctx.sudo('shutdown -r now')
ctx.close()