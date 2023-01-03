from fabric import Connection

addr = input('Enter IP address: ')
username = "aragorn"
userpass = input('Enter user password: ')
gitkey = input('Enter valid git key filename: ')
gitkeypath = "/home/" + username + "/.ssh/" + gitkey


ctx = Connection(host=addr, user=username, connect_kwargs={"password":userpass})

ctx.sudo('apt-get update')
ctx.sudo('apt-get upgrade -y')
ctx.run('export PATH="/home/' + username + '/.local/bin:$PATH"')
ctx.run('python3 -m pip install --user ansible')
ctx.sudo('mkdir /repos')
ctx.sudo('mkdir /repos/serenity')
ctx.run('mkdir /home/' + username + '/.ssh')
ctx.put(gitkey, remote=gitkeypath)
ctx.run('/home/' + username + '/.local/bin/ansible localhost -m ansible.builtin.git -a "repo=git@github.com:srsnowden/serenity.git clone=yes dest=/repos/serenity key_file=' + gitkeypath + ' accept_newhostkey=true" -b')
ctx.close()

# add shutdown line