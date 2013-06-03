from fabric.api import run, env, sudo

env.roledefs = {
    'web': ['ubuntu@184.72.242.204']
}

env.key_filename = 'ec2-keypair'

env.roles = ['web']

def deploy(verbose='no'):
    sudo('rm -rf /srv/app')
    if verbose == 'yes':
        sudo('puppet agent --no-daemonize --onetime -v')
    else:
        sudo('puppet agent --no-daemonize --onetime')
