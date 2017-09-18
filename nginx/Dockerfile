# --------------------------------------------------------------------------
# When Docker builds the nginx container, it builds it from this image.
#
# This file pulls a nginx image from Docker Hub (a sort of
# GitHub for Docker images), and copies NGINX config files to the container.
# --------------------------------------------------------------------------

FROM nginx:1.13.0

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf
COPY app.conf /etc/nginx/conf.d/