FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_CURR_USER_PASSWORD
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD
  
RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/bandit/${ARG_NEXT_USER_USERNAME}/password

COPY --chown=${ARG_CURR_USER_USERNAME}:${ARG_CURR_USER_USERNAME} --chmod=755 main.py /home/${ARG_CURR_USER_USERNAME}/main.py
RUN setcap cap_setuid+ep /usr/bin/python3.8

