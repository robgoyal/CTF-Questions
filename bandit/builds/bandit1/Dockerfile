FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD

RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/bandit/${ARG_NEXT_USER_USERNAME}/password

RUN /bin/bash -c 'mkdir -p /home/${ARG_CURR_USER_USERNAME}/flag{1..15}/.password{0..11}'
RUN echo "${ARG_NEXT_USER_PASSWORD}" > /home/${ARG_CURR_USER_USERNAME}/flag7/.password9/.hidden.password.txt
