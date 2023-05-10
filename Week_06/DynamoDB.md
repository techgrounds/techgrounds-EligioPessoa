# DynamoDB

AWS DynamoDB is a fully managed NoSQL database service that allows customers to store and retrieve any amount of data, at any time, from anywhere. It can be used for a variety of applications, from storing user profiles and product catalogs to powering real-time applications and IoT devices.

In a typical scenario where AWS DynamoDB applies, a company is using AWS to run their applications and services in the cloud. They need a highly available and scalable database solution that can handle large amounts of data and requests. With DynamoDB, they can easily store and retrieve data with high throughput and low latency, and can scale up or down as needed to meet changing demands.

## Key-terms
- **Tables**: A table is a grouping of data records. For example, you might have a Users table to store data about your users, and an Orders table to store data about your users' orders. This concept is similar to a table in a relational database or a collection in MongoDB.

- **Items**: An item is a single data record in a table. Each item in a table is uniquely identified by the stated primary key of the table. In your Users table, an item would be a particular User. An item is similar to a row in a relational database or a document in MongoDB.

- **Attributes**: Attributes are pieces of data attached to a single item. Attributes can be scalar values, sets, or nested JSON objects. This could be a simple Age attribute that stores the age of a user. An attribute is comparable to a column in a relational database or a field in MongoDB. DynamoDB does not require attributes on items except for attributes that make up your primary key.

- **Primary key**: A unique identifier for each item in a table. Can be a simple primary key made up of just a partition key; or a composite primary key made up of a partition key and a sort key.

- **Global secondary index (GSI)**: An index that allows you to query data using a different partition key or sort key.

- **Local secondary index (LSI)**: An index that allows you to query data using a different sort key within the same partition key.

- **Provisioned throughput**: The amount of read and write capacity that you provision for a table or index.

- **Query**: A request to retrieve data from a table or index based on specific criteria.

- **Scan**: A request to retrieve all data from a table or index.

- **Conditional writes**: Writes that only occur if certain conditions are met, such as if an item with a particular primary key doesn't already exist.


## Opdracht
### Gebruikte bronnen

https://www.dynamodbguide.com/key-concepts/

https://dynobase.dev/dynamodb-vs-aurora/

https://digitalcloud.training/amazon-dynamodb-tutorial-for-beginners/

https://crypto.stackexchange.com/questions/68093/how-does-aws-secret-key-and-access-key-work

https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html

https://docs.aws.amazon.com/accounts/latest/reference/root-user-access-key.html

### Ervaren problemen
Geen problemen ervaren

### Resultaat


### Benefits of Amazon DynamoDB

- **Managed service**: There is no need to hire experts to manage NoSQL installation. Developers need not worry about setting up, configuring a distributed database cluster, managing ongoing cluster operations, etc. It handles all the complexities of scaling, partitions and re-partitions data over more machine resources to meet I/O performance requirements.

- **Scalable**: There is no need to worry about predefined limits to the amount of data each table can store. Any amount of data can be stored and retrieved. DynamoDB will spread automatically with the amount of data stored as the table grows.

- **Fast**: Amazon DynamoDB provides high throughput at very low latency. As datasets grow, latencies remain stable due to the distributed nature of DynamoDB's data placement and request routing algorithms.

- **Durable and highly available**: Amazon DynamoDB replicates data over at least 3 different data centers’ results. The system operates and serves data even under various failure conditions.

- **Flexible**: Amazon DynamoDB allows creation of dynamic tables, i.e. the table can have any number of attributes, including multi-valued attributes.

- **Cost-effective**: Payment is for what we use without any minimum charges. Its pricing structure is simple and easy to calculate.



### Praktische opdracht
#### Create Profile in CLI

![dynamocrtprfl2.png](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/dynamocrtprfl2.png)

#### Create DynamoDB Table

![dynamocrttable.png](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/dynamocrttable.png)
![dynamocrttable2.png](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/dynamocrttable2.png)
![]()

#### Request downloaded JSON file and scan 

![dynamorequest.png](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/dynamorequest.png)
![dynamoscan.png](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/dynamoscan.png)


##### Enable point in time recovery

![dynamopitr](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/dynamopitr.png)

#### Create on-demand backup

![dynamobackup](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/dynamobackup.png)
![dynamobackup2](https://github.com/techgrounds/techgrounds-EligioPessoa/blob/main/00_includes/dynamobackup2.png)
