from fabric.api import run, env, sudo

env.roledefs = {
    'web': ['ubuntu@ec2-54-225-54-129.compute-1.amazonaws.com']
}

env.key_filename = 'ec2-keypair'

env.roles = ['web']

def deploy():
    sudo('rm -rf /srv/app')
    sudo('puppet agent --no-daemonize --onetime')
