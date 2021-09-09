#!/usr/bin/env python3

import os
import random
import requests
import json

from .arguments import args
from .logger import logger

TEXT_GEN_API_VAR = 'DEEP_AI_KEY'
DEFAULT_KEY = '9d414130-ca3d-4169-ab5e-0c0c2f17b65f'

words = [
  'The', 'he', 'at', 'but', 'there', 'of', 'was', 'be', 'not', 'use', 'and', 'for', 'this', 'what', 'an', 'a', 'on', 'have', 'all', 'each',
  'to', 'are', 'from', 'were', 'which', 'in', 'as', 'or', 'we', 'she', 'is', 'with', 'ine', 'when', 'do', 'you', 'his', 'had', 'your',
  'how', 'that', 'they', 'by', 'can', 'their', 'it', 'I', 'word', 'said', 'if'
]

with open(os.path.join(os.path.dirname(__file__), './data/cities.json')) as cities_file:
  cities = json.load(cities_file)

gop_members = [
  'Gary VanDeaver', 'Bryan Slaton', 'Cecil Bell Jr.', 'Keith Bell', 'Cole Hefner', 'Matt Schaefer', 'Jay Dean', 'Cody Harris',
  'Chris Paddie', 'Travis Clardy', 'Kyle Kacal', 'Ben Leman', 'John N. Raney', 'Steve Toth', 'Will Metcalf', 'John Cyrier', 'Ernest Bailes',
  'James White', 'Terry Wilson', 'Dade Phelan', 'Mayes Middleton', 'Greg Bonnen', 'Cody Vasut', 'Brooks Landgraf', 'Tom Craddick',
  'Dustin Burrows', 'John Frullo', 'Phil Stephenson', 'John T. Smithee', 'Four Price', 'Ken King', 'Candy Noble', 'Stephanie Klick',
  'Jeff Cason', 'Matt Krause', 'Tony Tinderholt', 'David Cook', 'Craig Goldman', 'Giovanni Capriglione', 'Charlie Geren', 'Sam Harless',
  'Dan Huberty', 'Briscoe Cain', 'Dennis Paul', 'Tom Oliverson', 'Mike Schofield'
]

with open(os.path.join(os.getcwd(), "bot", "data", "firstnameGirl.json")) as fng:
  firstNames = json.loads(fng.read())
  firstNames = firstNames["names"]

with open(os.path.join(os.getcwd(), "bot", "data", "firstnameBoy.json")) as fnb:
  maleFirstNames = json.loads(fnb.read())
  maleFirstNames = maleFirstNames["names"]

with open(os.path.join(os.getcwd(), "bot", "data", "lastname.json")) as ln:
  lastNames = json.loads(ln.read())
  lastNames = lastNames["names"]

with open(os.path.join(os.getcwd(), "bot", "data", "zips.json")) as z:
  zip_codes = json.loads(z.read())

# Seeds for text body generation
gpt2_prompts = [
  'My neighbor got an illegal abortion.', 'I suspect my father has violated the abortion ban.',
  random.choice(firstNames) + ' ' + random.choice(lastNames) + ' is helping people get abortions.',
  random.choice(gop_members) + ' has been sneaking around the abortion clinic in ' + random.choice(list(cities)) + '.'
]

info_location = [
  'A friend saw them', 'I work at the clinic', 'I know his secretary', 'He told me at the club', 'The police report', 'His wife told me',
  'From a coworker', 'From a neighbor', 'From a family member.', 'Heard from a friend', 'a relative told me', 'a private source',
  'A confession at church', 'I know their cousin', 'a taxi driver', 'From a cashier', 'Got a confidential tip', 'From a fellow parent',
  'a concerned citizen', 'From a relative.', 'A PP volunteer', 'A charity worker', 'A social worker', 'From my friend who knows cops',
  'from a lawyer', 'From a government employee'
]

