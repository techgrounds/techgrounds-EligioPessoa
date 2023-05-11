# AWS Trusted Advisor

AWS Trusted Advisor is a service that inspects all the resources present in your AWS account and suggests improvements to bring them in line with AWS best practices.

When you first start using AWS it is reasonably easy to keep track of what you have running, however as time goes on and your account footprint grows you may start to get sub-optimal scenarios in terms of cost management and performance that go unnoticed.

You may have orphaned resources, unused or obsolete snapshots, storage volumes that are no longer in use, resources that are not attached to instances, the list goes on and these resources are costing your business money. You may also have resources configured that aren’t optimised for security, performance or fault tolerance. 

In simple terms, AWS Trusted Advisor is a native AWS tool that provides active guidance to operate AWS workloads consistently, safely, and efficiently. 

AWS Trusted Advisor acts as a consultant with deep knowledge of AWS who can diagnose problems within your AWS infrastructure to improve performance, reliability, security, and costs. AWS Trusted Advisor evaluates your AWS resources by using pre-defined monitoring rules called “Checks.”

Trusted Advisor checks five categories of best practice compliance being cost optimization, performance, security, fault tolerance and service limits.

Not all Checks are available to every account. AWS has set up a pricing plan to offer more Checks to customers subscribing to a higher support plan.

## Key-terms

 - **AWS Infrastructure**: The underlying physical or virtual resources, such as compute, storage, and networking, that support the delivery of AWS services.
 - **Best Practice Checks**: A collection of automated checks that evaluate your AWS environment against AWS best practices in the categories of cost optimization, performance, security, and fault tolerance.
  - **Recommendations**: Suggestions provided by AWS Trusted Advisor on how to optimize your AWS environment based on the evaluation of your infrastructure and Best Practice Checks.
 - **Checks Refresh Rate**: The frequency at which AWS Trusted Advisor evaluates your AWS environment against Best Practice Checks, which is typically weekly.
 - **Support Plans**: The AWS Trusted Advisor is available as part of the AWS Support plans, which provide access to AWS experts, technical support, and resources.

## Opdracht
### Gebruikte bronnen

https://aws.amazon.com/premiumsupport/technology/trusted-advisor/

https://www.hava.io/blog/what-is-aws-trusted-advisor

https://cloudacademy.com/course/an-overview-of-aws-trusted-advisor/what-is-aws-trusted-advisor-2/

https://www.opsramp.com/guides/aws-monitoring-tool/trusted-advisor-checks/

https://www.nops.io/aws-trusted-advisor-comprehensive-guide/

### Ervaren problemen
Geen problemen ervaren.

### Resultaat

The main function of Trusted Advisor is to recommend improvements across your AWS account to help optimize and streamline your environment based on these AWS best practices.  These recommendations cover 5 distinct categories:

- **Cost optimization** - Helps to identify ways in which you could optimize your resources to help you reduce costs by implementing features such as reserved capacity and removing unused capacity
- **Performance**: This reviews your resources to highlight any potential performance issues across your infrastructure, determining if you could take benefits from performance-enhancing capabilities such as provisioned throughput
- **Security**: This analyses your environment for any potential security weaknesses or vulnerabilities that could potentially lead to a breach.
- **Fault Tolerance** - This helps to suggest best practices to maintain service operations by increasing resiliency, should a fault or incident occur across your resources.
- **Service Limit** - This identifies and warns you when your resources reach 80% capacity of their service limit quota. 



### Benefits of AWS Trusted Advisor

The AWS Trusted Advisor can help you meet compliance faster as you will have a more secure cloud.

#### Optimize Cloud Costs

The AWS Trusted Advisor analyzes past usage patterns and configurations that affect your cloud spend. You can optimize costs by identifying underutilized resources, terminating idle resources, or downgrading resources. Example checkpoints include:

 - **Optimize EC2 Costs**: The Trusted Advisor checks whether your RI (Reserve Instance) purchases are lower than corresponding On-Demand usage. The Trusted Advisor finds ways of saving you costs through Reserved Instances. The Trusted Advisor performs multiple simulations for each usage category to maximize RI purchases.

 - **Idle Amazon RDS DB Instances**: The Trusted Advisor checks for any idle Database Instances on RDS (remote desktop services) workloads and recommends the deletion of instances that were inactive for the past seven days.

 - **High-Risk Issues**: The AWS high-risk issues may make your costs escalate. The Trusted Advisor pulls this information from the Well-Architected Review reports.

 - **AWS Savings Plan**: The Trusted Advisor recommends using the AWS Savings plan based on AWS Lambda, Fargate, and EC2 usage for the previous month. You can save on these resources through one to three-year commitment plans.

 - **Unassociated Elastic IPs**: AWS Charges for Elastic IPs, one way to save costs is to check for Elastic IPs disconnected from EC2.

 - **Underutilized EBS Volumes**: The Trusted Advisor warns against underutilized EBS volumes, so you only pay for what you use.

#### Improve Cloud Security

AWS gets best practices on security from leading industry standards and security experts. AWS systems can examine your system for potential flaws and help you practice sound cyber hygiene. Here are common security checkpoints:

 - **Amazon S3 Bucket Permissions**: Some S3 configurations may have permissions that are too permissive; these include open access ports and allowing login on all IP addresses.

 - **AWS CloudTrail Logs**: The Trusted Advisor examines logs on any changes made to the account from various IAM users. CloudTrail can report abnormal activities for further investigation.

 - **Exposed Access Keys**: People with your access key can access the cloud remotely, making your system vulnerable. The Trusted Advisor detects exposed access keys through popular code platforms. The Trusted Advisor limits certain functions temporarily to help secure the account.

 - **IAM Access Key Rotation**: The AWS Advisor ensures that IAM (Identity and Access Management) access keys rotate every 90 days.

 - **IAM Password Policies**: The Trusted Advisor checks for weak passwords and disabled password policies.

 - **MFA**: The AWS Well-Architected Framework recommends the use of MFA (multi-factor authentication) for root users. Root users have to use MFA to get a code on mobile apps, eMail, or SMS before accessing the infrastructure.

#### Check Service Quotas

Regardless of your support plan, you can check whether you exceed service quotas through the AWS Trusted Advisor. Service quotas are the maximum limits on services you can launch in a given AWS account, including free-tier limits. Some service quota checkpoints include:

 - **Auto-Scaling Groups**: Checks if you’ve used more than 80% of the auto scale group quota.
 - **EC2 On-Demand Instances**: Checks if the CPU utilization of On-Demand instances is more than 80%.
 - **EC2 Reserved Instance Plans**: Checks if the RI usage is more than 80% of the RI lease agreement.
 - **Route53 Zones**: Each account has a limited number of Route53 hosted zones.
