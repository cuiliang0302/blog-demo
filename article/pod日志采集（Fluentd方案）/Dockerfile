FROM fluentd:v1.16-debian-1
USER root
RUN apt-get update && apt-get install -y build-essential libgeoip-dev autoconf automake libtool libffi-dev && apt-get autoclean
ADD GeoLite2-City.mmdb /fluentd/GeoLite2-City.mmdb
RUN fluent-gem install fluent-plugin-elasticsearch && fluent-gem install fluent-plugin-geoip && rm -rf /var/lib/apt/lists/* /var/cache/debconf/* /var/log/* /var/tmp/*