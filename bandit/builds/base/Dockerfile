FROM ubuntu:20.04

# Specify arguments for user in base image 
ARG ARG_NUM_BANDIT_USERS

# UPDATE and INSTALL packages
ENV TZ=America/New_York DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get upgrade -y
RUN yes | unminimize
RUN apt-get install ubuntu-minimal -y
RUN apt-get install openssh-server -y
RUN apt-get install sudo -y
RUN apt-get install net-tools -y
RUN apt-get install vim -y
RUN apt-get install man -y
RUN apt-get install file -y
RUN apt-get install wget -y
RUN apt-get install tar -y
RUN apt-get install adduser -y
RUN apt-get install netstat-nat -y
RUN apt-get install curl -y
RUN apt-get install perl -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-venv -y
RUN apt-get install zip -y
RUN apt-get install libncurses5 -y
RUN apt-get install w3m -y
RUN apt-get install binutils -y
RUN apt-get install hexedit -y
RUN apt-get install socat -y
RUN apt-get install ncat -y
RUN apt-get install tmux -y
RUN apt-get install dnsutils -y
RUN apt-get install cron -y
RUN apt-get install git -y
RUN apt-get install tcpdump -y

# MATRIX rainfall configuration on SSH login for every user
COPY tmatrix.tar.gz /tmp/tmatrix.tar.gz
RUN tar -xzvf /tmp/tmatrix.tar.gz -C /tmp
WORKDIR /tmp/installation
RUN ./install.sh
RUN rm /tmp/tmatrix.tar.gz
WORKDIR /root
RUN rm -r /tmp/installation

# MOTD for every SSH login
COPY motd /etc/motd
RUN chmod -x /etc/update-motd.d

# Default configuration for each user, create them, update password, and save password to disk, delete files
COPY --chmod=750 run.sh run.sh
COPY --chmod=440 .env passwords.txt
RUN ./run.sh $ARG_NUM_BANDIT_USERS
RUN rm run.sh passwords.txt

# Change WORKDIR and CMD entrypoint
WORKDIR /
RUN service ssh start
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
