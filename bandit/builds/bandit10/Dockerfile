FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD

RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/bandit/${ARG_NEXT_USER_USERNAME}/password

RUN chmod 751 /root
COPY --chmod=646 history /root/history
RUN sed -i "s/<ARG_NEXT_USER_USERNAME>/${ARG_NEXT_USER_USERNAME}/" /root/history
RUN sed -i "s/<ARG_NEXT_USER_PASSWORD>/${ARG_NEXT_USER_PASSWORD}/" /root/history
RUN echo "export HISTFILE=/root/history" >> /home/${ARG_CURR_USER_USERNAME}/.bashrc
RUN ln -sf /dev/null .bash_history
