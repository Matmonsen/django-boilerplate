import os
import random
import fileinput
from invoke import run, task
from .base.settings import SECRET_FILE


@task
def generate_secret_key():
    key = ''.join(
        [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    secret = open(SECRET_FILE, 'w')
    secret.write(key)
    secret.close()


@task
def setup(project_name='', app_name='',  superuser=False, git=True):
    print('Welcome to setup')
    if app_name and project_name:
        print('... renaming project')
        os.rename("boilerplate", app_name)
        os.rename("django_boilerplate", project_name)

        print('... adding project to installed apps')
        for line in fileinput.input(os.path.dirname(__file__) + '/base/settings/default.py', inplace=True):
            print(line.replace('boilerplate', app_name), end='')

        print('... generating secret key')
        generate_secret_key()

        if git:
            print('... removing old .git folder')
            run('rm- rf ../.git')
            print('... initilizing git')
            run('git init')

        if superuser:
            build()
            print('.. creating superuser')
            run('./manage.py createsuperuser')
        print('... done with setup. Enoy!')
    else:
        print('name cannot be empty')


@task
def build(production=False):
    print('Building... ')

    print('... migrating')
    run('./manage.py makemigrations')
    run('./manage.py migrate')

    if production:
        print('... collecting static')
        run('./manage.py collectstatic --noinput')
    print('... done building')


@task
def push(all_files=False, message=''):
    print('Pushing...')
    if all_files:
        print('... Adding all files')
        run('git add .')
    else:
        print('... Adding updated files')
        run('git add -u .')
    print('... committing')
    run('git commit -m "%s"') % message
    print('... pushing')
    run('git push')
    print('... done pushing')


@task
def deploy():
    print('Deploying...')
    print('... pulling')
    run('git pull')
    build(production=True)
    print('... done deploying')


@task
def test(app=''):
    print('Testing...')
    run('./manage.py test "%s"') % app
    print('... done testing')


@task
def run(port=8000):
    print('Running server ...')
    run('./manage.py runserver:{0}'.format(port))


@task
def docs():
    pass