# TX IPs gathered from here: https://www.xmyip.com/ip-addresses/united--states/texas
ips = [
  "66.136.125.",  # Abilene
  "64.46.160.",  # Addison
  "24.27.72.",  # Allen
  "65.65.132.",  # Alpine
  "64.243.53.",  # Alvarado
  "50.175.228.",  # Alvin
  "50.175.229.",  # Alvin
  "50.26.131.",  # Amarillo
  "12.163.172.",  # Angleton
  "23.117.126.",  # Arlington
  "68.93.254.",  # Arlington
  "8.34.145.",  # Austin
  "12.204.50.",  # Austin
  "24.153.156.",  # Austin
  "24.155.228.",  # Austin
  "50.94.23.",  # Austin
  "66.193.112.",  # Austin
  "66.193.113.",  # Austin
  "24.173.59.",  # Beaumont
  "63.174.138.",  # Beaumont
  "66.169.186.",  # Bedford
  "38.110.200.",  # Bellaire
  "24.219.225.",  # Benbrook
  "64.40.218.",  # Brownwood
  "64.202.78.",  # Carrollton
  "24.32.117.",  # Clarksville
  "50.15.108.",  # Conroe
  "50.21.240.",  # Conroe
  "64.158.39.",  # Conroe
  "66.136.21.",  # Conroe
  "66.170.212.",  # Conroe
  "64.194.96.",  # Copperas Cove
  "67.67.45.",  # Coppell
  "67.63.164.",  # Corpus Christi
  "4.26.150.",  # Dallas
  "4.68.19.",  # Dallas
  "4.71.196.",  # Dallas
  "12.21.88.",  # Dallas
  "12.41.199.",  # Dallas
  "12.53.23.",  # Dallas
  "12.56.225.",  # Dallas
  "12.96.170.",  # Dallas
  "12.132.16.",  # Dallas
  "12.134.216.",  # Dallas
  "12.135.64.",  # Dallas
  "12.167.120.",  # Dallas
  "12.182.130.",  # Dallas
  "12.209.171.",  # Dallas
  "12.209.212.",  # Dallas
  "12.210.242.",  # Dallas
  "12.233.59.",  # Dallas
  "17.253.118.",  # Dallas
  "23.119.13.",  # Dallas
  "23.119.14.",  # Dallas
  "23.119.15.",  # Dallas
  "24.242.248.",  # Dallas
  "23.33.244.",  # Dallas
  "23.33.245.",  # Dallas
  "23.33.246.",  # Dallas
  "23.33.247.",  # Dallas
  "23.95.39.",  # Dallas
  "23.216.55.",  # Dallas
  "23.218.192.",  # Dallas
  "24.153.219.",  # Dallas
  "24.162.85.",  # Dallas
  "24.175.0.",  # Dallas
  "24.219.28.",  # Dallas
  "24.219.165.",  # Dalla
  "32.144.6.",  # Dallas
  "32.144.7.",  # Dallass
  "32.144.40.",  # Dallas
  "32.145.187.",  # Dallas
  "32.149.78.",  # Dallas
  "32.149.122.",  # Dallas
  "32.149.194.",  # Dallas
  "32.149.195.",  # Dallas
  "32.149.196.",  # Dallas
  "32.149.197.",  # Dallas
  "32.153.78.",  # Dallas
  "32.153.79.",  # Dallas
  "32.153.80.",  # Dallas
  "32.153.81.",  # Dallas
  "32.153.82.",  # Dallas
  "32.153.83.",  # Dallas
  "32.153.84.",  # Dallas
  "32.153.85.",  # Dallas
  "32.153.86.",  # Dallas
  "32.153.87.",  # Dallas
  "32.153.88.",  # Dallas
  "32.153.89.",  # Dallas
  "32.153.90.",  # Dallas
  "32.153.91.",  # Dallas
  "32.153.92.",  # Dallas
  "32.153.93.",  # Dallas
  "32.153.94.",  # Dallas
  "32.153.95.",  # Dallas
  "32.153.96.",  # Dallas
  "32.153.97.",  # Dallas
  "32.153.98.",  # Dallas
  "32.153.104.",  # Dallas
  "32.168.139.",  # Dallas
  "38.107.254.",  # Dallas
  "40.139.103.",  # Dallas
  "50.58.239.",  # Dallas
  "50.84.221.",  # Dallas
  "54.182.134.",  # Dallas
  "63.25.84.",  # Dallas
  "63.97.48.",  # Dallas
  "63.133.145.",  # Dallas
  "63.133.167.",  # Dallas
  "63.158.21.",  # Dallas
  "63.234.233.",  # Dallas
  "64.56.170.",  # Dallas
  "64.125.5.",  # Dallas
  "64.130.250.",  # Dallas
  "64.145.92.",  # Dallas
  "64.195.173.",  # Dallas
  "64.197.59.",  # Dallas
  "64.205.163.",  # Dallas
  "64.245.210.",  # Dallas
  "65.44.75.",  # Dallas
  "65.69.15.",  # Dallas
  "65.71.67.",  # Dallas
  "65.118.54.",  # Dallas
  "65.152.83.",  # Dallas
  "65.227.224.",  # Dallas
  "66.106.98.",  # Dallas
  "66.155.134.",  # Dallas
  "66.155.135.",  # Dallas
  "66.253.55.",  # Dallas
  "67.48.192.",  # Dallas
  "67.110.83.",  # Dallas
  "67.192.56.",  # Dallas
  "67.216.80.",  # Dallas
  "67.216.81.",  # Dallas
  "67.216.82.",  # Dallas
  "67.216.83.",  # Dallas
  "67.216.84.",  # Dallas
  "67.216.85.",  # Dallas
  "67.216.86.",  # Dallas
  "67.216.87.",  # Dallas
  "67.216.88.",  # Dallas
  "67.216.89.",  # Dallas
  "67.216.90.",  # Dallas
  "67.216.91.",  # Dallas
  "67.216.92.",  # Dallas
  "67.216.93.",  # Dallas
  "67.216.94.",  # Dallas
  "67.216.95.",  # Dallas
  "68.90.101.",  # Dallas
  "68.95.146.",  # Dallas
  "68.109.248.",  # Dallas
  "47.184.118.",  # Denton
  "47.184.119.",  # Denton
  "47.184.120.",  # Denton
  "47.184.121.",  # Denton
  "24.206.145.",  # Denton
  "24.219.171.",  # Denton
  "68.116.255.",  # Denton
  "67.61.107.",  # DeSoto
  "67.10.46.",  # Edinburg
  "67.10.91.",  # Edinburg
  "24.242.98.",  # El Paso
  "65.117.156.",  # Euless
  "47.185.148.",  # Flower Mound
  "47.187.133.",  # Flower Mound
  "12.251.72.",  # Fort Stockton
  "12.184.253.",  # Fort Worth
  "12.210.27.",  # Fort Worth
  "12.203.146.",  # Fort Worth
  "12.203.147.",  # Fort Worth
  "12.184.254.",  # Fort Worth
  "12.90.92.",  # Fort Worth
  "24.182.108.",  # Fort Worth
  "24.219.224.",  # Fort Worth
  "24.219.163.",  # Fort Worth
  "47.32.223.",  # Fort Worth
  "50.11.19.",  # Fort Worth
  "68.113.154.",  # Fort Worth
  "50.207.209.",  # Friendswood
  "24.155.190.",  # Frisco
  "45.21.225.",  # Frisco
  "47.186.248.",  # Garland
  "66.112.246.",  # Georgetown
  "64.134.76.",  # Grapevine
  "66.169.188.",  # Haltom City
  "66.169.189.",  # Haltom City
  "8.23.67.",  # Houston
  "12.8.38.",  # Houston
  "12.43.39.",  # Houston
  "12.68.245.",  # Houston
  "12.155.35.",  # Houston
  "12.195.152.",  # Houston
  "12.198.216.",  # Houston
  "12.219.120.",  # Houston
  "16.35.199.",  # Houston
  "16.160.30.",  # Houston
  "16.186.156.",  # Houston
  "24.206.72.",  # Houston
  "24.206.173.",  # Houston
  "24.238.235.",  # Houston
  "34.9.77.",  # Houston
  "34.131.207.",  # Houston
  "38.100.150.",  # Houston
  "45.17.135.",  # Houston
  "45.33.171.",  # Houston
  "50.24.234.",  # Houston
  "50.162.2.",  # Houston
  "50.162.44.",  # Houston
  "50.206.107.",  # Houston
  "63.145.123.",  # Houston
  "63.236.223.",  # Houston
  "64.211.171.",  # Houston
  "65.16.135.",  # Houston
  "65.122.33.",  # Houston
  "65.124.92.",  # Houston
  "65.201.78.",  # Houston
  "66.3.44.",  # Houston
  "66.3.45.",  # Houston
  "66.3.46.",  # Houston
  "66.67.94.",  # Houston
  "66.78.229.",  # Houston
  "66.78.230.",  # Houston
  "66.78.231.",  # Houston
  "66.161.197.",  # Houston
  "68.91.35.",  # Hurst
  "50.84.165.",  # Irving
  "50.84.181.",  # Irving
  "64.129.174.",  # Irving
  "64.195.138.",  # Irving
  "64.195.139.",  # Irving
  "64.195.140.",  # Irving
  "64.195.141.",  # Irving
  "64.195.142.",  # Irving
  "64.195.143.",  # Irving
  "66.25.22.",  # Irving
  "64.244.179.",  # Keller
  "67.76.51.",  # Keller
  "24.32.224.",  # Kingwood
  "68.88.193.",  # Lancaster
  "47.187.76.",  # Lewisville
  "24.204.52.",  # Longview
  "66.185.67.",  # Longview
  "12.38.125.",  # Lubbock
  "50.94.139.",  # Lubbock
  "67.22.223.",  # Lubbock
  "38.114.200.",  # Lufkin
  "12.218.97.",  # McAllen
  "24.243.98.",  # McAllen
  "24.243.150.",  # McAllen
  "24.243.151.",  # McAllen
  "24.243.152.",  # McAllen
  "38.103.227.",  # McAllen
  "67.10.39.",  # McAllen
  "67.10.80.",  # McAllen
  "47.182.27.",  # McKinney
  "66.190.64.",  # Mineral Wells
  "50.30.144.",  # Missouri City
  "66.76.77.",  # Normangee
  "24.32.137.",  # Odessa
  "50.252.46.",  # Pasadena
  "67.219.174.",  # Perryton
  "24.242.89.",  # Pflugerville
  "67.10.20.",  # Pharr
  "24.173.213.",  # Plano
  "47.185.248.",  # Plano
  "50.84.81.",  # Plano
  "65.42.136.",  # Plano
  "65.71.223.",  # Plano
  "66.138.79.",  # Plano
  "66.140.20.",  # Plano
  "66.143.7.",  # Plano
  "67.65.12.",  # Plano
  "67.66.13.",  # Plano
  "68.20.41.",  # Plano
  "68.20.53.",  # Plano
  "68.22.119.",  # Plano
  "68.72.56.",  # Plano
  "68.90.204.",  # Plano
  "68.93.19.",  # Plano
  "68.93.208.",  # Plano
  "23.113.179.",  # Richardson
  "23.123.121.",  # Richardson
  "23.126.17.",  # Richardson
  "24.27.103.",  # Richardson
  "45.23.148.",  # Richardson
  "47.186.44.",  # Richardson
  "47.186.233.",  # Richardson
  "63.204.90.",  # Richardson
  "63.204.168.",  # Richardson
  "64.148.35.",  # Richardson
  "64.149.192.",  # Richardson
  "65.69.103.",  # Richardson
  "65.70.203.",  # Richardson
  "66.138.5.",  # Richardson
  "67.39.101.",  # Richardson
  "63.199.94.",  # Richardson
  "63.203.212.",  # Richardson
  "63.203.213.",  # Richardson
  "64.109.192.",  # Richardson
  "64.123.188.",  # Richardson
  "64.218.64.",  # Richardson
  "64.252.212.",  # Richardson
  "64.252.213.",  # Richardson
  "64.252.214.",  # Richardson
  "64.252.215.",  # Richardson
  "64.252.216.",  # Richardson
  "64.252.217.",  # Richardson
  "64.252.218.",  # Richardson
  "64.252.219.",  # Richardson
  "64.252.220.",  # Richardson
  "64.252.221.",  # Richardson
  "64.252.222.",  # Richardson
  "64.252.223.",  # Richardson
  "64.252.224.",  # Richardson
  "64.252.225.",  # Richardson
  "64.252.226.",  # Richardson
  "64.252.227.",  # Richardson
  "64.252.228.",  # Richardson
  "64.252.229.",  # Richardson
  "64.252.230.",  # Richardson
  "64.252.231.",  # Richardson
  "64.252.232.",  # Richardson
  "64.252.233.",  # Richardson
  "64.252.234.",  # Richardson
  "64.252.235.",  # Richardson
  "64.252.236.",  # Richardson
  "64.252.237.",  # Richardson
  "64.252.238.",  # Richardson
  "65.65.49.",  # Richardson
  "65.68.3.",  # Richardson
  "65.68.4.",  # Richardson
  "65.64.221.",  # Richardson
  "65.64.222.",  # Richardson
  "65.64.223.",  # Richardson
  "66.73.64.",  # Richardson
  "66.136.184.",  # Richardson
  "66.136.185.",  # Richardson
  "66.136.186.",  # Richardson
  "66.136.187.",  # Richardson
  "66.137.185.",  # Richardson
  "66.138.90.",  # Richardson
  "66.142.202.",  # Richardson
  "67.38.82.",  # Richardson
  "67.64.87.",  # Richardson
  "67.117.108.",  # Richardson
  "67.121.40.",  # Richardson
  "67.122.104.",  # Richardson
  "67.123.146.",  # Richardson
  "68.23.31.",  # Richardson
  "68.72.157.",  # Richardson
  "68.72.158.",  # Richardson
  "68.72.0.",  # Richardson
  "68.72.114.",  # Richardson
  "68.89.77.",  # Richardson
  "68.91.19.",  # Richardson
  "63.174.141.",  # Rocksprings
  "66.235.81.",  # Rosenberg
  "8.9.196.",  # San Antonio
  "12.7.34.",  # San Antonio
  "12.7.35.",  # San Antonio
  "12.27.88.",  # San Antonio
  "12.190.120.",  # San Antonio
  "12.211.20.",  # San Antonio
  "15.105.182.",  # San Antonio
  "15.109.33.",  # San Antonio
  "15.109.99.",  # San Antonio
  "15.110.110.",  # San Antonio
  "15.116.44.",  # San Antonio
  "15.118.122.",  # San Antonio
  "15.118.179.",  # San Antonio
  "15.120.12.",  # San Antonio
  "15.120.150.",  # San Antonio
  "15.121.102.",  # San Antonio
  "15.122.12.",  # San Antonio
  "15.126.8.",  # San Antonio
  "15.128.254.",  # San Antonio
  "15.129.7.",  # San Antonio
  "15.129.118.",  # San Antonio
  "15.132.18.",  # San Antonio
  "15.135.133.",  # San Antonio
  "15.135.219.",  # San Antonio
  "15.137.122.",  # San Antonio
  "15.137.172.",  # San Antonio
  "15.140.41.",  # San Antonio
  "15.141.27.",  # San Antonio
  "15.142.164.",  # San Antonio
  "15.143.175.",  # San Antonio
  "15.145.145.",  # San Antonio
  "15.145.242.",  # San Antonio
  "15.149.7.",  # San Antonio
  "15.149.233.",  # San Antonio
  "15.155.5.",  # San Antonio
  "15.152.9.",  # San Antonio
  "15.153.121.",  # San Antonio
  "15.153.133.",  # San Antonio
  "15.162.156.",  # San Antonio
  "15.162.231.",  # San Antonio
  "15.165.122.",  # San Antonio
  "15.169.145.",  # San Antonio
  "15.169.231.",  # San Antonio
  "15.170.117.",  # San Antonio
  "15.173.25.",  # San Antonio
  "15.173.118.",  # San Antonio
  "15.173.231.",  # San Antonio
  "15.174.40.",  # San Antonio
  "15.176.53.",  # San Antonio
  "15.177.123.",  # San Antonio
  "15.177.176.",  # San Antonio
  "15.177.254.",  # San Antonio
  "15.180.1.",  # San Antonio
  "15.180.224.",  # San Antonio
  "15.181.177.",  # San Antonio
  "15.183.87.",  # San Antonio
  "15.183.211.",  # San Antonio
  "15.188.81.",  # San Antonio
  "15.191.51.",  # San Antonio
  "15.193.183.",  # San Antonio
  "15.193.203.",  # San Antonio
  "15.204.130.",  # San Antonio
  "15.204.186.",  # San Antonio
  "15.208.102.",  # San Antonio
  "15.209.138.",  # San Antonio
  "15.213.214.",  # San Antonio
  "15.213.241.",  # San Antonio
  "15.214.133.",  # San Antonio
  "15.214.237.",  # San Antonio
  "15.216.199.",  # San Antonio
  "12.219.40.",  # San Antonio
  "15.224.247.",  # San Antonio
  "15.225.148.",  # San Antonio
  "15.226.90.",  # San Antonio
  "15.227.214.",  # San Antonio
  "15.235.202.",  # San Antonio
  "15.235.203.",  # San Antonio
  "15.243.241.",  # San Antonio
  "15.248.37.",  # San Antonio
  "15.252.43.",  # San Antonio
  "15.252.185.",  # San Antonio
  "15.255.94.",  # San Antonio
  "15.150.168.",  # San Antonio
  "15.150.169.",  # San Antonio
  "15.155.249.",  # San Antonio
  "40.141.126.",  # San Antonio
  "15.138.0.",  # San Antonio
  "15.138.1.",  # San Antonio
  "15.154.136.",  # San Antonio
  "15.154.137.",  # San Antonio
  "15.131.196.",  # San Antonio
  "15.131.197.",  # San Antonio
  "15.131.198.",  # San Antonio
  "15.131.199.",  # San Antonio
  "15.131.200.",  # San Antonio
  "15.143.78.",  # San Antonio
  "15.150.12.",  # San Antonio
  "15.158.33.",  # San Antonio
  "15.160.200.",  # San Antonio
  "15.160.201.",  # San Antonio
  "15.160.202.",  # San Antonio
  "15.176.129.",  # San Antonio
  "15.193.69.",  # San Antonio
  "15.193.70.",  # San Antonio
  "15.211.169.",  # San Antonio
  "15.132.71.",  # San Antonio
  "15.132.72.",  # San Antonio
  "15.190.132.",  # San Antonio
  "15.156.247.",  # San Antonio
  "15.156.248.",  # San Antonio
  "15.219.34.",  # San Antonio
  "15.176.79.",  # San Antonio
  "15.176.80.",  # San Antonio
  "15.176.81.",  # San Antonio
  "15.133.222.",  # San Antonio
  "12.207.43.",  # San Antonio
  "15.243.228.",  # San Antonio
  "15.243.229.",  # San Antonio
  "15.244.168.",  # San Antonio
  "15.250.151.",  # San Antonio
  "15.161.146.",  # San Antonio
  "15.162.246.",  # San Antonio
  "15.162.247.",  # San Antonio
  "15.162.248.",  # San Antonio
  "15.162.249.",  # San Antonio
  "15.118.251.",  # San Antonio
  "15.122.23.",  # San Antonio
  "15.128.234.",  # San Antonio
  "15.128.235.",  # San Antonio
  "15.134.233.",  # San Antonio
  "15.134.234.",  # San Antonio
  "15.117.166.",  # San Antonio
  "15.157.163.",  # San Antonio
  "15.159.219.",  # San Antonio
  "15.160.97.",  # San Antonio
  "15.160.98.",  # San Antonio
  "15.160.99.",  # San Antonio
  "15.189.87.",  # San Antonio
  "15.189.88.",  # San Antonio
  "15.120.172.",  # San Antonio
  "15.181.151.",  # San Antonio
  "15.181.152.",  # San Antonio
  "15.221.80.",  # San Antonio
  "15.237.79.",  # San Antonio
  "24.173.86.",  # San Antonio
  "24.243.33.",  # San Antonio
  "50.84.228.",  # San Antonio
  "50.95.50.",  # San Antonio
  "52.239.178.",  # San Antonio
  "67.155.93.",  # San Antonio
  "68.98.252.",  # San Antonio
  "24.155.227.",  # San Marcos
  "64.134.224.",  # San Marcos
  "66.90.132.",  # San Marcos
  "38.65.97.",  # Schertz
  "45.21.35.",  # Schertz
  "67.78.77.",  # Seguin
  "67.179.27.",  # Seguin
  "47.182.60.",  # Sherman
  "64.22.112.",  # Spring
  "65.174.248.",  # Stafford
  "67.21.188.",  # Stephenville
  "12.205.32.",  # Sugar Land
  "50.162.51.",  # Sugar Land
  "64.61.53.",  # Sugar Land
  "24.162.122.",  # Temple
  "24.119.145.",  # Texarkana
  "66.76.230.",  # Tyler
  "67.216.244.",  # Tyler
  "68.69.62.",  # Tyler
  "24.32.200.",  # Vernon
  "23.123.184.",  # Waco
  "65.65.52.",  # Waco
  "12.94.58.",  # Weatherford
  "66.69.161.",  # Wichita Falls
  "50.56.36.",  # Windcrest
]

