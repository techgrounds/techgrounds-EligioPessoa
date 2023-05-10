# CloudWatch
AWS CloudWatch is a service provided by Amazon Web Services that helps customers monitor and collect metrics, logs, and events from their AWS resources and applications. In simple terms, AWS CloudWatch allows customers to keep an eye on what's happening within their AWS environment. It can collect data on things like CPU usage, network traffic, and application logs, which can help customers troubleshoot issues, optimize resource usage, and maintain the performance and availability of their applications.

In a typical scenario where AWS CloudWatch applies, a company is using AWS to run their applications and services in the cloud. They want to be able to monitor the health and performance of their resources and applications, and receive alerts if something goes wrong.

With AWS CloudWatch, the company can set up metrics and alarms to track the performance of their resources and applications. For example, they might set up an alarm to alert them if CPU usage on an EC2 instance exceeds a certain threshold. They can also collect and analyze logs from their applications to help them identify and troubleshoot issues.

Overall, AWS CloudWatch provides customers with a way to monitor and manage their AWS environment, helping them maintain the performance and availability of their applications and services.

## Key-terms

- Metrics
  - It represents a time-ordered set of data points that are published to Amazon CloudWatch
  - All data point is marked with a timestamp
  - Metric is a variable that is monitored and data points are the value of that variable over time
  - They are uniquely defined by a name, namespace, and zero or more dimensions
  - Metric math is used to query multiple cloudwatch metrics and use math expressions to create new time-series based on these metrics

- Dimensions
  - A dimension is a name/value pair which uniquely identifies a metric
  - Dimensions are the unique identifiers for a metric, so whenever you add a unique name/value pair to one of the metrics, you are creating a new variation of that metric.

- Statistics
  - Statistics are metric data aggregations over specified periods of time
  - The few available statistics on Cloudwatch are maximum, minimum, sum, average, and sample count.

- Alarm
  - It is used  to automatically initiate actions on our behalf
  - It watches a single metric over a specified time period and performs one or more specified actions based on the value of the metric
  - The estimated AWS charges can also be monitored using the alarm

CPU Utilization and Bytes Download are metric data of EC2 and SNS specifically.

There are 3 alarm states:

    OK – Within Threshold.
    ALARM – Crossed Threshold.
    INSUFFICIENT_DATA – Metric not available/ Missing data (Good, Bad, Ignore, Missing).

One of these states will be considered at each millisecond of using CloudWatch metric data.



- Percentiles
  - It represents the relative weightage of the data in a dataset
  - It helps the user to get a better understanding of the distribution of metric data

- Cloudwatch dashboard
  - A user-friendly Cloudwatch console is available which is used for monitoring resources in a single view.
  - There is no limit on the number of cloudwatch dashboards you can create.
  - These dashboards are global and not region-specific

- Cloudwatch agent
  - It is required to be installed
  - It collects logs and system-level metrics from EC2 instances and on-premises servers

- Cloudwatch Events:
  - Cloudwatch events help you to create a set of rules that match with any event(i.e stopping of EC2 instance).
  - These events can be routed to one or more targets like AWS Lambda functions, Amazon SNS Topics, Amazon SQS queues, and other target types.
  - Cloudwatch Events observes the operational events continuously and whenever there is any change in the state of the event, it performs the action by sending notifications, activating lambda, etc.
  - An event indicates a change in the AWS environment. Whenever there is a change in the state of AWS resources, events are generated.
  - Rules are used for matching events and routing to targets.
  - Target process events. They include Amazon EC2 instances, AWS Lambda functions, etc. A target receives the events in JSON format.

- Cloudwatch logs:
  - Amazon Cloudwatch logs enable you to store, monitor, and access files from AWS resources like Amazon EC2 instances, Route53, etc.
  - It also helps you to troubleshoot your system errors and maintain the logs in highly durable storage.
  - It also creates log of information about the DNS queries that Route 53 receives

## Opdracht
### Gebruikte bronnen

https://www.techtarget.com/searchaws/definition/CloudWatch



### Ervaren problemen

Geen problemen ervaren

### Resultaat

Voor de praktische gedeelte, wil ik refereren naar [de opdracht waar ik twee CloudWatch alarms heb gecreërd voor Elastic Load Balancing](link)

Amazon CloudWatch Alarms





Advantages of Amazon CloudWatch

    One dashboard, Access all data
        The web applications produce a lot data as they are highly distributed, to access all the data which have been collected you just need a single CloudWatch dashboard.
    Visibility on the complete Infrastructure
        You can see through all the AWS resources and services you use, so you can correlate and contradict data produced from multiple services.
    Improve total cost of ownership
        CloudWatch can be used to set high resolution alarms and can take automated actions while there is an breach in the limits provided. This can help in minimize the costs spent on AWS services

    Insights from logs
        You receive detailed insights on separate AWS services and the applications you run on the infrastructure. Data like memory, CPU utilization, and capacity utilization can be monitored and receive insights from it
    Optimize Applications and resources
        Using the log and metric data, you can optimize your AWS services to provide maximum throughput and performance.
