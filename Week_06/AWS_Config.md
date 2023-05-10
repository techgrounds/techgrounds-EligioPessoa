# AWS Config


AWS Config (Amazon Web Services Config) is an Amazon cloud auditing tool that provides an inventory of existing resources, allowing an administrator to accurately track AWS assets to analyze compliance levels and security. It also enables an administrator to troubleshoot why a resource may have stopped working properly.

The benefits of using AWS Config are that it provides customers with a centralized view of their AWS resources, enables them to track and manage changes to their infrastructure over time, and helps them ensure that their resources are configured in a way that complies with their organization's policies and best practices. Additionally, AWS Config enables customers to identify and respond to changes that could impact their infrastructure's security, compliance, and performance, helping them maintain a more secure and optimized AWS environment.

## Key-terms

- **AWS Config Rules**: A Config Rule represents desired configurations for a resource and is evaluated against configuration changes on the relevant resources, as recorded by AWS Config. AWS Config Rules can check resources for certain desired conditions and if violations are found the resources are flagged as “noncompliant”. Examples of Config Rules:

  - Is backup enabled on Amazon RDS?
  - Is CloudTrail enabled on the AWS account?
  - Are Amazon EBS volumes encrypted.

Rules give us a way to evaluate the configuration of our resources in near real-time. They tap into the configuration stream as resources are created or updated and compare the configuration to a desired state defined in the rule. If the configuration of the resource deviates from the rule then it is marked as NON_COMPLIANT. There are two types of rules Managed & Custom.
 - **Managed Rules**: Managed rules are provided by AWS. We can pick which ones are relevant to our environment and deploy them through the AWS Console, Cli or IAC tools. A full list is available here. Managed rules are also used by other AWS Services such as Security Hub to report overall compliance of resources within the AWS Account.
 - **Custom Rules**: We can also create our own rules either using the AWS Console, cfn-guard, or the AWS Config Rules Development Kit. Custom rules are backed by Lambda.



- **Configuration Items (CI)**: A configuration item is a snapshot of a supported resource at a specific point in time. A CI consists of 5 sections:

  - Basic information about the resource that is common across different resource types (e.g., Amazon Resource Names, tags).
  - Configuration data specific to the resource (e.g., Amazon EC2 instance type).
  - Map of relationships with other resources (e.g., EC2::Volume vol-3434df43 is “attached to instance” EC2 Instance i-3432ee3a).
  - AWS CloudTrail event IDs that are related to this state.
  - Metadata that helps you identify information about the CI, such as the version of this CI, and when this CI was captured.

It includes metadata, attributes, relationships, current configuration, and related events. These configuration items are the building blocks that AWS Config uses to provide the configuration history of your AWS Resources. For example, if AWS Config is recording Amazon S3 buckets, AWS Config creates a configuration item whenever a bucket is created, updated, or deleted

- **Resources**: We create resources through the Console, Cli, or your favorite IAC tools such as Cloudformation or Terraform. These resources include IAM Users, EC2 Instances, EBS Volumes, S3 Buckets, and more. As long as the resource is on the supported resources list for AWS Config, it will keep track of it for you.

- **Configuration Recorder**: Think of Configuration Recorder as the engine that's responsible for storing all the configuration items for all supported resources within the region where AWS Config is running. By default, the Configuration Recorder will store configuration items for all supported resources, but you can select a subset of resources if needed.

- **Configuration Snapshot**: A configuration snapshot is a complete picture of the supported resources that exist in your account and their configurations. It's a collection of the configuration items that have been recorded, and it can be a useful tool for validating your configuration. This snapshot provides a comprehensive view of your AWS resources, making it easier to ensure that everything is configured correctly. These can be delivered to S3 or viewed in the AWS Config console.

- **Configuration Stream**: The configuration stream is the firehose of all the updates to those supported resources. Whenever a resource is created, modified, or deleted, AWS Config creates a configuration item and adds them to the configuration stream. This stream is very powerful in that we can react to these events directly using Systems Manager or using other AWS services such as Lambda and many others.

- **Relationships**: Relationships provide information on how configuration items relate to one another, giving us a better picture of our resources.
For example:

  - An IAM User configuration item could have a relationship with an IAM Group if it was a member of the Group.

  - An EC2 instance might include a relationship with an EBS Volume.

These relationships help to provide more context of how our resources are related.

## Opdracht
### Gebruikte bronnen

https://digitalcloud.training/aws-config/

https://www.techtarget.com/searchaws/definition/AWS-Config-Amazon-Web-Services-Config

https://k21academy.com/amazon-web-services/aws-config/

https://blog.awsfundamentals.com/an-introduction-to-aws-config

https://tutorialsdojo.com/aws-config/

### Ervaren problemen
Geen problemen ervaren

### Resultaat


Benefits of AWS Config

 - **Security Analysis & Resource Administration**: It allows continuous monitoring and oversight of resource configurations, as well as assisting you in evaluating them for any misconfigurations that could lead to security vulnerabilities or weaknesses.
 - **Continuous monitoring**: It allows you to monitor and record configuration changes to your AWS resources in real-time. At any time, it allows you to inventory your AWS resources, their configurations, and software configurations within EC2 instances. An Amazon Simple Notification Service (SNS) notification can be sent to you after a change from a prior state is detected for you to review and act on.
 - **Continuous assessment**: It allows you to audit and analyse the overall compliance of your AWS resource configurations with your organization’s policies and standards on a continual basis. Config allows you to specify rules for creating and configuring Amazon Web Services services. These rules can be delivered individually or in a pack (known as a conformance pack) with compliance remediation actions that can be implemented throughout your whole business with a single click.
 - **Change management**: Before making changes, you can use Config to track resource relationships and examine resource dependencies. You can rapidly check the history of the resource’s configuration once a change occurs and determine what the resource’s configuration looked like at any point in time. It provides you with information to assess how a change to a resource configuration would affect your other resources, which minimizes the impact of change-related incidents.
 - **Enterprise-wide compliance monitoring**: With multi-account, multi-region data aggregation in Config, you can view compliance status across your enterprise and identify non-compliant accounts. You can dive deeper to view the status for a specific region or a specific account across regions. You can view this data from the Config console in a central account, removing the need to retrieve this information individually from each account and each region.
