import logging
import os
import requests
import subprocess
import time

from cloudevents.http import from_http
from flask import Flask, request
from kubernetes import client, config


app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

EVENT_TYPES = ("dev.knative.apiserver.resource.add",)
SERVICE_PORT = 5000
SERVICE_NAMESPACE = "open-cluster-management-agent"
SERVICE_ACCOUNT = "klusterlet-work-sa"
PULL_SECRET = "physics-harbor-pullsecret"
MANIFEST_WORK_SEMANTICS = "cluster-registration-semantics"
MANIFEST_WORK_ENERGY = "cluster-registration-energy"
ENERGY_JOB = 'energy-semantics'
SEMANTIC_SERVICE = 'service-semantics'

# create an endpoint at http://localhost:/8080/
@app.route("/", methods=["POST"])
def home():
    # create a CloudEvent
    event = from_http(request.headers, request.get_data())

    # we are only interested on the omboarding of new clusters,
    # not in the updates or removal
    event_type = event['type']
    app.logger.info('The event type is %s', event_type)
    return "", 204
    # filter by event type (only "add" event is needed)
    # if event_type not in EVENT_TYPES:
    #    return "", 202

    replicas = len(v1.list_pod_for_all_namespaces (label_selector="scale=true").items)
    print("Scaling to " + str(replicas) + " replicas ...")
    subprocess.run(["kubectl", "-n", "openshift-machine-api", "scale",  "--replicas="+str(replicas), "machineset/ocphub-t4rh8-worker-eu-north-1b"])
    return "", 204

if __name__ == "__main__":
    app.run(port=8080)
