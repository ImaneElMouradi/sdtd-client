#!/usr/bin/python3

from kafka import KafkaProducer
import numpy as np
from sys import argv, exit
from time import time, sleep
import random


crimes = ["meurtre", "vol", "torture",
          "enlèvement", "extorsion", "destruction"]

COUNTRY_PROFILES = {
    "France": {'city_key': 'FR', 'incident_type': crimes, 'incident_latitude': (-90, 90), 'incident_longitude': (-180, 180), 'incident_description': 'DESCRIPTION DU CRIME'},
    "USA": {'city_key': 'US', 'incident_type': crimes, 'incident_latitude': (-90, 90), 'incident_longitude': (-180, 180), 'incident_description': 'DESCRIPTION DU CRIME'},
    "Russia": {'city_key': 'RU', 'incident_type': crimes, 'incident_latitude': (-90, 90), 'incident_longitude': (-180, 180), 'incident_description': 'DESCRIPTION DU CRIME'},

}

# check for arguments, exit if wrong
if len(argv) != 2 or argv[1] not in COUNTRY_PROFILES.keys():
    print("please provide a valid COUNTRY name:")
    for key in COUNTRY_PROFILES.keys():
        print(f"  * {key}")
    print(f"\nformat: {argv[0]} COUNTRY_NAME")
    exit(1)

profile_name = argv[1]
profile = COUNTRY_PROFILES[profile_name]

# set up the producer
producer = KafkaProducer(bootstrap_servers='172.17.0.2:9092')
count = 1

# until ^C
while True:
    city_key = profile['city_key']
    num = random.randint(0, 5)
    incident_type = profile['incident_type'][num]
    incident_latitude = np.random.normal(
        profile['incident_latitude'][0], profile['incident_latitude'][1])
    incident_longitude = np.random.normal(
        profile['incident_longitude'][0], profile['incident_longitude'][1])
    incident_description = profile['incident_description']

    # create CSV structure
    msg = f'{time()},{profile_name},{city_key},{incident_type},{incident_latitude},{incident_longitude},{incident_description}'

    # send to Kafka
    producer.send('crimes', bytes(msg, encoding='utf8'))
    print(f'sending data to kafka, #{count}')

    count += 1
    sleep(.5)
