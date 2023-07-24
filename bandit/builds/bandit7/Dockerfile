FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD

RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/blacktuque/${ARG_NEXT_USER_USERNAME}/password

COPY --chmod=0700 run.sh /root/run.sh
RUN sed -i "s/<ARG_CURR_USER_USERNAME>/${ARG_CURR_USER_USERNAME}/g" /root/run.sh
RUN sed -i "s/<ARG_NEXT_USER_PASSWORD>/${ARG_NEXT_USER_PASSWORD}/g" /root/run.sh
RUN sed -i "s/<ARG_NEXT_USER_USERNAME>/${ARG_NEXT_USER_USERNAME}/g" /root/run.sh
RUN chmod 700 /tmp
CMD ["/root/run.sh"]
