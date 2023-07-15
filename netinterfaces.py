"""
https://www.reddit.com/r/learnpython/comments/ve34h9/loop_to_check_dictionary_object_for_key/
"""

NET_DATA = {
    "interfaces": {
        "GigabitEthernet1/0/1": {
            "dot1x_pae_authenticator": True,
            "switchport_access_vlan": "22",
            "switchport_mode": "access",
        },
        "GigabitEthernet1/0/2": {
            "switchport_access_vlan": "77",
            "switchport_mode": "access",
        },
        "GigabitEthernet1/0/3": {
            "switchport_mode": "trunk"
        },
        "GigabitEthernet1/0/4": {
            "switchport_access_vlan": "55",
            "switchport_mode": "access",
        },
    }
}


def filter_interfaces(ifaces):
    for k, v in ifaces.items():
        if (v["switchport_mode"] == "access" 
            and v["switchport_access_vlan"] != "77"
            and ("dot1x_pae_authenticator" not in v
            or not v["dot1x_pae_authenticator"])):
            yield k


def main() -> None:
    result = filter_interfaces(NET_DATA["interfaces"])
    for item in result:
        print(item)    

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
