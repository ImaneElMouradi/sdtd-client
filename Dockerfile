FROM centos:latest

RUN yum -y update;
RUN yum -y clean all;

#SET UP THE ENVIRONNEMENT
RUN yum install -y  wget dialog curl sudo lsof vim telnet nano openssh-server openssh-clients bzip2 passwd tar bc git unzip
#INSTALL JAVA 1.8
RUN yum install -y java-1.8.0-openjdk java-1.8.0-openjdk-devel 

#CREATE USER
RUN useradd guest -u 1000
RUN echo guest | passwd guest --stdin


# #INSTALL PYTHON 3.6 
RUN yum install -y python36

#INSTALL PYTHON3 DEPENDENCIES 
RUN pip3 install kafka-python numpy

ENV HOME /home/guest
WORKDIR $HOME







# SET ENVIRONNEMENT ALIASES 
ADD setenv.sh /home/guest/setenv.sh
RUN chown guest:guest setenv.sh
RUN echo . ./setenv.sh >> .bashrc




# ADD THE PYTHON SCRIPTS THAT MOCKS THE PRODUCER
ADD country_crimes.py /home/guest/country_crimes.py
RUN chmod +x /home/guest/country_crimes.py




# RUN THE STARTUP SCRIPT
#CMD [ "bash", "startup_script.sh" ]
