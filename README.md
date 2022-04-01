# CDL-prereq
Pre-requisite case study for applying for NU CDL student researcher position

## Task 1: Kubernetes pod creation

`back` and `front` folder each contains files needed to create each of the pod, service connecting the pod, and docker image that the pod runs on. On the home page of each of pod, one should be able to see "Hello world! This is front/back end".

`command.txt` keeps track of all the K8s and docker commands utilized in this task

Issue: When exposing services with command `minikube service --all`, I always receive this error message:

```
🏃  Starting tunnel for service frontend.
🏃  Starting tunnel for service hello.
🏃  Starting tunnel for service kubernetes.
❗  Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
```

## Task 2: MNIST classification with TF2

`CDL_Tensorflow_MNIST.ipynb` notebook includes the code and outputs for this task.

## Task 3: Deploy MongoDB onto K8s

All files for this task is stored under `mongo-flask` folder. Code from creating docker images to deploying the Mongo-flask app can be found in `mongo-flask/commands-mongo.txt`. 

Reference: [Deploy your first Flask+MongoDB app on Kubernetes](https://levelup.gitconnected.com/deploy-your-first-flask-mongodb-app-on-kubernetes-8f5a33fa43b4)


## Video demo

`demo_K8s.mp4` is the demo video for Task 1, `demo_MNIST.mp4` is for Task 2, and `demo_MongoDB.mp4` is for Task 3.

