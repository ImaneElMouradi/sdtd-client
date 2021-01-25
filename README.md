# sdtd-client

### Description 

- `country_crimes.py` est un script qui permet de créer un kafka-producer grâce à la ligne : `producer = KafkaProducer(bootstrap_servers='172.17.0.2:9092')`, puis de générer des données selon le pays choisi (France, USA, Russia) sous la forme : (city_key, incident_type, incident_latitude, incident_longitude, incident_description) et enfin les envoyer au cluster de Kafka grâce au Producer.
