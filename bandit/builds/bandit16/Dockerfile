FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_CURR_USER_PASSWORD
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD
  
RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/blacktuque/${ARG_NEXT_USER_USERNAME}/password

RUN addgroup tmux
RUN mkdir /var/tmux
RUN chgrp tmux /var/tmux
RUN chmod g+ws /var/tmux
RUN usermod -aG tmux ${ARG_CURR_USER_USERNAME}
RUN usermod -aG tmux ${ARG_NEXT_USER_USERNAME}
RUN echo "* * * * * ${ARG_NEXT_USER_USERNAME} bash -c 'if ! tmux -S /var/tmux/shared-session ls; then tmux -S /var/tmux/shared-session new -d; fi'" > /etc/crontab

COPY --chmod=0700 run.sh /root
CMD ["/root/run.sh"]
