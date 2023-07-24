FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD

RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/blacktuque/${ARG_NEXT_USER_USERNAME}/password

COPY --chmod=0700 main.py /root/main.py
RUN /root/main.py ${ARG_NEXT_USER_PASSWORD} > /home/${ARG_CURR_USER_USERNAME}/regex.txt
