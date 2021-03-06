Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3
* Git
* pip
* virtualenv

eg, on Ubuntu:

    sudo apt-get install nginx git python3 python3-pip
    sudo pip3 install virtualenv

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Upstart Job

* see gunicorn-upstart.template.conf
* replace SITENAME with, eg, staging.my-domain.com

## Folder structure:
Assume we have a user account at /home/username

/home/username
└── sites
    └── SITENAME
         ├── database
         ├── source
         ├── static
         └── virtualenv

## Fabric
* Runs in Python 2
    sudo pip2 install python-dev
    sudo pip2 install fabric
    sudo pip2 install pycrypto
    sudo pip2 install ecdsa

* Deploy:
    fab deploy --host=cmermingas@staging.fitbody.io


## Set up NGINX and GUNICORN
## nginx.template.conf
* Notice 'cmermingas' hardcoded in the file
    sed "s/SITENAME/WWW.DOMAIN.COM/g" deploy_tools/nginx.template.conf | sudo tee /etc/nginx/sites-available/WWW.DOMAIN.COM
    sudo ln -s /etc/nginx/sites-available/WWW.DOMAIN.COM /etc/nginx/sites-enabled/WWW.DOMAIN.COM

## gunicorn-upstart.template.conf
* Notice 'cmermingas' hardcoded in the file
    sed "s/SITENAME/WWW.DOMAIN.COM/g" deploy_tools/gunicorn-upstart.template.conf | sudo tee /etc/init/gunicorn-WWW.DOMAIN.COM.conf
    sudo service nginx reload
    sudo start gunicorn-WWW.DOMAIN.COM
    sudo restart gunicorn-WWW.DOMAIN.COM

* Logging with gunicorn
    exec ../virtualenv/bin/gunicorn \
        --bind unix:/tmp/superlists-staging.ottg.eu.socket \
        --access-logfile ../access.log \
        --error-logfile ../error.log \
        superlists.wsgi:application
    That will put an access log and error log into the ~/sites/$SITENAME folder.