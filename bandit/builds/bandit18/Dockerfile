FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_CURR_USER_PASSWORD
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD
  
RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/blacktuque/${ARG_NEXT_USER_USERNAME}/password

RUN apt-get install tcpdump cron ftp -y
COPY --chown=${ARG_NEXT_USER_USERNAME}:${ARG_NEXT_USER_USERNAME} --chmod=640 main.py /home/${ARG_NEXT_USER_USERNAME}/main.py
RUN sed -i "s/<ARG_NEXT_USER_USERNAME>/${ARG_NEXT_USER_USERNAME}/" /home/${ARG_NEXT_USER_USERNAME}/main.py
RUN echo "*/2 * * * * ${ARG_NEXT_USER_USERNAME} python3 /home/${ARG_NEXT_USER_USERNAME}/main.py" >> /etc/crontab
RUN groupadd pcap
RUN usermod -a -G pcap ${ARG_CURR_USER_USERNAME}
RUN chgrp pcap /usr/sbin/tcpdump
RUN setcap cap_net_raw,cap_net_admin=eip /usr/sbin/tcpdump

COPY --chmod=750 run.sh /root
CMD ["/root/run.sh"]
