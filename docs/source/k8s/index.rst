

Install docker or Podman
Follow the official installation guide for Docker: https://docs.docker.com/get-docker/
Or for Podman: https://podman.io/getting-started/installation
If you use Podman ensure rootless mode is properly configured.

Install kind
Follow the official installation guide for kind: https://kind.sigs.k8s.io/docs/user/quick-start/
and execute command kind create cluster --config=cluster-config.yaml

Install the Gateway API CRDs before Traefik
The Traefik configuration creates ``Gateway`` and ``GatewayClass`` resources.
Install the Gateway API CRDs before installing the Traefik Helm chart:

.. code-block:: console

   kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.6.2/standard-install.yaml
   kubectl wait --for=condition=Established --timeout=60s crd/gatewayclasses.gateway.networking.k8s.io crd/gateways.gateway.networking.k8s.io

Install Traefik as the cluster's ingress controller
Follow the official Traefik installation guide: https://doc.traefik.io/traefik/getting-started/install-traefik/

openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=*.docker.localhost"
kubectl create namespace traefik
kubectl create secret tls local-selfsigned-tls --cert=tls.crt --key=tls.key --namespace traefik
helm install traefik traefik/traefik --namespace traefik --values values.yaml