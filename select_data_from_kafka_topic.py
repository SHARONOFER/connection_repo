#C:/Program Files/Python38/python.exe" "c:/Users/sharono/OneDrive - QuestarAuto/Desktop/python_project_test/select_data_from_kafka_topic.py"
# Import KafkaConsumer from Kafka library
from kafka import KafkaConsumer

# Import sys module
import sys

# Define server with port
bootstrap_servers = ['localhost:9092']

# Define topic name from where the message will recieve
topicName = 'users'

# Initialize consumer variable
consumer = KafkaConsumer (topicName, group_id ='group1',bootstrap_servers =
   bootstrap_servers)

# Read and print message from consumer
for msg in consumer:
 print("Topic Name=%s,Message=%s"%(msg.topic,msg.value))

# Terminate the script
sys.exit()