FROM ubuntu:20.04


ENV TZ=America/New_York DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && apt-get upgrade -y
RUN yes | unminimize
RUN apt-get install ubuntu-minimal -y
RUN apt-get install openssh-server -y
RUN apt-get install python3-pip -y
RUN apt-get install python3-venv -y
RUN apt-get install vsftpd -y
RUN apt-get install knockd -y
RUN apt-get install ufw -y

RUN mkdir -p /var/run/vsftpd/empty && mkdir -p /etc/vsftpd && mkdir -p /var/ftp && mv /etc/vsftpd.conf /etc/vsftpd.orig && mkdir -p /etc/service/vsftpd

COPY vsftpd.conf /etc/vsftpd.conf

WORKDIR /opt

# COPY BABYSHARK C2
COPY BabyShark BabyShark
RUN pip3 install -r BabyShark/requirements.txt
COPY --chmod=777 entrypoint.sh /entrypoint.sh

COPY knockd.conf /etc/knockd.conf
COPY tcpdump/tcpdump.pcap /var/ftp/knock-knock.pcap
COPY note.txt /var/ftp/note.txt 

EXPOSE 20-21
EXPOSE 65500-65515
EXPOSE 420
EXPOSE 64821
EXPOSE 57492
EXPOSE 26356

ENTRYPOINT ["/entrypoint.sh"]

