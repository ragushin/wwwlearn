sudo /etc/init.d/mysql start
mysql -u root -e "CREATE DATABASE box_django;"

sudo rm -r /etc/nginx/sites-enabled/default
ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo gunicorn -b 0.0.0.0:8080 hello &
sudo gunicorn -b 0.0.0.0:8000 ask.wsgi:application &

#virtualenv --python=/usr/bin/python3.4 web/myvenv 
#web/myvenv source web/myvenv/bin/activate
#sudo gunicorn -b 0.0.0.0:8080 --pythonpath /home/box/web/ hello:app &     
#sudo gunicorn -b 0.0.0.0:8000 --pythonpath /home/box/web/ask ask.wsgi:application & 


