# Docker-related Materials

This repository shows useful commands which will help faciliate the development of docker-related projects.

<!-- https://stackoverflow.com/questions/55931321/docker-mysql-connection-dbeaver -->

## Sample files


## Docker Commands

### Image-related commands
- List all docker images
    - `docker images -a`
- Remove docker image
    - `docker rmi <image_id>`
- Remove all docker images
    - `docker rmi -f $(docker images -aq)` *(linux)*
    - `for /F %i in ('docker images -a -q') do docker rmi -f %i` *(windows)*

### Container-related commands
- List all docker containers
    - `docker ps -a`
- Stop running container
    - `docker stop <container_id>`
    - `docker stop -f $(docker ps -aq)` *(linux)*
    - `for /F %c in ('docker ps -a -q') do (docker stop %c)` *(windows)*
- Remove docker container
    - `docker rm <container_id>`
- Remove all docker containers (**Note**: You have to stop the container first before removing)
    - `docker rm -f $(docker ps -aq)` *(linux)*
    - `for /F %c in ('docker ps -a -q') do (docker rm %c)` *(windows)*

### Others
```sh
docker volume ls
docker network ls
# Start Docker Service (detached)
docker compose -f pgvector.yml up -d
# End Docker Service
docker compose -f pgvector.yml down -v
docker compose -f pgvector.yml stop
```

# Pruning
Remove all unused containers, networks, images (both dangling and unreferenced), and optionally, volumes. [reference](https://docs.docker.com/engine/reference/commandline/system_prune/)

- `docker system prune`
- `docker container prune`
- `docker image prune`
- `docker network prune`
- `docker volume prune`
- Prune dangling volume
    - `docker volume rm $(docker volume ls -qf dangling=true)`

# Minikube and Kubernetes
- installation: [link](https://minikube.sigs.k8s.io/docs/start/?arch=%2Fmacos%2Farm64%2Fstable%2Fhomebrew)
    ```sh
    brew install minikube   # install kubectl as well
    brew install kubectx    # optional
    minikube addons enable ingress # https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/
    kubectl get pods -n ingress-nginx # check ingress controller is running
    minikube dashboard
    ```
- Components
    - node (replicas through deployment)
        - Master
        - Worker
    - pods
    - service (permanent IP and load balancing)
        - ClusterIP (default)
        - headless  (communicate directly to specific pod)
        - NodePort  (External traffic is accessible to node - port: 30000-32767)
        - LoadBalancer (similar to NodePort but external traffic do not have direct access to internal pod)
    - ingress
    - configmap
    - secrets
    - volumes (data persistance) - [link](https://gitlab.com/nanuchi/youtube-tutorial-series/-/tree/master/kubernetes-volumes)
        - persistent volume (cluster resource -> localdisk or nfs server or cloud storage)
        - persistent volume claim (subset of PV for pod to claim)
        - storage class (dyanmically provision storage)
    - deployment vs statefulset
        - `Deployment` manages a `ReplicaSet` which manages `Pods` which is an abstraction of `Container`
- minikube
    ```sh
    minikube start # check drivers if it fails to start
    minikube status
    minikube service <SERVICE>  # assign external ip to service (loadbalancer type)
    ```
- Kubens
    ```sh
    kubens              # check default namespace
    kubens <NAMESPACE>  # switch default namespace
    ```
- Kubectl
    - Basic
    ```sh
    kubectl version
    kubectl get all
    kubectl get nodes
    kubectl get pod                         # -l app=frontend, -o wide (get more output like IP addr), --watch (see live updates)
    kubectl get services    
    kubectl get deployment                  # -o yaml
    kubectl get replicaset  
    kubectl get configmap
    kubectl get ingress
    kubectl get ns
    kubcetl logs <POD>
    kubectl describe pod <POD>
    kubectl exec -it <POD> -- bin/bash      # start a terminal inside pod
    kubectl get namespace
    kubectl create namespace <namespace_name>
    kubectl cluster-info
    kubectl api-resources --namespaced=false
    ```
    - Manage deployment (or things under it - pod,replicaset)
    ```sh
    kubectl create deployment NAME --image-image    # naive way of creating (use config file instead of inline command)
    kubectl apply -f <FILE>                         # standard way of applying config yaml file
    kubectl edit deployment NAME                    # edit deployment (yaml)
    kubectl delete deployment NAME
    kubectl delete -f <FILE>
    ```
- Considerations
    - Secrets accept only values which are base-64 encoded.
        ```sh
        echo -n 'password' | base64     # output to be copied: dXNlcm5hbWU=
        ```
    
- Resources
    - [Labels and selectors](https://devtron.ai/blog/kubernetes-labels-and-selectors-a-definitive-guide-with-hands-on/)

# Accessing
[public-key-retrieval-is-not-allowed](https://stackoverflow.com/questions/50379839/connection-java-mysql-public-key-retrieval-is-not-allowed)

For DBeaver users:
- Right click your connection, choose "Edit Connection"
- On the "Connection settings" screen (main screen) click on "Edit Driver Settings"
- Click on "Connection properties", (In recent versions it named "Driver properties")
- Right click the "user properties" area and choose "Add new property"
- Add two properties: "useSSL" and "allowPublicKeyRetrieval"
- Set their values to "false" and "true" by double clicking on the "value" column