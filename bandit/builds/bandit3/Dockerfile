FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD

RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/bandit/${ARG_NEXT_USER_USERNAME}/password

WORKDIR /home/${ARG_CURR_USER_USERNAME}
RUN dd if=/dev/random of=data bs=1024 count=8
RUN echo "The password for ${ARG_NEXT_USER_USERNAME} is: '${ARG_NEXT_USER_PASSWORD}'" >> data
RUN dd if=/dev/random bs=1024 count=10 >> data
