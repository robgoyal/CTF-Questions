FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_CURR_USER_PASSWORD
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD
  
RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/bandit/${ARG_NEXT_USER_USERNAME}/password

RUN usermod -aG sudo ${ARG_CURR_USER_USERNAME}
RUN apt-get install tmux -y

WORKDIR /root
COPY lshell.tar.gz lshell.tar.gz
RUN tar -xzvf lshell.tar.gz

WORKDIR /root/lshell
RUN python3 setup.py install --no-compile --install-scripts=/usr/bin

WORKDIR /
RUN echo "/bin/lshell" >> /etc/shells
RUN chsh -s /bin/lshell ${ARG_CURR_USER_USERNAME}

RUN echo "Welcome hacker. The password is located at /var/password.txt Can you access it?" > /home/${ARG_CURR_USER_USERNAME}/note.txt
RUN echo "The password for ${ARG_NEXT_USER_USERNAME} is: '${ARG_NEXT_USER_PASSWORD}'" > /var/password.txt
