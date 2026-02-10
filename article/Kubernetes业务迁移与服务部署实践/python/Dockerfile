FROM rockylinux:8
RUN dnf -y install wget gcc gcc-c++ net-tools telnet iproute procps tcpdump python38 python38-devel
ADD project /project
RUN pip3.8 install -r /project/requirements.txt -i https://pypi.doubanio.com/simple
WORKDIR /project
CMD ["python3.8","main.py"]