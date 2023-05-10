# Identity and Access Management (IAM)
AWS IAM (Identity and Access Management) is a service provided by Amazon Web Services that helps customers manage access to their AWS resources.

In simple terms, AWS IAM allows customers to control who can access their AWS resources and what actions they can perform. This can help customers maintain the security of their infrastructure and ensure compliance with industry regulations.

In a typical scenario where AWS IAM applies, a company is using AWS to run their applications and services in the cloud. They want to ensure that only authorized individuals can access their AWS resources, and that those individuals can only perform the actions they need to perform.

With AWS IAM, the company can create users, groups, and roles that have specific permissions to access their AWS resources. For example, they might create a user who has permissions to launch and manage EC2 instances, but not to access S3 buckets. They can also use AWS IAM to enforce multi-factor authentication (MFA) and password policies to further enhance security.

Overall, AWS IAM provides customers with a way to manage access to their AWS resources, helping them maintain the security of their infrastructure and ensure compliance with industry regulations.

## Key-terms

- **Users**: Individuals within an organization who require access to AWS resources.

- **Groups**: A collection of users who share the same permissions and access to AWS resources.

- **Roles**: A set of permissions that define what actions a user or service can perform on AWS resources.

- **Policies**: Documents that define permissions and access to AWS resources.

- **Permissions**: Rules that define what actions can be performed on AWS resources.

- **Access keys**: Credentials used to authenticate API requests made to AWS resources.

- **Multi-factor authentication (MFA)**: A security feature that requires users to provide two forms of authentication to access AWS resources.

- **Identity providers (IdPs)**: External systems used to authenticate users and provide access to AWS resources.

- **Federation**: The process of connecting an external identity provider to AWS IAM to allow users to access AWS resources.

- **AWS Security Token Service (STS)**: A service that enables users to request temporary security credentials to access AWS resources.

## Opdracht
### Gebruikte bronnen

https://www.freecodecamp.org/news/aws-iam-explained/

https://www.javatpoint.com/aws-iam

https://digitalcloud.training/courses/aws-certified-cloud-practitioner-video-course/sections/section-4-identity-and-access-management-aws-iam/

### Ervaren problemen
Geen problemen ervaren

### Resultaat

### Features of IAM

- **Centralised control of your AWS account**: You can control creation, rotation, and cancellation of each user's security credentials. You can also control what data in the aws system users can access and how they can access.
- **Shared Access to your AWS account**: Users can share the resources for the collaborative projects.
- **Granular permissions**: It is used to set a permission that user can use a particular service but not other services. When permissions are granular, they are highly specific and detailed, allowing for fine-grained control over who can access what resources, and what actions they can perform on those resources.
- **Identity Federation**: An Identity Federation means that we can use Facebook, Active Directory, LinkedIn, etc with IAM. Users can log in to the AWS Console with same username and password as we log in with the Active Directory, Facebook, etc.
- **Multifactor Authentication**: An AWS provides multifactor authentication as we need to enter the username, password, and security check code to log in to the AWS Management Console.
- **Permissions based on Organizational groups**: Users can be restricted to the AWS access based on their job duties, for example, admin, developer, etc.
- **Networking controls**: IAM also ensures that the users can access the AWS resources within the organization's corporate network.
- **Provide temporary access for users/devices and services where necessary**: If you are using a mobile app and storing the data in AWS account, you can do this only when you are using temporary access.
- **Integrates with many different aws services**: IAM is integrated with many different aws services.
- **Supports PCI DSS Compliance**: PCI DSS (Payment Card Industry Data Security Standard) is a compliance framework. If you are taking credit card information, then you need to pay for compliance with the framework.
- **Eventually Consistent**: IAM service is eventually consistent as it achieves high availability by replicating the data across multiple servers within the Amazon's data center around the world.
- **Free to use**: AWS IAM is a feature of AWS account which is offered at no additional charge. You will be charged only when you access other AWS services by using IAM user.


### Praktische opdracht
#### Create New User

![iamcreateuser](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/iamcreateuser.png)
![iamcreateuser](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/iamcreateuser2.png)

#### Creat Group with admin access and add user

![creategroup](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/iamcreategroup.png)
![creategroup](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/iamcreategroup2.png)
![creategroup](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/iamcreategroup3.png)

#### Sign in as new user

![iamsignin](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/iamsignin1.png)
![iamsignin](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/iamsignin2.png)
