import os
import random
import fileinput
from invoke import run, task


@task
def generate_secret():
    """

        Generates a new secret key and stores it secret.txt

    """
    secret_file = os.path.join(os.path.dirname(__file__) + '/base/settings/', 'secret.txt')
    key = ''.join(
        [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    secret = open(secret_file, 'w')
    secret.write(key)
    secret.close()


@task
def setup(project_name='', app_name='', superuser=False, git=False, documentation=False):
    """
        Setup

        Changes the project and app name.
        Adds the new app name to installed_apps.
        It ca also create superusers.
        Or even initialize a new git and delete the old .git/ folder
        Generates documentation

        Args:
            project_name (str): New project name instead of django-boilerplate.
            app_name (str): New application name instead of django_boilerplate.
            superuser (bool): Decides whether to create a superuser or not.
            git (bool): Decides whether to init a new git and delete the old.
            documentation (bool): Decides whether to generate new documentation or not
    """
    print('Welcome to setup')
    if app_name and project_name:
        print('... generating secret key')
        generate_secret()

        print('... adding project to installed apps')
        for line in fileinput.input(os.path.dirname(__file__) + '/base/settings/default.py', inplace=True):
            print(line.replace('boilerplate', app_name), end='')

        print('... renaming project')
        os.rename("boilerplate", app_name)
        os.rename(os.path.dirname(__file__), os.path.dirname(os.path.dirname(__file__)) + '/' + project_name)
        os.rename(os.path.dirname(os.path.dirname(__file__)),
                  os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + '/' + project_name)

        if git:
            print('... removing old .git folder')
            run('rm -rf ../.git')
            print('... initilizing git')
            run('git init ../')

        build(documentation=documentation)

        if superuser:
            print('.. creating superuser')
            run('./manage.py createsuperuser')
        print('... done with setup. Enoy!')
    else:
        print('project and app name cannot be empty')


@task
def build(documentation=False, production=False):
    """
        Builds the application

        Migrates the database.
        Generates documentation.
        Collects static

        Args:
            documentation (bool): Decides whether to generate documentation or not
            production (bool): Decides whether to collect static or not
    """
    print('Building... ')

    print('... migrating')
    run('./manage.py makemigrations')
    run('./manage.py migrate')

    if production:
        print('... collecting static')
        run('./manage.py collectstatic --noinput')

    if documentation:
        docs()
    print('... done building')


@task
def push(all_files=False, message=''):
    """
        Easier to add, commit and push via git

        all_files (bool):  Decides if only updated or all files should be pushed.
        message (str): Commit message
    """
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
    """
        Pulls the project for git repo.
        Restarts the server.
    """
    print('Deploying...')
    print('... pulling')
    run('git pull')
    build(production=True)
    print("run('deploying shellscript that restarts the server')")
    print('... done deploying')


@task
def test(app=''):
    """
        Tests one app or all apps
    """
    print('Testing...')
    run('./manage.py test "{0}"'.format(app))
    print('... done testing')


@task
def freeze(name='requirements'):
    """
        Freezes the dependencies into a file

        Args:
            name (str): Name of the requirement file
    """
    print('Freezing requirements...')
    run('pip freeze > ../{0}.txt'.format(name))
    print('... done freezing')


@task
def update():
    """

        Updates the requirements file

    """
    print('Updating...')
    run('pip install --upgrade -r requirements.txt')
    print('... done upgrading')


@task
def install():
    """
        Install all from requirements.txt
    """
    print('Installing ...')
    run('pip install -r requirements.txt')
    print('... done installing')
    

@task
def docs():
    """
        Creates documentation for the project
    """
    if os.path.isdir(os.path.dirname(os.path.dirname(__file__)) + '/docs'):
        print('Creating docs...')
        run('make html')
        print('.. done with docs')
    else:
        print('Creating docs...')
        run('sphinx-quickstart')
        print('.. done with docs')
