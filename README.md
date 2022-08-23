## Network Intrusion Detection With Machine Learning

Intrusion Detection System (IDS) software are used to detect malicious activities in a single computer or a network of computers. In order to detect an intrusion in network traffic, network packets are examined. Due to the lack of reliable test and validation datasets, anomaly-based intrusion detection approaches are suffering from consistent and accurate performance evolutions. Moreover, integrating machine learning techniques in this process can result in higher intrusion detection rates.

### About the Dataset

CICIDS2017 dataset contains benign and the most up-to-date common attacks, which resembles the true real-world data (PCAPs). It also includes the results of the network traffic analysis using CICFlowMeter with labeled flows based on the time stamp, source, and destination IPs, source and destination ports, protocols and attack (CSV files).

<table>
<tr><th colspan="2"><b><h3>Data Dictionary</h3></b></th></tr>

<tr>
<th>Dataset Source</th>
<td>

https://www.unb.ca/cic/datasets/ids-2017.html

</td>
</tr>

<tr>
<th>General Information</th>
<td>

| Number of Features | Number of Entries |
| :----------------: | :---------------: |
|         80         |      928391       |

</td>
</tr>

<tr>
<th>Target Classes</th>
<td>

|   C1   | C2  |  C3  |    C4    |     C5      |     C6     | C7  |
| :----: | :-: | :--: | :------: | :---------: | :--------: | :-: |
| benign | dos | ddos | portscan | brute_force | web_attack | bot |

</td>
</tr>

<tr>
<th>Feature Definition</th>
<td>

| Feature                 | Description                                                          |
| :---------------------- | :------------------------------------------------------------------- |
| dest port               | Destination port number                                              |
| flow duration           | Duration of ow in microseconds                                       |
| bwd packet len max      | Maximum packet length (backward direction)                           |
| bwd packet len min      | Minimum packet length (backward direction)                           |
| bwd packet len mean     | Mean packet length (backward direction)                              |
| bwd packet len std      | Packet length standard deviation (backward direction)                |
| flow IAT mean Mean      | packet inter-arrival time                                            |
| flow IAT std            | Standard deviation of packet inter-arrival time                      |
| flow IAT max            | Maximum packet inter-arrival time                                    |
| flow IAT min            | Minimum packet inter-arrival time                                    |
| fwd IAT total           | Total packet inter-arrival time (forward direction)                  |
| fwd IAT mean            | Mean packet inter-arrival time (forward direction)                   |
| fwd IAT std             | Standard deviation of packet inter-arrival time (forward direction)  |
| fwd IAT max             | Maximum packet inter-arrival time (forward direction)                |
| fwd IAT min             | Minimum packet inter-arrival time (forward direction)                |
| bwd IAT total           | Total packet inter-arrival time (backward direction)                 |
| bwd IAT mean            | Mean packet inter-arrival time (backward direction)                  |
| bwd IAT std             | Standard deviation of packet inter-arrival time (backward direction) |
| bwd IAT max             | Maximum packet inter-arrival time (backward direction)               |
| bwd IAT min             | Minimum packet inter-arrival time (backward direction)               |
| fwd PHS flags           | PSH (push) ag count (forward direction)                              |
| fwd packets s           | Number of forward packets per second                                 |
| max packet len          | Maximum packet length                                                |
| packet len mean         | Mean packet length                                                   |
| packet len std          | Standard deviation of packet length                                  |
| packet len var          | Packet length variance                                               |
| FIN flag coun           | t FIN (fnished) ag count                                             |
| SYN flag count          | SYN (synchronisation) ag count                                       |
| PSH flag count          | PSH (push) ag count                                                  |
| ACK flag count          | ACK (acknowledgement) ag count                                       |
| URG flag count          | URG (urgent) ag count                                                |
| avg packet size         | Average size of a packet                                             |
| avg bwd segment size    | Average size (backward direction)                                    |
| init win bytes forward  | Number of bytes sent in the initial window (forward direction)       |
| init win bytes backward | Number of bytes sent in the initial window (backward direction)      |
| active min              | Minimum time a ow was active before becoming idle                    |
| idle mean               | Mean time a ow was idle before becoming active                       |
| idle std                | Standard deviation of time a ow was idle before becoming active      |
| idle max                | Maximum time ow idle before becoming active                          |
| idle min                | Minimum time ow idle before becoming active                          |

</tr>
</td>
</table>

## Content

```bash
./
|   .gitignore
│   README.md
│
└───data/
│   │   intrusion_detection_sample_ata.csv
│
└───src/
    |   preprocess_eda.ipynb
    │   explore_models.ipynb.ipynb
    |   train_model.ipynb
    |
    └───ids-app/
            |
            └───client/
            |    |   dashboard.py
            |    |   feature_extractor.py
            |    |   flow.py
            |    |   main.py
            |    |
            |    └───flowmeter/
            |
            |
            |
            └───server/
                |   api.py
                |   Pipfile
                |   pipfile.lock
                |   Procfile
                |   requirements.txt
                |
                └───bin/
                |   |   start_server
                |
                └───classifier/
                |   |   model.py
                |   |
```

## Goals

- Analise the Canadian Institute Cybersecurity Intrusion Detection Dataset
- Train Machine Learning Models to detect network intrusion by classifying network packets
- Develop an application that enables users to classify captured network packets

## Conclusion

Traditional IDSs fail in the event of previously unseen attacks such as zero-day attacks (a software vulnerability unknown to its vendors yet). Therefore, the application of the machine learning approach as an engine for attack detection can be used as complementary to the traditional system.
