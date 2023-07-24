FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_CURR_USER_PASSWORD

COPY motd /etc/motd
RUN echo "cat /etc/motd" >> /home/${ARG_CURR_USER_USERNAME}/.profile
