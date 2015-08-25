import os
import random
import fileinput
from invoke import run, task


@task
def generate_secret():
    secret_file = os.path.join(os.path.dirname(__file__) + '/base/settings/', 'secret.txt')
    key = ''.join(
        [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    secret = open(secret_file, 'w')
    secret.write(key)
    secret.close()


@task
def setup(project_name='', app_name='',  superuser=False, git=False):
    print('Welcome to setup')
    if app_name and project_name:
        print('... generating secret key')
        generate_secret()

        print('... renaming project')
        os.rename("boilerplate", app_name)
        os.rename(os.path.dirname("django_boilerplate"), project_name)

        print('... adding project to installed apps')
        for line in fileinput.input(os.path.dirname(__file__) + '/base/settings/default.py', inplace=True):
            print(line.replace('boilerplate', app_name), end='')

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
        print('project and app name cannot be empty')


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
        run('git add -u')
    print('... committing')
    run('git commit -m "{0}"'.format(message))
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
    run('./manage.py test "{0}"'.format(app))
    print('... done testing')


@task
def run_server(port=8000):
    print('Running server ...')
    print('... Running on 127.0.0.1:{0}'.format(port))
    run('./manage.py runserver localhost:{0}'.format(port))


@task
def docs():
    pass