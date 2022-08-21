"""
Search for number of lost packets
https://www.reddit.com/r/learnpython/comments/wtwj0c/need_help_with_searching_log_file/
"""

import re


PATTERN_PKTLOST = r"^(\w{3} \d{1,2}) (\d{2}:\d{2}:\d{2}) (\d+\.\d+\.\d+\.\d+) : %SEC-6-IPACCESSLOGP: .+ (\d+\.\d+\.\d+\.\d+\(\d+\)) \-\> (\d+\.\d+\.\d+\.\d+\(\d+\)), (\d+) packets$"

SAMPLE = """
Jun 23 00:28:46 145.89.109.1 : %SEC-6-IPACCESSLOGP: list 120 denied tcp 121.18.238.123(0) -> 145.89.109.49(0), 15 packets
Jun 23 00:28:46 145.89.109.2 : 33 packets received
Jun 23 00:28:48 145.89.109.1 : %SEC-6-IPACCESSLOGP: list 120 denied tcp 121.18.238.123(0) -> 145.89.109.49(0), 9 packets
"""


def get_packet_loss_info(data):
    regex = re.compile(PATTERN_PKTLOST)
    for line in data.split("\n"):
        m = regex.search(line)
        if m:
            yield m.groups()


def print_loss_info(info):
    """
    Prints packet loss information:
        - IP address which logged the event
        - date & time
        - source
        - destination
        - number of packets lost

    Args:
        info (_type_): tuple of strings
    """

    date_str, time_str, machine, src, dest, num_packets = info
    print(f"@{machine} on {date_str} {time_str}\n  from {src} to {dest} lost {num_packets} packets")


def main() -> None:
    loss_info = get_packet_loss_info(SAMPLE)
    for item in loss_info:
        print_loss_info(item)


if __name__ == "__main__":
    main()
