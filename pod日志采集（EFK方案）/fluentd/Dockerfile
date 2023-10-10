FROM fluent/fluentd:v1.16.2-debian-1.1
USER root
ADD GeoLite2-City.mmdb /fluentd/GeoLite2-City.mmdb
RUN buildDeps="build-essential libgeoip-dev autoconf automake libtool libffi-dev" \
    && sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y --no-install-recommends $buildDeps \
    && gem sources --add https://gems.ruby-china.com/ --remove https://rubygems.org/ \
    && fluent-gem install fluent-plugin-elasticsearch fluent-plugin-geoip fluent-plugin-rewrite-tag-filter \
    && apt-get autoclean \
    && gem sources --clear-all \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem