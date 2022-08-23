from scapy.all import *
from flowmeter.flow import Flow
from flowmeter.features.context.packet_flow_key import get_packet_flow_key
from flowmeter.features.context.packet_direction import PacketDirection

import pandas as pd


class Features_Extractor:
    def __init__(self, file):
        self.file = file
        self.packets = []
        self.df = None

        self.features = ['destination_port', 'flow_duration', 'total_fwd_packets',
                         'total_backward_packets', 'total_length_of_fwd_packets',
                         'total_length_of_bwd_packets', 'fwd_packet_length_max',
                         'fwd_packet_length_min', 'fwd_packet_length_mean',
                         'fwd_packet_length_std', 'bwd_packet_length_max',
                         'bwd_packet_length_min', 'bwd_packet_length_mean',
                         'bwd_packet_length_std', 'flow_bytes/s', 'flow_packets/s',
                         'flow_iat_mean', 'flow_iat_std', 'flow_iat_max', 'flow_iat_min',
                         'fwd_iat_total', 'fwd_iat_mean', 'fwd_iat_std', 'fwd_iat_max',
                         'fwd_iat_min', 'bwd_iat_total', 'bwd_iat_mean', 'bwd_iat_std',
                         'bwd_iat_max', 'bwd_iat_min', 'fwd_psh_flags', 'fwd_header_length',
                         'bwd_header_length', 'fwd_packets/s', 'bwd_packets/s',
                         'min_packet_length', 'max_packet_length', 'packet_length_mean',
                         'packet_length_std', 'packet_length_variance', 'fin_flag_count',
                         'syn_flag_count', 'rst_flag_count', 'psh_flag_count', 'ack_flag_count',
                         'urg_flag_count', 'ece_flag_count', 'down/up_ratio',
                         'average_packet_size', 'avg_fwd_segment_size', 'avg_bwd_segment_size',
                         'fwd_header_length.1', 'subflow_fwd_packets', 'subflow_fwd_bytes',
                         'subflow_bwd_packets', 'subflow_bwd_bytes', 'init_win_bytes_forward',
                         'init_win_bytes_backward', 'act_data_pkt_fwd', 'min_seg_size_forward',
                         'active_mean', 'active_std', 'active_max', 'active_min', 'idle_mean',
                         'idle_std', 'idle_max', 'idle_min', 'label', 'is_intrusion']

        self.set_packets()
        self.set_dataFrame()

    def set_packets(self):
        packets = []
        for packet in PcapReader(self.file):
            if len(packets) <= 1000:
                if packet.getlayer(TCP):
                    packets.append(packet)
            else:
                break
        self.packets = packets

    def set_dataFrame(self):
        final_data = []
        for p in self.packets:
            if p.getlayer(TCP):
                flow = Flow(p, PacketDirection.FORWARD)
                flow.add_packet(p, PacketDirection.FORWARD)
                flow.add_packet(p, PacketDirection.FORWARD)
                data = flow.get_data()

                final_data.append(data)
        df = pd.DataFrame(final_data)
        df = df.reindex(columns=self.features[:-2])
        self.df = df.sample(20)
