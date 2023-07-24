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
COPY --chmod=0700 run.sh /root
RUN sed -i "s/<ARG_NEXT_USER_USERNAME>/${ARG_NEXT_USER_USERNAME}/" /root/run.sh
RUN sed -i "s/<TMUX_SOCKET_NAME>/\/var\/tmux\/shared-session/" /root/run.sh
CMD ["/root/run.sh"]
