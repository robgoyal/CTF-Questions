FROM bandit-base-img:latest

ARG ARG_CURR_USER_USERNAME
ARG ARG_NEXT_USER_USERNAME
ARG ARG_NEXT_USER_PASSWORD
ARG NEXT_USER_PASSWORD_KEY=trinity

RUN echo "${ARG_NEXT_USER_PASSWORD}" > /etc/bandit/${ARG_NEXT_USER_USERNAME}/password

RUN echo "${ARG_NEXT_USER_PASSWORD}" | openssl aes-256-cbc -a -pass pass:${NEXT_USER_PASSWORD_KEY}> /home/${ARG_NEXT_USER_USERNAME}/encrypted.txt
RUN chfn -o "In case I forget my password, I left a hint in ~." ${ARG_NEXT_USER_USERNAME}
RUN echo "I used the following to command to encrypt my password: 'echo [mypassword] | openssl aes-256-cbc -a -pass pass:${NEXT_USER_PASSWORD_KEY}'" > /home/${ARG_NEXT_USER_USERNAME}/note.txt
