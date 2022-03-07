from subprocess import Popen, PIPE
import re
from requests import get

API_ENDPOINT = 'http://www.ip-api.com/json/'

def extractip(url:str) -> str:
    """Get ip address from the output with regerx
    """
    try:
        pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
        return pattern.search(url)[0]
    except:
        return None
    
def getlocation(ip:str) -> str:
    """Send ip to  http://www.ip-api.com 
    to detect the country
    """
    print(ip)
    request_url = get(API_ENDPOINT + ip)
    try:
        return request_url.json()['country']
    except:
        return "Private Network"        

def traceroute(url:str):
    pipe = Popen(['tracert', url], stdout=PIPE) #Popen exeutes the commands in terminal via python

    while True:
        result = str(pipe.stdout.readline()).replace('\\r','').replace('\\n','').strip()
        result_ip = extractip(result)

        if result_ip is not None :
            print(getlocation(result_ip))              
        if not result:
            print("Request failed")


if __name__ == "__main__":
    input = input('Enter the URL:')
    print('please wait for data to receive')
    try:
        traceroute(input)      
    except :
        print('Something went wrong!')
   