# Elastic Container Service (ECS)
Amazon Elastic Container Service (ECS), also known as Amazon EC-2 Container Service, is a managed service that allows users to run Docker-based applications packaged as containers across a cluster of EC2 instances. Running simple containers on a single EC-2 instance is simple but running these applications on a cluster of instances and managing the cluster is being administratively heavy process. With ECS, Fargate launch type, the load, and responsibility of managing the EC2 cluster is transferred over to the AWS and you can focus on application development rather than management of your cluster architecture.

In simple terms, containers are like lightweight, self-contained packages that include everything an application needs to run, such as code, libraries, and dependencies. AWS ECS allows customers to run and manage these containers in the cloud, making it easier to deploy and scale applications.

In a typical scenario where AWS ECS applies, a company wants to run their applications in the cloud using containers. They might have several applications that need to be run together, and they want to manage them as a group. With AWS ECS, the company can easily create a cluster of virtual machines (called EC2 instances) and deploy their containers onto the cluster.

AWS ECS provides features like load balancing, auto scaling, and monitoring to help customers manage their applications at scale. For example, if an application receives more traffic than expected, AWS ECS can automatically add more containers to handle the increased load.

Overall, AWS ECS makes it easier for customers to manage their containerized applications in the cloud, allowing them to focus on building and running their business instead of managing infrastructure.

## Key-terms

 - **Container**: A container is a package that holds an application and everything(dependencies, libraries etc.) the application requires to run. Containers are independent of the underlying operating system and hence container applications are fairly portable, flexible, and scalable. This ensures the application will run always as expected irrespective of the system and environment in with a container is run.
 - **Docker**: Docker is a software that facilitates and automates installation and deployment of applications inside Linux containers.
 - **Cluster**: A logic group of EC2 instances running as a single application.
 - **Container Instance**: Each EC2 in an ECS Cluster is called a container instance.

## Opdracht
### Gebruikte bronnen

https://www.trianz.com/insights/ecs-vs-ec2

https://www.techtarget.com/searchaws/definition/Amazon-EC2-Container-Service

https://www.geeksforgeeks.org/introduction-to-amazon-elastic-container-service-ecs/

### Ervaren problemen
Geen problemen ervaren

### Resultaat

### What is ECS used for?

Amazon ECS is best used with:

 - **Machine learning**: Machine learning (ML) models can be easily containerized for training and inference with Amazon ECS. ML models can be created with loosely coupled, distributed services that can be placed on a variety of platforms or close to the data being analyzed by the application.
 - **Microservices**: Amazon ECS assists in the operation of microservices applications by providing native integration to AWS and enabling continuous integration and continuous deployment (CI/CD) pipelines.
 - **VMs**: The Amazon Elastic Compute Cloud (Amazon EC2) web service can create and operate Linux VMs in the cloud -- these VMs are called instances. Developers can specify rules for the isolated sets of EC2 instances that run on top of a host OS which increase computing performance and portability.
 - **Migrating apps to the cloud**: Legacy enterprise applications can be feasibly containerized and migrated to Amazon ECS without necessitating any code changes. This is an expression of lift-and-shift application migration.
 - **Batch processing**: Batch workloads can run with custom or managed schedulers on AWS On-Demand Instances, Reserved Instances or Spot Instances.

### How Amazon Elastic Container Service works

With Amazon ECS, developers can pull the necessary Docker images and resources from Amazon Elastic Container Registry (ECR), or other repositories, to define their application. The ECS service then ingests container images and  arranges or composes containers and resources into an application. Once all the appropriate containers are gathered and services implemented, the containers are deployed either on EC2 or AWS Fargate. Finally, Amazon ECS scales the application and continuously manages the availability of containers.

AWS account holders can integrate the ECS service with other Amazon Web Services, such as:

- AWS CloudTrail logs
- AWS Command Line Interface (AWS CLI)
- Amazon EC2
- AWS CloudFormation templates
- AWS SDKs
- AWS Tools for Windows PowerShell
- Amazon ECR

### ECS launch types

Amazon ECS launches containers through _Fargate_ or _EC2_.

 - **Fargate**: The Fargate launch type offers a serverless computing alternative that provisions, launches and runs containers without the need to manage the underlying infrastructure. Fargate is best for small, batch or highly scalable -- that is, burstable -- workloads with relatively short time-to-live (TTL) requirements.

 - **EC2**: The EC2 launch type is a more traditional deployment option. Users can provision and deploy EC2 instances to run containers while the service manages the related infrastructure and services. EC2 is well-suited for larger and more demanding workloads, applications that require persistent storage, applications that benefit from careful resource tuning or configuration and where direct management of the AWS infrastructure is desired.
Amazon Elastic Container Service features

- **Scheduling**: Schedulers place containers over clusters according to the desired resources -- such as RAM or CPU -- and availability requirements. This feature can be used to schedule batch jobs and long-running applications or services.

Amazon ECS includes two schedulers to deploy containers based on computing needs or availability requirements. AWS Blox, an open source container orchestration tool, integrates with ECS to schedule containers. Long-running applications and batch jobs benefit from the use of schedulers for their responsiveness; ECS also supports third-party scheduling options.

