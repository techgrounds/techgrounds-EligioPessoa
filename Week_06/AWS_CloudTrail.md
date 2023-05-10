# CloudTrail
AWS CloudTrail is a service provided by Amazon Web Services that keeps a log of everything that happens in your AWS account. This includes things like who made changes and when they made them. It helps you keep track of what's happening in your account, which can be important for things like security and compliance.

Let's say a company is using AWS to run their applications and services in the cloud. They want to ensure the security of their infrastructure and be able to track changes made to their resources for compliance purposes. They decide to enable AWS CloudTrail, which allows them to monitor and record all API activity within their AWS account.

Whenever an API call is made, AWS CloudTrail logs the details of the call, including who made it, when it was made, and what resources were accessed or changed. The log files are then stored in an S3 bucket, which the company can access and analyze to gain insights into their account activity.

With AWS CloudTrail, the company can maintain visibility into the activity occurring within their AWS account, which can help them identify potential security risks, troubleshoot issues, and maintain compliance with industry regulations.

## Key-terms

 - **Events**: An event in CloudTrail is the record of an activity in an AWS account. This activity can be an action taken by an IAM identity, or service that is monitorable by CloudTrail. CloudTrail events provide a history of both API and non-API account activity made through the AWS Management Console, AWS SDKs, command line tools, and other AWS services. There are three types of events that can be logged in CloudTrail: management events, data events, and CloudTrail Insights events. By default, trails log management events, but not data or Insights events.

- **Management Events**: Management Events provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. Example management events include:
  - Configuring security (for example, AWS Identity and Access Management AttachRolePolicy API operations).
  - Registering devices (for example, Amazon EC2 CreateDefaultVpc API operations).
  - Configuring rules for routing data (for example, Amazon EC2 CreateSubnet API operations).
  - Setting up logging (for example, AWS CloudTrail CreateTrail API operations).

Management events can also include non-API events that occur in your account. For example, when a user signs in to your account, CloudTrail logs the ConsoleLogin event.


- **Data Events**: Data Events provide information about the resource operations performed on or in a resource. These are also known as data plane operations. Data events are often high-volume activities.

- **Insights Events**: CloudTrail Insights events capture unusual API call rate or error rate activity in your AWS account by analyzing CloudTrail management activity. If you have Insights events enabled, and CloudTrail detects unusual activity, Insights events are logged to a different folder or prefix in the destination S3 bucket for your trail. Insights events are logged only when CloudTrail detects changes in your account's API usage or error rate logging that differ significantly from the account's typical usage patterns.

- **Trails**: A trail is a configuration that enables delivery of CloudTrail events to an Amazon S3 bucket, CloudWatch Logs, and Amazon EventBridge. You can use a trail to filter the CloudTrail events you want delivered, encrypt your CloudTrail event log files with an AWS KMS key, and set up Amazon SNS notifications for log file delivery.

- **Eventbridge**: Amazon EventBridge is an AWS service that delivers a near real-time stream of system events that describe changes in AWS resources. In EventBridge, you can create rules that respond to events recorded by CloudTrail.


## Opdracht
### Gebruikte bronnen


https://intellipaat.com/blog/aws-cloudtrail/?US

https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-concepts.html#cloudtrail-concepts-events

### Ervaren problemen
Geen problemen ervaren

### Resultaat

### Advantages of AWS CloudTrail

- **Security Analysis and Troubleshooting**: By periodically capturing an extensive history of modifications made to the AWS account, AWS CloudTrail will enable the user to identify and troubleshoot security and operational issues.

- **Simplified Compliance**: By automatically capturing and keeping event logs for actions created periodically in the AWS account, AWS CloudTrail can change the compliance audits. Searching through the log data is made simple by integration with Amazon CloudWatch Logs.

Additionally, it aids in identifying events that are out of compliance and speeds up incident investigations and auditor request responses.

- **Visibility into user and resource activity**: By capturing AWS Management Console events and API calls, Amazon CloudTrail will improve insight into user and resource activity.

The user can ascertain which accounts and users are referred to as AWS. Once the calls took place, the calls’ supply internet protocol address was formed.

- **Security Automation**: The user can utilize Amazon CloudTrail to automatically reply to the account for the protection of Amazon resources. The user will be able to specify workflows that run once events that could result in security vulnerabilities are discovered thanks to the integration of Amazon CloudWatch Events.


### Application of AWS CloudTrail

- **Security Analysis**: The user can be in control of security analysis, and they can observe user behavior with the aid of AWS CloudTrail events, patterns, log management, and analytics tools.

- **Data Exfiltration**: By gathering activity information on S3 objects, the user can observe data exfiltration with the use of object-level API events that are recorded in Amazon Cloudtrail.

- **Compliance AID**: By providing a history of activity in the AWS account, AWS CloudTrail makes it simpler to certify compliance with internal policies and regulatory standards. 

- **Operational Issue Troubleshooting**: By using the AWS CloudTrail decision history for the AWS API, the user can address operational issues.

For example, the user will be able to identify the most recent changes made to resources in the environment as well as the creation, modification, and deletion of AWS resources rapidly (e.g., Amazon EC2 instances, Amazon VPC security teams, and Amazon EBS volumes).




### AWS cloud trail vs AWS cloud watch
| AWS Cloud Trail | AWS Cloud Watch |
| --------------- | --------------- |
| Aws Cloud Trail requires web services | AWS Cloud Watch requires monitoring services |
| The requester, the services used, the actions taken, the action parameters, and the response components supplied by the AWS service are all logged by CloudTrail.	| By using CloudWatch, you may gather and monitor metrics, gather and watch over log files, and trigger alarms. |
| After making an API call, CloudTrail provides an event within 15 minutes.	| Metric data from CloudWatch is delivered at 5-minute intervals. |
| You may get detailed information about what happened in your AWS account through CloudTrail Logs.	| Application logs are reported on by CloudWatch Logs. |
| AWS API calls made in your AWS account are the main focus of CloudTrail | A near-real-time stream of system events describing modifications to your AWS resources is called CloudWatch Events. |
