FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD

RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/blacktuque/${ARG_NEXT_USER_USERNAME}/password

WORKDIR /home/${ARG_CURR_USER_USERNAME}
RUN mkdir matrix
COPY xxd.html man.page matrix
RUN echo "Disallow: /the/password/for/${ARG_NEXT_USER_USERNAME}/is/${ARG_NEXT_USER_PASSWORD}" > matrix/robots.txt
RUN tar -czvf matrix.tar matrix
RUN gzip matrix.tar
RUN xxd matrix.tar.gz > whatisthis
RUN rm -r matrix matrix.tar.gz
