"""
https://www.reddit.com/r/learnpython/comments/ts9gjs/find_ip_in_log_file_script_help/
"""

IP_ADDRESS = "192.168.75.1"
PATH_LOG = "./resources/maillog_sample.log"


def ipaddr_count(ipaddr: str, s: str) -> int:
    result = 1 if ipaddr in s else 0
    return result


def search_ipaddr_in_file(ipaddr: str, path: str) -> int:
    result = 0
    with open(path) as fr:
        for each_line in fr:
            result += ipaddr_count(ipaddr, each_line)
    return result


def main() -> None:
    count = search_ipaddr_in_file(IP_ADDRESS, PATH_LOG)
    print(f"Number of IP address {IP_ADDRESS} occurences: {count}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user.")
