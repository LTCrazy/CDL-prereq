FROM python:latest
RUN apt-get update -y
COPY frontend.py .
RUN pip install Flask
EXPOSE 80 6000

#CMD [/usr/sbin/nginx -g "daemon off;"]
#RUN python3 -m virtualenv env && source env/bin/activate
#CMD [/usr/sbin/nginx -g "daemon off;"]
CMD [python3 frontend.py]

ENTRYPOINT ["python3", "frontend.py"]
#ENTRYPOINT ["/bin/sh", "-c"]


# docker run -p 5000:6000 flask-front:latest