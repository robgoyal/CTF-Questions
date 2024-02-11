FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_CURR_USER_PASSWORD
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD
  
RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/bandit/${ARG_NEXT_USER_USERNAME}/password

# chattr - sudo privileges for current user
RUN echo "${ARG_CURR_USER_USERNAME} ALL = NOPASSWD: /usr/bin/chattr" > /etc/sudoers.d/${ARG_CURR_USER_USERNAME}
RUN touch /opt/seed
RUN chown ${ARG_CURR_USER_USERNAME}:${ARG_CURR_USER_USERNAME} /opt/seed

# copy pspy64
COPY --chown=${ARG_CURR_USER_USERNAME}:${ARG_CURR_USER_USERNAME} pspy64 /home/${ARG_CURR_USER_USERNAME}/pspy

# CRONJOB script execution
COPY --chown=${ARG_NEXT_USER_USERNAME}:${ARG_NEXT_USER_USERNAME} --chmod=755 check.sh /usr/local/bin/check.sh
RUN echo "* * * * * root /bin/bash /usr/local/bin/check.sh ${ARG_CURR_USER_USERNAME} ${ARG_NEXT_USER_USERNAME}" > /etc/cron.d/daily
RUN chmod o-r /etc/cron.d/daily

# Execute chattr and run the sshd
COPY --chmod=750 run.sh /root/run.sh
CMD ["/root/run.sh"]
