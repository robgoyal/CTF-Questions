FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_CURR_USER_PASSWORD
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD
  
RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/blacktuque/${ARG_NEXT_USER_USERNAME}/password

COPY hello-elementor.zip /tmp
RUN unzip /tmp/hello-elementor.zip -d /tmp
RUN mkdir -p /var/www/wordpress
RUN mv /tmp/hello-elementor/* /var/www/wordpress
RUN rm -r /tmp/hello-elementor* 
RUN chmod o+w /home/bandit17 /var/www /var/www/wordpress
RUN echo "* * * * * ${ARG_NEXT_USER_USERNAME} cd /var/www/wordpress && tar -czvf /home/${ARG_CURR_USER_USERNAME}/wordpress-backup.tar.gz *" > /etc/crontab

COPY --chmod=750 run.sh /root
CMD ["/root/run.sh"]
