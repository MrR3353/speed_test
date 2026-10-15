import humanize
import requests


def download_speed_test(url: str, requests_num: int = 10):
    total_size_bytes = 0
    total_download_time = 0
    for i in range(requests_num):
        response = requests.get(url, timeout=5)
        time = response.elapsed.total_seconds()
        size = len(response.content)
        total_size_bytes += size
        total_download_time += time
        speed = size / time
        print(f'Request {i + 1}/{requests_num}; {size} bytes; {time} seconds; speed: {humanize.naturalsize(speed, binary=True)}/s')

    print(f'Total size: {humanize.naturalsize(total_size_bytes, binary=True)}; total time: {total_download_time} seconds')
    avg_speed = total_size_bytes / total_download_time
    print(f'Average download speed: {avg_speed} byte/s OR {humanize.naturalsize(avg_speed, binary=True)}/s')

if __name__ == '__main__':
    # 579.0 kB or 565 kB
    url = 'https://n1s1.hsmedia.ru/bd/10/00/bd1000ecf84d5cd747860f09e3288872/800x600_0xac120003_17349027241591266862.webp'
    download_speed_test(url, 10)