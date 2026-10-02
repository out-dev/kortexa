

Local Kubernetes Cluster Setup
===============================

This repository uses kind to set up a local Kubernetes cluster for development purposes.
First, ensure you have Docker or Podman installed on your system. If you use Podman, ensure rootless mode is properly configured.

Install kind using the official installation guide: https://kind.sigs.k8s.io/docs/user/quick-start/.
Navigate to the directory containing the cluster configuration file k8s/kind/cluster/cluster-config.yaml.
Execute the following command to create the cluster:

.. code-block:: console

   kind create cluster --config=cluster-config.yaml

We use traefik as the ingress controller for the local Kubernetes cluster. First install the missing Gateway API CRDs.

.. code-block:: console

   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.6.2/standard-install.yaml
   kubectl wait --for=condition=Established --timeout=60s crd/gatewayclasses.gateway.networking.k8s.io crd/gateways.gateway.networking.k8s.io

Wait until the Gateway API CRDs are established before proceeding. Then you can install Traefik as the ingress controller.
Follow the official Traefik installation guide for the next steps https://doc.traefik.io/traefik/getting-started/install-traefik/.

To simulate a cloud provider for the local Kubernetes cluster, we use coud-provider-kind https://github.com/kubernetes-sigs/cloud-provider-kind. 
Clone the repository and build a new executable for you host. 

.. code-block:: console

   git clone https://github.com/kubernetes-sigs/cloud-provider-kind.git
   cd cloud-provider-kind
   go install sigs.k8s.io/cloud-provider-kind@latest
   cd ./bin
   ./cloud-provider-kind

Check your traefik load balancer:      

.. code-block:: console

   kubectl get services -n traefik

If everything worked correctly, you should see the Traefik service listed with an external IP or a load balancer IP.

To get a nice name resolution we use CoreDNS. Download CoreDNS https://github.com/coredns/coredns and run 

.. code-block:: console

   coredns -conf=k8s/core-dns/config

You can test your local setup by accessing https://dashboard.out-dev.localhost/dashboard/ you should see the Traefik dashboard.







