FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD

RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/bandit/${ARG_NEXT_USER_USERNAME}/password

# ROT17 -> base64
COPY main.py /root/main.py
RUN python3 /root/main.py "The password for ${ARG_NEXT_USER_USERNAME} is: '${ARG_NEXT_USER_PASSWORD}'" 17 | base64 > /home/${ARG_CURR_USER_USERNAME}/encoded.encrypted.txt
