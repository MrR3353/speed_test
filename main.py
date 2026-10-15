import argparse

import humanize
import requests

DEFAULT_URL = 'https://n1s1.hsmedia.ru/bd/10/00/bd1000ecf84d5cd747860f09e3288872/800x600_0xac120003_17349027241591266862.webp'


def to_mib_per_sec(bytes_per_sec: float) -> float:
    return bytes_per_sec / (1024 * 1024)


def download_speed_test(url: str, requests_num: int = 10):
    total_size_bytes = 0
    total_download_time = 0.0
    for i in range(requests_num):
        response = requests.get(url, timeout=5)
        time = response.elapsed.total_seconds()
        size = len(response.content)
        total_size_bytes += size
        total_download_time += time
        speed = size / time if time > 0 else float('inf')
        print(f'Request {i + 1}/{requests_num}; {size} bytes; {time} seconds; speed: {to_mib_per_sec(speed):.2f} MiB/s')

    avg_time = total_download_time / requests_num
    print(f'Total size: {humanize.naturalsize(total_size_bytes)}; total time: {total_download_time:.3f} seconds')
    print(f'Average request time: {avg_time:.3f} seconds')
    if total_download_time > 0:
        avg_speed = total_size_bytes / total_download_time
        print(f'Average download speed: {to_mib_per_sec(avg_speed):.2f} MiB/s')
    else:
        print('Average download speed: n/a (total download time is 0)')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Measure average internet download speed.')
    parser.add_argument('url', nargs='?', default=DEFAULT_URL, help='URL of a file to download (defaults to a sample image)')
    parser.add_argument('-n', '--requests-num', type=int, default=10, help='number of sequential requests to make')
    args = parser.parse_args()

    download_speed_test(args.url, args.requests_num)