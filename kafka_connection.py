#https://www.conduktor.io/kafka/how-to-install-apache-kafka-on-windows/
#https://www.youtube.com/watch?v=BwYFuhVhshI 5:54


#start zookepper ?
#.\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

#--start kafka
#.\bin\windows\kafka-server-start.bat .\config\server.properties

#create topi
from kafka.admin import KafkaAdminClient ,NewTopic

# Connection string for the Kafka bootstrap server
bootstrap_servers = 'localhost:9092'

# Create an instance of KafkaAdminClient
admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)

# Specify the topic name, number of partitions, replication factor, and any additional topic configuration

topic_list = []
topic_list.append(NewTopic(name="topic5", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)