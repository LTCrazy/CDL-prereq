FROM python:latest
RUN apt-get update -y
COPY backend.py .
RUN pip install Flask
EXPOSE 80 5000

#CMD [/usr/sbin/nginx -g "daemon off;"]
#RUN python3 -m virtualenv env && source env/bin/activate
#CMD [/usr/sbin/nginx -g "daemon off;"]
CMD ["python3", "backend.py"]

ENTRYPOINT ["python3", "backend.py"]
#ENTRYPOINT ["/bin/sh", "-c"]
