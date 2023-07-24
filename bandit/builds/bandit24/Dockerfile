FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_CURR_USER_PASSWORD
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD
  
RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/blacktuque/${ARG_NEXT_USER_USERNAME}/password

COPY  --chown=${ARG_NEXT_USER_USERNAME}:${ARG_NEXT_USER_USERNAME} --chmod=771 main.py /home/${ARG_CURR_USER_USERNAME}/generate_password.py
RUN echo "${ARG_CURR_USER_USERNAME} ALL=(${ARG_NEXT_USER_USERNAME}) /home/${ARG_CURR_USER_USERNAME}/generate_password.py *" > /etc/sudoers.d/bandit24
RUN pip3 install click
