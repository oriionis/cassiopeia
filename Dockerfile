######################################################################
#
# Image for MWL Backend
#
######################################################################
FROM python:2.7
RUN pip install virtualenv

# Create Virtual Env and install python dependencies
COPY requirements.txt /home/gdrive/
WORKDIR /home/gdrive
RUN virtualenv server-env
RUN ["/bin/bash", "-c" ,"source server-env/bin/activate"]
RUN pip install -r requirements.txt

# Copy the Source code...
WORKDIR /home/gdrive
COPY *.py /home/gdrive/
COPY config/* /home/gdrive/config/

COPY ./docker-entry-point.sh .
ENTRYPOINT ["./docker-entry-point.sh"]
