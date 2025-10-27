# frist  build the docker image and then push it to the repo 
  docker build -t erfanashraafi/fastapi-app:latest .
  docker push erfanashraafi/fastapi-app:latest

# then creat namespace names fastapi-app and deploy the deployment file on it also expose the service file 
  * k = kubectl
  k create namespace fastapi-app
  k apply -f deployment.yaml -n fastapi-app
  k apply -f service.yaml -n fastapi-app

# we can change the replica to 1 
  k scale -n fastapi-app deployment/fastapi-app --replicas=1

# we can describe our pod to see event and logs and some info about it 
  k describe pod -n fastapi-app fastapi-app-769ccccb75-r64kh  
    
    Name:             fastapi-app-769ccccb75-r64kh
    Namespace:        fastapi-app
    Priority:         0
    Service Account:  default
    Node:             minikube/192.168.49.2
    Start Time:       Mon, 27 Oct 2025 12:35:02 +0330
    Labels:           app=fastapi-app
                      pod-template-hash=769ccccb75
    Annotations:      <none>
    Status:           Running
    IP:               10.244.0.163
    IPs:
      IP:           10.244.0.163
    Controlled By:  ReplicaSet/fastapi-app-769ccccb75
    Containers:
      fastapi:
        Container ID:   docker://45b91aae8f13fb3c8e4d23d5369859de273414b098cf720feaec05bb763065d9
        Image:          erfanashraafi/fastapi-app:latest
        Image ID:       docker-pullable://erfanashraafi/fastapi-app@sha256:322aa633cb526dcac990620afcc282496923f30239f3c29f749f7b56720277bc
        Port:           8000/TCP
        Host Port:      0/TCP
        State:          Running
          Started:      Mon, 27 Oct 2025 12:35:05 +0330
        Ready:          True
        Restart Count:  0
        Limits:
          cpu:     500m
          memory:  128Mi
        Requests:
          cpu:      250m
          memory:   64Mi
        Liveness:   http-get http://:8000/health delay=30s timeout=1s period=10s #success=1 #failure=3
        Readiness:  http-get http://:8000/health delay=5s timeout=1s period=5s #success=1 #failure=3
        Environment:
          PYTHONUNBUFFERED:  1
        Mounts:
          /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-ndwnx (ro)
    Conditions:
      Type                        Status
      PodReadyToStartContainers   True 
      Initialized                 True 
      Ready                       True 
      ContainersReady             True 
      PodScheduled                True 
    Volumes:
      kube-api-access-ndwnx:
        Type:                    Projected (a volume that contains injected data from multiple sources)
        TokenExpirationSeconds:  3607
        ConfigMapName:           kube-root-ca.crt
        Optional:                false
        DownwardAPI:             true
    QoS Class:                   Burstable
    Node-Selectors:              <none>
    Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
    Events:
      Type    Reason     Age   From               Message
      ----    ------     ----  ----               -------
      Normal  Scheduled  22m   default-scheduler  Successfully assigned fastapi-app/fastapi-app-769ccccb75-r64kh to minikube
      Normal  Pulling    22m   kubelet            Pulling image "erfanashraafi/fastapi-app:latest"
      Normal  Pulled     22m   kubelet            Successfully pulled image "erfanashraafi/fastapi-app:latest" in 2.519s (2.519s including waiting). Image size: 149562501 bytes.
      Normal  Created    22m   kubelet            Created container: fastapi
      Normal  Started    22m   kubelet            Started container fastapi
