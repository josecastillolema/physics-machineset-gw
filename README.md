# physics-machineset-gw
Knative source to sink service to trigger machineset scales upon KEDA deployment scales

## Deploy

The steps to deploy it are:

* Deploy a knative service too, so that the application is
  scaled to 0 when not used, since cluster registration is sporadic action and
  this could lead to saving resources

```
oc apply -f deploy/004b-sink.yaml
```

* Create the knative ApiServerSource by running the command:

```
oc apply -f deploy/005-apiserversource.yaml
```

## Logic for the application

* Receive the notification event about a new dummy deployment being scaled by KEDA

* Scale the machineset accordingly

## Create a container from the application at cluster-registration folder

To build the a new image of the sink application, just run: 

```
$ docker build -t quay.io/myuser/machineapi-gw:latest -f Dockerfile .
```

### Push the image to your registry

```
$ docker login -u myuser quay.io
$ docker push quay.io/myuser/machineapi-gw:latest

```

