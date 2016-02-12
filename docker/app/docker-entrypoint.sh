#!/bin/bash
set -e

# Add app as command if needed
if [ "${1:0:1}" = '-' ]; then
	set -- app "$@"
fi

function checkLastCommand 
{
	if [ $? == 0 ]; then
		echo $(printf "%s ok" "$1")
	else
		echo $(printf "%s failed" "$1")
		exit 1
	fi
}  

if [ "$1" = 'app' ]; then
	# Change ownership
	#sudo chown -R app $APP_DIR
	#sudo chown -R app:app /usr/local/bin/gosu

	STRLOG="basic check of required environment variables ... "

	if [ -z "$APP_DIR" ]; then
		echo $(printf "%s failed" "$STRLOG")
		echo >&2 'error: you have not set required environment variables: APP_DIR'
		exit 1
	fi

	if [ -z "$SUPERUSER_NAME" -o -z "$SUPERUSER_EMAIL" -o -z "$SUPERUSER_PASSWORD" ]; then
		echo $(printf "%s failed" "$STRLOG")
		echo >&2 'error: you have not set required environment variables: SUPERUSER_NAME, SUPERUSER_EMAIL and SUPERUSER_PASSWORD'
		exit 1
	fi

	echo $(printf "%s ok" "$STRLOG")

	# Simple but effective 
	# Check if polymer components have been installed to setup some one time only needed setup
	#if [ ! -d $APP_DIR/node_modules ]; then


			##cd $APP_DIR && npm install
			##checkLastCommand "installing npm components"
	#fi

	if [ ! -f /etc/supervisord.conf ]; then

		echo "running one-time only needed setup ... "
		python $APP_DIR/backend/manage.py makemigrations blog accounts services
		checkLastCommand "make first-time migrations for apps: blog, accounts services"

		python $APP_DIR/backend/manage.py migrate
		checkLastCommand "running migrate django ... "
		# First Time - Create SuperUser, install polymer & make migrations
		echo "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('$SUPERUSER_NAME', '$SUPERUSER_EMAIL', '$SUPERUSER_PASSWORD'); exit()" | python $APP_DIR/backend/manage.py shell
		checkLastCommand "creating superuser $SUPERUSER_NAME"


		sudo ln -sf $APP_DIR/backend/conf/celeryd.conf /etc/celeryd.conf
		sudo ln -sf $APP_DIR/backend/conf/celerybeat.conf /etc/celerybeat.conf
		sudo ln -sf $APP_DIR/backend/conf/supervisord.conf /etc/supervisord.conf

		sudo mkdir -p /var/log/supervisord/
		sudo chown yeoman:yeoman /var/log/supervisord/
		sudo touch /var/log/supervisord/supervisord.log
		sudo chown yeoman:yeoman /var/log/supervisord/supervisord.log
	fi

	tail -f /var/log/supervisord/supervisord.log &
	tail -f /app/backend/log/celerybeat.log &
	tail -f /app/backend/log/celery.log &
	tail -f /app/backend/log/project.log & 

	sudo supervisord -c /etc/supervisord.conf
	checkLastCommand "running supervisord ... "

	# Future: add some basic checks that 'backend/' and 'manage.py' exist etc.
	python $APP_DIR/backend/manage.py migrate
	checkLastCommand "running migrate django ... "

	python $APP_DIR/backend/manage.py collectstatic --noinput
	checkLastCommand "collecting static files ... "

	if [ "$ENV_TYPE" = 'dev' -o "$ENV_TYPE" = 'test' ]; then
		python $APP_DIR/backend/manage.py runserver_plus 0.0.0.0:8000
		checkLastCommand "running django $ENV_TYPE server ... "
		##npm run build
		##checkLastCommand "building frontend ... "
		##npm start
		##checkLastCommand "running frontend in $ENV_TYPE mode ... "
	elif [ "$ENV_TYPE" = 'prod' ]; then
		echo "Running Production Django Server Script"
		python $APP_DIR/backend/bin/run.py &
		#echo "Running FrontEnd Polymer"
		#gulp
		##npm start --release
	else
		echo "ERROR: Neither production or development environment selected (ENV_TYPE=$ENV_TYPE is not valid)"
		exit 1
	fi

	echo
	echo 'App init process done. Ready for start up.'
	echo

fi

exec "$@"
