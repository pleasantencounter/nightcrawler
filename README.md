# nightcrawler

Welcome to the Interview Questions Project repository! This project aims to be a comprehensive resource for technical interviews.

> **IMPORTANT>** The tools you'll use in these exercises have a -h or --help command you can leverage if you are unsure how to proceed.

## Requirements

- kubernetes cluster (k3d,minikube,etc..)
- container runtime (docker,containerd,podman)
- helm
- git
- python

## Python exercise

**API KEY**: 3b93dbe006af066f0a0db26c13d3a15c

**API DOCS**:

- https://openweathermap.org/api/geocoding-api
- https://openweathermap.org/current

1. Setup a new python virtual enviroment and activate it
2. Within the virtual environment, install the package requirements file `python/requirements`
3. Set up an environment variable `OW_API` with the API KEY above as the value
4. Execute the `python/weather.py` script and resolve any errors
    1. Errors are printed to stdout as stack traces.
    2. The script produces a blank output when there are no errors.
    3. You may use print statements for debugging and/or refer to the API docs
5. Add a new, optional command line argument `--units` to the script for unit of measurement
    1. View the api docs for units
    2. Use the same default specified in the API docs
    3. Add the new argument as a parse arg after the existing two (e.g.`--zip`, `--country`)
6. Update endpoint url located in the `get_daily_weather` function to include units using the parse arg created in the previous step
7. Create a new function `get_weather_string` that returns a string containing the following data fields: `temp`, `temp_min`, `temp_max`, `wind speed`, and `weather description`
    1. This function should leverage the response in `get_daily_weather`
    2. View the API docs for the response JSON
    3. Only include the first weather description
    4. You may modify `get_daily_weather` if necessary
8. Call the new function and print out the result

## Docker exercise

1. View the Dockerfile in `images/nginx-http`
2. Create a file `hello.txt` with the contents "Hello World!"
3. Place the new file within the `/nginx/files` directory
4. Build the Dockerfile and tag image as `nginx:nightcrawler`
5. Run docker image exposing port 8080
6. Access http server on localhost and view your `hello.txt` file

## Helm Chart exercise
**Service Docs**: https://kubernetes.io/docs/concepts/services-networking/service/


1. Resolve issues with helm chart, there are multiple problems to fix
2. Add a NodePort service manifest to helm chart that will expose the nginx deployment
4. Name the service the same name as the deployment
5. Deploy the helm chart and curl the service

## K8s Imperative exercise

1. Create pod with name nginx in the namespace `interview` using image `nginx:latest`
2. Check the logs of the pod

## K8s Declaritive exercise

**Init Container Docs**: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/

1. Create a deployment manifest with the name httpd use the container `httpd:latest`
2. Add an init container to the manifest that uses the `busybox` image to `echo hello world`

## Git exercise

1. Create a branch
2. Commit changes to branch
3. Run `git log` to check the commit history
