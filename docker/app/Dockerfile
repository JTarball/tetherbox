FROM jtarball/docker-base:latest
MAINTAINER James Tarball <james.tarball@gmail.com>

ENV ENV_TYPE test
ENV APP_DIR /app

# 1. install pip requirements    - install requirements based on environment type (dev/production)
# 2. copy app folder             - code source code (you can then mount using docker-compose for development)
# 3. copy and define entrypoint  - script running required command/s (see Dockerfile best practices)
COPY requirements $BUILD_DIR/requirements
RUN sudo pip install -r $BUILD_DIR/requirements/$ENV_TYPE.txt
# If a test environment Need a few more things
#RUN if [ "$ENV_TYPE" = 'test' ]; then apt-get -yq update && apt-get -yq install firefox && apt-get clean && rm -rf /var/lib/apt/lists/*; fi

COPY app $APP_DIR

COPY docker-entrypoint.sh /entrypoint.sh
RUN sudo chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 8000
EXPOSE 3000
EXPOSE 3001

CMD ["app"]
