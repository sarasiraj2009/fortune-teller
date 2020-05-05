# SECRET_KEY='YOUR_SECRET_KEY'
# MYSQL_USER='YOUR_MYSQL_USER'
# MYSQL_PASSWORD='YOUR_MYSQL_PASSWORD'
# MYSQL_HOST='YOUR_MYSQL_HOST'
# MYSQL_DATABASE='YOUR_MYSQL_DATABASE'
# ==================================

# install pip dependencies
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt

# remove the old project files
sudo rm -rf /opt/flask-app
# copy new project files into the installation directory
sudo mkdir /opt/flask-app
sudo cp -r . /opt/flask-app
# make sure that the files are owned by pythonadm because that is the user running this application
sudo chown -R pythonadm:pythonadm /opt/flask-app

# configure the service script
# the service script has templated values, the sed command here is replacing them for the actual values which are defined at the start of this script
# once the values have been replace, the file is being saved to /etc/systemd/system/flask-app.service
sed -e "s/{{SECRET_KEY}}/${SECRET_KEY}/g" \
    -e "s/{{MYSQL_USER}}/${MYSQL_USER}/g" \
    -e "s/{{MYSQL_PASSWORD}}/${MYSQL_PASSWORD}/g" \
    -e "s/{{MYSQL_HOST}}/${MYSQL_HOST}/g" \
    -e "s/{{MYSQL_DATABASE}}/${MYSQL_DATABASE}/g" \
    flask-app.service \
    | sudo tee /etc/systemd/system/flask-app.service

# when a change is made to a service unit (which the command above just did), these changes must be reload
sudo systemctl daemon-reload

# recreate the tables in the database if opted for
if ${RECREATE_TABLES}; then 
    # set the database uri so that the create script understands how to connect to the database 
    # this is using the values set at the top of the script
    export DATABASE_URI="mysql+pymysql://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_HOST}/${MYSQL_DATABASE}"
    python create.py
fi

# make sure that the new flask application is running, also stopping the current running flask application
sudo systemctl restart flask-app