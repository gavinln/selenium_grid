FROM node:0.10.30

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq && \
    apt-get update && \
    apt-get install -y -q \
        wget \
        openjdk-7-jdk && \
    rm -rf /var/lib/apt/lists/*

# Define commonly used JAVA_HOME variable
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64

RUN npm install -g bower \
        npm-cache \
        grunt-cli

RUN wget -q http://maven.jenkins-ci.org/content/repositories/releases/org/jenkins-ci/plugins/swarm-client/1.22/swarm-client-1.22-jar-with-dependencies.jar

CMD java -jar swarm-client-1.22-jar-with-dependencies.jar -master http://$MASTER_PORT_8080_TCP_ADDR:$MASTER_PORT_8080_TCP_PORT $EXTRA_PARAMS
