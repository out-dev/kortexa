Backend Helm Chart
==================

The local development chart is in ``k8s/helm/backend``. It runs the backend
using Django's development server, so it is not intended for production.

Run DevSpace from the repository root to build the backend image, deploy the
chart, synchronize backend source files, and forward port 8000::

   devspace dev -n kortexa

Build and load the image into a local kind cluster, then install the chart::

   docker build -t kortexa-backend:dev .\backend
   kind load docker-image kortexa-backend:dev
   helm upgrade --install kortexa .\k8s\helm\backend --namespace kortexa --create-namespace

Forward the service port to access the backend from the host::

   kubectl port-forward -n kortexa service/kortexa 8000:8000

Set deployment configuration in ``values.yaml``. Add environment entries
there to customize Django settings or reference Kubernetes Secrets without
storing secret values in the chart.