# random element from each list


def anonymous_form():
  while True:
    city, county = random.choice(list(cities.items()))
    form_data = {
      'textarea-1': get_tip_body(),
      'text-1': random.choice(info_location),
      'text-6': 'Dr. ' + random.choice(maleFirstNames) + ' ' + random.choice(lastNames),
      'text-2': city,
      'text-3': 'Texas',
      'text-4': str(random.randint(75001, 79942)),
      'text-5': county,
      'hidden-1': random.choice(ips) + str(random.randint(0, 255)),
      'checkbox-1[]': 'no',
    }
    yield form_data


def sign_up_page():
  raise NotImplementedError()


def get_tip_body():
  rv = ''
  # If we have an API key for GPT2, use it
  if args.generate:
    key = DEFAULT_KEY
    if TEXT_GEN_API_VAR in os.environ:
      key = os.environ[TEXT_GEN_API_VAR]
      logger.info('Using key from environment: ' + key)
    else:
      logger.info('Using default key.')
    prompt = random.choice(gpt2_prompts)
    r = requests.post("https://api.deepai.org/api/text-generator", data={
      'text': prompt,
    }, headers={'api-key': key})
    rv = str(r.json()['output'].encode('utf-8'))
    # cut out the prompt, which comes from a limited set and can be filtered on
    rv = rv.replace(prompt, '').lstrip()
    # take string up through last complete sentence since we occasionally get trailing words
    if '.' in rv:
      rv = rv[0:rv.rindex('.')] + '.'
  else:
    # standard tip body generation
    rv = random.choice(gop_members) + ' took their mistress ' + random.choice(firstNames) + ' ' + random.choice(
      lastNames
    ) + ' to get an abortion after their affair.'
  logger.info('Generated text:\n' + rv)
