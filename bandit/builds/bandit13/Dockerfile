FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_CURR_USER_PASSWORD
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD

RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/blacktuque/${ARG_NEXT_USER_USERNAME}/password

COPY --chmod=755 customshell /usr/bin/customshell
RUN echo "/usr/bin/customshell" >> /etc/shells
COPY note.txt /home/${ARG_CURR_USER_USERNAME}/note.txt
RUN cat /usr/bin/customshell >> /home/${ARG_CURR_USER_USERNAME}/note.txt
RUN chsh -s /usr/bin/customshell ${ARG_CURR_USER_USERNAME}
RUN mkdir .hidden
RUN echo "${ARG_NEXT_USER_PASSWORD}" > .hidden/.thisisntthebesthidingspotbutyoufoundme.txt
