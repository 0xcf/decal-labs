FROM fedora:latest

RUN yum update -y && yum install python3-pip && \
    pip3 install --upgrade pip && \
    pip3 install pyfiglet termcolor

ADD missile.py /
CMD ["/usr/bin/python3.6", "missile.py"]
