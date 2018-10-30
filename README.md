# cassiopeia

## Build the docker image.
docker build -t [repos]/[image]:[label] . 

After the docker image has been built, it can be deployed to the server where other components are running, the Nginx and the 
OHIF Viewer.

If Credentials have to be changed update the files in the config folder.
