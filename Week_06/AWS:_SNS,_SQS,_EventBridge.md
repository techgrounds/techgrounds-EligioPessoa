# SNS, SQS, Event Bridge
AWS SNS, SQS, and EventBridge are AWS messaging and event services that can be used to build scalable and reliable distributed systems and applications.

AWS SNS (Simple Notification Service) is a managed service that enables you to send messages or notifications to a variety of endpoints, such as email, SMS, mobile push notifications, and more. This service can be used to simplify the process of sending notifications to a large number of users across various channels.

AWS SQS (Simple Queue Service) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications. This service can be used to queue up requests and process them in a scalable and reliable manner.

AWS EventBridge is a serverless event bus that makes it easy to build event-driven architectures in the cloud. This service can be used to set up rules and event patterns that trigger specific actions or workflows based on events from different sources.

Overall, these services provide a way to send messages, manage queues, and build event-driven architectures in the cloud. They can be used individually or together to build complex, scalable, and reliable applications on AWS.

## Key-terms

**SQS Main Concepts**

- **Queues**: Queues are the first class citizens of AWS. They are what you as the user will create either through the console, CLI, or IaC. Queues are the destination of where you, the application owner, will be publishing messages to. Content published to the queue will persist until a consuming application retrieves and processes the messages. A message in a queue gets ‘claimed’ when a thread attempts to process it – during which time that message is invisible to other threads until either it is successfully processed (and therefore deleted), or a timeout occurs (timeout duration is configurable).
- **Messages**: Messages are the content or payload of what gets sent to the queue. Each message is a single entry in the queue, and typically contains a JSON object that is specific to your application. For example, in a credit card transaction application, I may publish events to an SQS queue that indicate a new transaction occurred.
- **Polling**: Polling is the mechanism by which the consumer of the queue will process them. You can poll a queue for one or more messages (the latter being called batch polling). When a consuming application polls the queue and acquires messages, they become invisible to all other consuming application threads. SQS supports both short and long polling.

**SNS Main Concepts**

- **Topics**: Topics are the first class citizens of SNS. They are similar to queues in that messages are published to them, but they are not stateful in any way. They do not ‘hold’ messages, they simply are an endpoint that a publishing application can write to, and in turn, rely on SNS to broadcast a copy of that message out to all recipients. In other words, Topics allow for fan-out notifications to many clients. Topics are usually created with a particular theme in mind. Using the same example from our prior exercise, we may have a OrderCreation topic that will broadcast messages to all consumers when a message is published to it.
- **Messages**: Messages are simply JSON blobs that contain payload data. Note that during the publishing process, an identical message is published to each downstream subscriber for consumption.
- **Publish/Subscribe**: Publish/Subscribe or PubSub is a term that loosely defines the relationships between owners of data, and consumers of data. The application or person who owns the data would be considered the topic owner or publisher. And the application or person interested in consuming the data would be considered a consumer or subscriber.

**EventBridge Main Concepts**

- **Message Bus**: Message Buses are very similar to SNS topics in that they receive events that need to be broadcaster to downstream consumers.
- **Events**: Events are similar to messages in the context of SNS and SQS, just with a fancier name. They consist of JSON blobs that describes the source and payload of the event. Events can also be “scheduled” to run at periodic intervals using a cron expression. This is useful for those of you looking to perform timed batch jobs regularly at a certain time of day.
- **Targets**: Targets are the downstream recipient of events that are published to the message bus. Very similar to SNS consumers.
- **Rules**: Rules are the routing logic component for Message Buses. Essentially, you can configure rules such that only when a certain condition is met (within the message data itself), will a message be broadcaster to a specific target. An Event Pattern is something that you define that matches the content of the message to a specific target. You can have many rules that all match to different patterns, but only 5 targets per rule. If you’d like to have more, you would need to create a new rule with the same event pattern, but with different configured targets.
- **Event Bus**: An Event Bus is a mechanism that allows different components to communicate with each other without knowing about each other. A component can send an Event to the Event Bus without knowing who will pick it up or how many others will pick it up. Components can also listen to Events on an Event Bus, without knowing who sent the Events. That way, components can communicate without depending on each other. Also, it is very easy to substitute a component. As long as the new component understands the Events that are being sent and received, the other components will never know.

## Opdracht
### Gebruikte bronnen

https://awstip.com/aws-eventbridge-vs-sns-vs-sqs-d9dff51af4b6?gi=1415ff314ce5

https://beabetterdev.com/2021/09/10/aws-sqs-vs-sns-vs-eventbridge/

https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-tutorial-archive-replay.html

https://www.youtube.com/watch?v=vwYy8GUV8Zw (SNS)

https://www.youtube.com/watch?v=xyHLX1dUwuA (SQS)

https://www.youtube.com/watch?v=ea9SCYDJIm4 (EventBridge) 

https://www.youtube.com/watch?v=mOysNzNFDRw (EventBridge)

### Ervaren problemen
Geen problemen ervaren

