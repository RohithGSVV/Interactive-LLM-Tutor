FROM python:3.9-slim
# RUN echo 'deb http://deb.debian.org/debian testing main' >> /etc/apt/sources.list \
#     && apt-get update && apt-get install -y --no-install-recommends -o APT::Immediate-Configure=false gcc g++

RUN apt-get update &&  apt install -y python3-ldap
WORKDIR /app

COPY . /app

# RUN pip install # python-ldap

CMD ["python", "ldap_auth_daemon.py"]