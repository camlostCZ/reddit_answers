"""
https://www.reddit.com/r/learnpython/comments/u8h8r7/list_duplicates_of_a_list_in_another_list/
"""

import re
from collections import Counter


ASGS = [
    "asg-lc-crl-tst-turfpari-rtl20220124153420214800000001",
    "asg-lc-crl-tst-turfpari-rtl20220330150836189100000001",
    "asg-lc-dpr-dev1-app_hode-hdh20220420140650975800000001",
    "asg-lc-crl-di1-ledger-manager-rtl20220414144111344500000001",
    "asg-lc-dpr-dev1-app_hode-hdh20220420143831109200000001",
    "asg-lc-crl-tst-art-manager-rtl20220124162240173500000001",
    "asg-lc-crl-tst-art-manager-rtl20220330150933020900000001",
    "asg-lc-bck-ope-backoh-oh20201021134525920100000001",
    "asg-lc-bck-ope-springbootadmin-oh20201021134526042200000002",
]

PATTERN =  r"^(.+)-([^-]+)$"

rx = re.compile(PATTERN)

# Either these lines ...
lst = []
for item in ASGS:
    m = rx.match(item)
    if m:
        lst.append(m.group(1))
result = Counter(lst)

# ... or an ugly one-liner:
result = Counter([m.group(1) for x in ASGS if (m := re.match(rx, x))])

for k, v in result.items():
    print(f"{k}:  {v}")

