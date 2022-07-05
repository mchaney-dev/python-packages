# write config file and store in directory
def store_config():
  from clint import resources
  resources.init('', '')
  resources.user.write('./config/config.ini', 'content')
  
# OSX: '/Users/appuser/Library/Application Support/AppName/config.ini'
# Windows: 'C:\\Users\\appuser\\AppData\\Local\\Company\\AppName\\config.ini'
# Linux: '/home/appuser/.config/appname/config.ini'

# get ip for alternate mirror download
def get_ip():
  import socket
  
  print('Retrieving IP address for location-based mirrors.')
  ip = socket.gethostbyname(socket.gethostname())
  return ip

# use ip to determine country (mirrors are location-based)
def get_location():
  from ip2geotools.databases.noncommercial import DbIpCity
  import ipaddress
  from requests import get
  import pycountry
  
  response = DbIpCity.get(get_ip(), api_key='free')
  
  # if country code returns as 'ZZ', check if NAT is enabled
  if (response.country == 'ZZ'):
    # if address is private, get address of public interface
    if (ipaddress.ip_address(ip).is_private == True):
      ip = get('https://api.ipify.org').text
      # update response variable with public-facing address
      response = DbIpCity.get(ip, api_key='free')
      
  country = pycountry.countries.get(alpha_2=response.country)
  print('Country: ' + country)
  return country


def try_alternate_source(location: str):
  from bs4 import BeautifulSoup
  import requests
  
  alt_url = 'https://launchpad.net/ubuntu/+cdmirrors'
  print('Retrieving alternate mirrors from ' + alt_url + '.')
  session = requests.Session()
  data = session.get(alt_url)
  soup = BeautifulSoup(data.text)
  alternate_sources = []
  
  table = soup.find('table', {'id':'mirrors_list'})
  rows = list()
  for row in table.findAll('tr'):
    rows.append(row)
    
  for i in rows:
    pass 
  
  print('Mirrors available for ' + location + ': ' + str(alternate_sources.len())
  for i in enumerate(alternate_sources):
    print(alternate_sources[i])

# downloads current daily iso image for ubuntu server
def download_image():
  import sys
  import os
  import requests
  import urllib3
  from clint.textui import progress
  
  # url = 'https://cdimage.ubuntu.com/ubuntu-server/daily-live/current/kinetic-live-server-amd64.iso'
  
  # TEST CASE URL
  url = 'http://ipv4.download.thinkbroadband.com/50MB.zip'
  
  # create persistent http session for the download
  session = requests.Session()
  data = session.get(url, stream=True)
  # downloaded file will be stored in user's temp directory
  # before extraction to installation media (windows only)
  temp_dir = os.getenv('TMP', 'TEMP')
  # file_name = temp_dir + '/ubuntu_server_image.iso'
  
  # TEST CASE FILE NAME
  file_name = temp_dir + '/example_file.zip'
  
  # begin error handling
  try:
    # check for http response indicating successful connection 
    # (status codes 200-299)
    if ((data.status_code >= 200) and (data.status_code <= 299)):
      print('Connection established.')
      # open file in binary writing mode
      with open(file_name, 'wb') as f:
        # get file size from http header
        total_length = int(data.headers.get('content-length'))
        # convert bytes to MB
        file_mb_size = (total_length / 1024) + 1
        # specify chunk size (currently about 10 MB, 1 MB = 1024 bytes)
        data_chunk_size = 1024 * 10
    
        # render progress animation in console
        for chunk in progress.mill(data.iter_content(chunk_size=data_chunk_size), label='Downloading file ... ', hide=None, expected_size=file_mb_size, every=10):
          if chunk:
            f.write(chunk)
            f.flush()
    # if http response code is not successful, raise ConnectionError
    else:
      raise(ConnectionError())
    
  # handle ConnectionError if raised
  except ConnectionError():
    # call function to find alternate iso mirrors
    # based on detected country
    try_alternate_source(get_location())
  
  # check if file was downloaded
  finally:
    if (os.path.exists(file_name)):
      print('Done.')
    # if file was not detected after multiple download attempts, 
    # raise FileNotFoundError and exit
    else:
      raise(FileNotFoundError())
      exit(1)
    
get_alternate_source(get_location())
input('Press ENTER to exit')
