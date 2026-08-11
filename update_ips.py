import urllib.request
import re

target_url = "https://developer.amazon.com/amazonbot/ip-addresses"
req = urllib.request.Request(target_url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    # Amazon 페이지 HTML 가져오기
    html_content = urllib.request.urlopen(req).read().decode('utf-8')
    
    # 정규표현식으로 IPv4 및 CIDR 추출
    ips = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}(?:/\d{1,2})?\b', html_content)
    
    # 중복 제거 및 IP 정렬
    unique_ips = sorted(list(set(ips)))

    # txt 파일로 덮어쓰기 저장
    with open("amazonbot_ips.txt", "w") as f:
        f.write("\n".join(unique_ips))
        
    print(f"Successfully extracted {len(unique_ips)} IPs.")
    
except Exception as e:
    print(f"Error occurred: {e}")
