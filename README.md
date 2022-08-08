## Network Intrusion Detection With Machine Learning

### Data Dictionary

<table>
<tr>
<th>General Information</th>
<td>

| Number of Chosen Features |
| :-----------------------: |
|            40             |

    </td>
    <td>

| Number of Entries |
| :---------------: |
|      820722       |

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
