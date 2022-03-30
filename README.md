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

## Video demo

`demo_K8s.mp4` is the demo video for Task 1 and `demo_MNIST.mp4` is for Task 2.