### Resultaat
AWS EventBridge is a separate service from AWS SNS and SQS, but it can integrate with them as targets for events. EventBridge provides a serverless event bus that can receive events from various sources, such as AWS services, SaaS applications, and custom applications.

You can use EventBridge to set up rules that match events and route them to various targets, including AWS Lambda functions, SNS topics, SQS queues, and other AWS services. This allows you to build event-driven architectures and workflows that respond to events in real-time, without the need for complex and manual integrations.

So, while EventBridge is not directly related to SNS and SQS, it can work with them as part of a larger event-driven architecture.


EventBridge Features:

- **Schema Registry/Discovery**: One of the big problems with using SNS is determining message format and content. For example, if you subscribe to an SNS topic, how will you know the exact schema of the messages you’ll be receiving? Typically, we would rely on the publishing team to provide model objects for their notifications so that consumers can use them to deserialize the message. However, this is usually something that gets overlooked during the development process.
Schema Registry is a component of eventbridge that allows developers to register their event schemas and make them discoverable by other teams. The registry automates the process of detecting event schemas and making them available to other teams.
Users looking to consume a message of a particular schema can generate code bindings which output model objects in a language of your choice. This makes it a lot easier to hit the ground running and building your application quicker. This is a huge plus for Eventbridge over SNS.

- **Third Party Integrations**: Perhaps the largest selling point of using Eventbridge is its native support for third party integrations.
Today, there are tons of SaaS companies that emit useful events that developers want to integrate into their application. For example Shopify – wouldn’t it be nice if automatically we can hook into Shopify order creation events for our e-commerce store, and invoke a Lambda function as a result?
With Eventbridge Third Party Integrations, this becomes a trivial task. The feature supports many popular integration services such as Shopify, Datadog, Pagerduty, Zendesk, Amazon Seller API and many many more. See a list in this link.
This means developers have little work to do to detect and broadcast these messages into their application ecosystem.


- **Scheduled Events (Formerly Cloudwatch Events)**: One of the neat hidden features of EventBridge is the ability to create scheduled events that periodically ‘poke’ your event bus to broadcast a message.
This is not a new feature – in fact, scheduled events were up until recently branded as Cloudwatch Events. These days, cloudwatch events has been absorbed as a feature of eventbridge.
Using scheduled events, you can use a cron expression to set a periodic event that fires at a certain time. For example, this expression 0 8 * * * translates to “Everyday at 8am”. You can even customize the payload of the event to contain content of your choosing. Crontab is a great tool to help you build your cron expressions by the way.
Scheduled events can be used for periodic maintenance tasks and a wide variety of other use cases.
- **Scheduler**: EventBridge Scheduler is a brand new feature announced in November 2022. It is very similar to Scheduled Events but makes several improvements.
For one, it allows you to create one-time events that trigger at a specific time that you define. For example, you can create a one-time schedule set to fire an event on January 31st at 01:00.
The new feature also supports rate and cron based recurrence schedules. However, with these schedules you can specify a start and end time for when you would like the timer to begin and end. For example you can create a schedule that will fire every 1 minute starting on January 1st and ending on the 31st.
The final set of improvements of Scheduler over Events is in terms of resiliency. Scheduler offers a robust retry policy mechanism that will attempt to repeatedly deliver events over a period of time. If the event cannot be successfully delivered you can configure it to be sent to a Dead Letter Queue (DLQ).


### Praktische Opdracht
### SNS

#### Create SNS Topic

![snscreate](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/snscreate.png)


#### Create Lambda Function

![snscreatelambda](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/snscreatelambda.png)

#### Create SNS subscription

![snscreatesubscription](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/snscreatesubscription.png)

#### Check status Lambda function

![snsstatuslambda](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/snsstatuslambda.png)

#### SNS: publish message

![snspublish](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/snspublish.png)

#### View Cloudwatch logs of Lambda Function

![snsviewlog](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/snsviewlog.png)


### SQS

#### Create Lambda Function

![sqscreatelambda1](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/sqscreatelambda1.png)
![sqscreatelambda2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/sqscreatelambda2.png)

#### Create SQS Queue

![sqscreateq](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/sqscreateq1.png)

#### Add trigger to Lambda function

![sqstrigger](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/sqstrigger1.png)

#### Send SQS messages

![sqsmessageq](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/sqsmessageq.png)

#### Enable trigger and check Lambda Cloudwatch logs


![sqslog](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/sqslog.png)

### EventBridge

#### Create Lambda Function

![eventbridgecrtlambda](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/eventbridgecrtlambda.png)

#### Create EventBridge Archive

![eventbridgearch](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/eventbridgearch.png)

#### Create Rule

![eventbridgecrtrule](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/eventbridgecrtrule.png)


#### Send Test Events

![eventbridgesenttest](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/eventbridgesenttest.png)

#### Replay Events

![eventbridgereplay](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/eventbridgereplay.png)

#### View logs for Lambda Function

![eventbridgelog](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/eventbridgelog.png)



 
