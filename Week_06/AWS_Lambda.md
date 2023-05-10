# Lambda
AWS Lambda lets customers run code in the cloud without having to worry about provisioning and managing servers. Customers can upload their code to AWS Lambda and it will automatically run in response to specific events or requests.

In a typical scenario where AWS Lambda applies, a company is using AWS to run their applications and services in the cloud. They want to be able to run code in response to certain events, such as a file being uploaded to an S3 bucket or a message being sent to an SQS queue.

With AWS Lambda, the company can upload their code to the service and configure it to run in response to specific events or requests. For example, they might create a Lambda function that processes an image when it is uploaded to an S3 bucket, or a function that sends an email when a message is received in an SQS queue.

By providing customers with a way to run code in the cloud without having to manage servers, AWS Lambda makes it easier and more cost-effective to build and run applications and services.

## Key-terms

 - **AWS Serverless Application Model (SAM)**: an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings.

 - **Function**: The code that runs in AWS Lambda in response to an event or request. A function is a program or a script which runs in AWS Lambda. Lambda passes invocation events into your function, which processes an event and returns its response.

 - **Event**: An action or trigger that causes a Lambda function to run.

- **Event source**: An event source is an AWS service, such as Amazon SNS, or a custom service. This triggers function helps you to executes its logic.

 - **Handler**: The entry point for a Lambda function. It's the function that AWS Lambda calls when an event occurs.

 - **Runtime**: The language and version of the code that the Lambda function is written in. Runtime allows functions in various languages which runs on the same base execution environment. This helps you to configure your function in runtime. It also matches your selected programming language.

 - **Trigger**: An event source that causes a Lambda function to run.

 - **Invocation**: The act of running a Lambda function.

 - **Cold start**: The initial startup time of a Lambda function when it hasn't been run in a while.

 - **Warm start**: When a Lambda function is run multiple times and the container hosting the function is already initialized, resulting in faster response times.

 - **Concurrent executions**: The number of instances of a Lambda function that can run simultaneously.

 - **Execution environment**: The infrastructure that AWS Lambda provides to run the code, including the operating system and other system resources.

 - **Lambda Layers**: Lambda layers are an important distribution mechanism for libraries, custom runtimes, and other important function dependencies. This AWS component also helps you to manage your development function code separately from the unchanging code and resources that it uses.

 - **Log streams**: Log stream allows you to annotate your function code with custom logging statements which helps you to analyse the execution flow and performance of your AWS Lambda functions.

## Opdracht
### Gebruikte bronnen

https://aws.amazon.com/serverless/sam/

https://www.guru99.com/aws-lambda-function.html

https://digitalcloud.training/aws-lambda-tutorial-create-a-serverless-function/

https://www.youtube.com/watch?v=3Ar1ABlD_Vs

### Ervaren problemen
Geen problemen ervaren

### Resultaat
#### Create Function

![lambcreatefunction](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/lambcreatefunction.png)


#### Test Function

![lambtest](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/lambtest.png)
![lambtestsuccess](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/lambtestsuccess.png)

#### View Logs

![lambviewlog1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/lambview%20log1.png)
![lambviewlog2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/lambviewlog2.png)

#### View Metrics


![lambmon](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/lambmon.png)
