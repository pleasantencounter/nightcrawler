# nightcrawler
Welcome to the Interview Questions Project repository! This project aims to be a comprehensive resource for technical interviews.

## Requirements
* kubernetes cluster (k3d,minikube,etc..)
* container runtime (docker,containerd,podman)
* helm
* git
* python

## Python exercise

**API KEY**: 3b93dbe006af066f0a0db26c13d3a15c

**API DOCS**:
* https://openweathermap.org/api/geocoding-api
* https://openweathermap.org/current

1. Setup python virtual envrionment
2. Activate virtual env and install `python/requirements` modules
3. Set Linux virtual env `OW_API` with the API KEY above as the value
4. Execute the script and resolve issues with script
5. Add parse arg for unit of measurement, look at api docs for units
6. Update endpoint located in the get_daily_weather function to request unit using the parse arg created in the previous step
7. Create a new function that returns a string with the following data: temp, temp_min, temp_max, wind speed, and weather description
8. Print out data above

## Docker exercise

1. Create test file with the string "Hello World!" in the Dockerfile within the `/nginx/files` directory
2. Build Dockerfile and tag image
3. Run docker image targetport 8080
4. Access http server on localhost

## Helm Chart exercise

1. Resolve issue with helm chart
2. Add service manifest to helm chart that will expose nginx deployment
3. Deploy helm chart and curl service

## K8s Imperative exercise
1. Create pod with name nginx in the namespace `interview` using image `nginx:latest`
2. Check the logs of the pod

## K8s Declaritive exercise
1. Create a deployment manifest with the name httpd use the container httpd:latest
2. Add an init container to the manifest using a python container that prints `hello world`

## Git exercise
1. Create a branch
2. Commit changes to branch
3. Run `git log` to check the commit history

# Test