- **Docker integration**: Amazon ECS supports Docker, which enables AWS users to manage Docker containers across clusters of Amazon EC2 instances. Each EC2 instance in a cluster runs a Docker daemon that deploys and runs any application packaged as a container locally on Amazon ECS without the need to make any changes to the container.

- **Networking**: Amazon ECS supports Docker networking, as well as integration with Amazon Virtual Private Cloud (Amazon VPC), to provide isolation for containers. This provides developers with control over how the containers interact with other services and external traffic. There are four networking modes available for the containers; each one supports different use cases. The modes include:

  - **Host mode**: Adds containers directly to the host's network stack and exposes containers on the network that are not isolated.
  - **Task networking mode**: Assigns every running Amazon ECS task a dedicated elastic networking interface which provides the containers with full networking features in Amazon VPC similar to EC2 instances.
  - **None mode**: Deactivates external networking for containers.
  - **Bridge mode**: Creates a Linux bridge to connect all containers operating on the host in a local virtual network and accessed through the host's default network connection.

- **Cluster management**: Amazon ECS handles all of the cluster management processes for the developer. This typically involves installing, operating and scaling cluster management software, monitoring solutions and configuration management systems, as well as building the architecture and managing the availability and scalability of each system. With Amazon ECS, the developer simply launches a cluster of container instances and specifies the desired tasks to perform.

- **Task definitions**: Users define tasks through a declarative JSON template called a Task Definition. The Task Definition lets developers specify which containers they need for their task, including memory and CPU requirements, Docker repository and images, and shared data volumes, and also choose how the containers connect to each other. Task Definition files also enables developers to version control their application specification.

- **Load balancing**: Integration with AWS ELB lets developers to distribute traffic across containers. They can specify the Task Definition and ELB to use, and then the Amazon ECS scheduler automatically adds and removes containers using the ELB.

- **Repository support**: Developers can use any third-party repository, accessible private Docker registry or Docker Hub with Amazon ECS as long as it is specified in the Task Definition.

- **Local development**: The AWS CLI lets users simplify the local development experience and set up an Amazon ECS cluster and its related resources. The CLI also supports Docker Compose, an open source tool used to define and run multicontainer applications.

- **Programmatic control**: Various simple APIs let developers integrate and extend the Amazon ECS service. With APIs, users can create or delete clusters, launch or destroy Docker containers and register or unregister tasks, as well as access detailed information about the state of the cluster and its instances. Developers can also use AWS CloudFormation to deliver Amazon ECS clusters, register Task Definitions and schedule containers.

- **Logging**: Amazon CloudWatch Logs receives every container instance's ECS agent logs and Docker container logs for issue diagnosis. All Amazon ECS API calls can also be recorded and the log files will be delivered to the user through AWS CloudTrail.

- **Monitoring**: Monitoring capabilities check the health of containers and clusters. Average and aggregate CPU can be supervised, as well as the memory utilization of running tasks grouped by Task Definition, service or cluster through Amazon CloudWatch. Furthermore, users can set CloudWatch alarms to alert developers whenever a container or cluster needs to be scaled up or down.

- **Container deployments**: Whenever a new version of the application Task Definition is uploaded, the Amazon ECS scheduler automatically starts new containers using the updated image and disables any container running on the old version. Amazon ECS will also register and unregister the appropriate new and old containers from the AWS ELB.

- **Container auto-recovery**: Amazon ECS service scheduler automatically recovers unhealthy containers. This ensures the necessary number of containers are constantly supporting the application.

- **Container security**: EC2 instances reside in the Amazon VPC and a user can specify which instances are exposed to the internet. EC2 instances and ECS tasks also adhere to IAM roles, while security groups and network access control lists limit access to instances.
Benefits of Amazon Elastic Container Service

Amazon ECS is a beneficial choice for modern software teams that are smaller and cross-functional because it is simple and fast to set up and start running. Furthermore, since it is a fully managed platform from AWS, users do not have to worry about dealing with platform-related issues, and can instead focus on migrating their app.

Other benefits include:

  - **Improved security**: Amazon ECR and ECS collaborate to provide optimal application security.
  - **Cost efficient**: Amazon ECS lets developers schedule various containers on the same node, which achieves high density on Amazon EC2.
  - **Performance at scale**: Amazon ECS can launch thousands of Docker containers in seconds without any additional complexity.
  - **Improved compatibility**: The container-based pipeline helps eliminate any issues that may arise due to deployments functioning differently in various environments.
  - **Designed for collaboration**: Integration of Amazon ECS with other AWS services, such as Amazon ECR and AWS ELB, provides users with a complete offering for running a variety of containerized applications and services.
  - **Manageable at any scale**: With Amazon ECS, it is unnecessary to operate cluster management software and create fault-tolerant clusters. Since there is no software to install, scale or manage, developers can focus on building their container-based applications.
  - **Extensible**: Amazon ECS offers total visibility and control of AWS resources, thus enabling it to be easily integrated or extended through APIs.


### Amazon Elastic Container Service pricing

There is no additional cost to AWS customers for using ECS. That said, users employing the EC2 launch type pay for EC2 instances and EBS volumes in the cluster plus any other billable AWS resources used in conjunction with the containerized application.

Users that choose the Fargate launch type pay for the memory and vCPU provided to the container for the duration of its operation -- rounded up to the nearest second. Amazon ECS on AWS Outposts obeys the same pricing rules as the Amazon EC2 launch type.
