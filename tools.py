import re,os
from urllib.parse import parse_qs, urlparse
os.system('pip3 install -r requirements.txt')
os.system('pip install -r requirements.txt')

import requests
#from selenium import __version__


def check_url_patterns(url):
    patterns = [
        r"ww\.mirrobox\.com",
        r"www\.nephobox\.com",
        r"freeterabox\.com",
        r"www\.freeterabox\.com",
        r"1024tera\.com",
        r"4funbox\.co",
        r"www\.4funbox\.com",
        r"mirrobox\.com",
        r"nephobox\.com",
        r"terabox\.app",
        r"terabox\.com",
        r"www\.terabox\.ap",
        r"www\.terabox\.com",
        r"www\.1024tera\.co",
        r"www\.momerybox\.com",
        r"teraboxapp\.com",
        r"momerybox\.com",
        r"tibibox\.com",
        r"www\.tibibox\.com",
        r"www\.teraboxapp\.com",
    ]

    for pattern in patterns:
        if re.search(pattern, url):
            return True

    return False


def get_formatted_size(size_bytes):
    if size_bytes >= 1024 * 1024:
        size = size_bytes / (1024 * 1024)
        unit = "MB"
    elif size_bytes >= 1024:
        size = size_bytes / 1024
        unit = "KB"
    else:
        size = size_bytes
        unit = "b"

    return f"{size:.2f} {unit}"


def get_urls_from_string(string):
    pattern = r"(https?://\S+)"
    urls = re.findall(pattern, string)
    urls = [url for url in urls if check_url_patterns(url)]
    if not urls:
        return
    return urls[0]


def find_between(data, first, last):
    try:
        start = data.index(first) + len(first)
        end = data.index(last, start)
        return data[start:end]
    except ValueError:
        return None


def extract_surl_from_url(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    surl = query_params.get("surl", [])

    if surl:
        return surl[0]
    else:
        return False


def get_data(url: str):
    r = requests.Session()
    headersList = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "PANWEB=1; csrfToken=zcB-8zYpUSuGJYARruP6ciKa; lang=en; TSID=UG8Ux11m0tQJhha2h6AYF6HoRuElxvMU; __bid_n=18c0b12d393d1a88c44207; _ga=GA1.1.534448201.1700992834; __stripe_mid=63de2b36-0aa9-48d3-b049-d92a35378933041de1; ndus=Y-R0se7teHuivLrNA0f1oAiHAzBWcLRCIovVHKTb; browserid=cP5XWdCGKn9XXeBSULS9_aCyY3XzUgKTIo5xMGHMbeYH3WJwFiJvauWfTg8=; ndut_fmt=F4EF2C82459DE488D18B2AE1F9BEB77918DDBF7C7AF722B5E9D086A42352A286; _ga_06ZNKL8C2E=GS1.1.1706342076.15.1.1706343527.60.0.0",
        "DNT": "1",
        "Host": "www.terabox.app",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    payload = ""

    response = r.get(url, data=payload, headers=headersList)
    response = r.get(response.url, data=payload, headers=headersList)
    logid = find_between(response.text, "dp-logid=", "&")
    jsToken = find_between(response.text, "fn%28%22", "%22%29")
    bdstoken = find_between(response.text, 'bdstoken":"', '"')
    shorturl = extract_surl_from_url(response.url)
    if not shorturl:
        return False

    reqUrl = f"https://www.terabox.app/share/list?app_id=250528&web=1&channel=0&jsToken={jsToken}&dp-logid={logid}&page=1&num=20&by=name&order=asc&site_referer=&shorturl={extract_surl_from_url(response.url)}&root=1"

    headersList = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9,hi;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "PANWEB=1; csrfToken=zcB-8zYpUSuGJYARruP6ciKa; lang=en; TSID=UG8Ux11m0tQJhha2h6AYF6HoRuElxvMU; __bid_n=18c0b12d393d1a88c44207; _ga=GA1.1.534448201.1700992834; __stripe_mid=63de2b36-0aa9-48d3-b049-d92a35378933041de1; ndus=Y-R0se7teHuivLrNA0f1oAiHAzBWcLRCIovVHKTb; browserid=cP5XWdCGKn9XXeBSULS9_aCyY3XzUgKTIo5xMGHMbeYH3WJwFiJvauWfTg8=; ndut_fmt=F4EF2C82459DE488D18B2AE1F9BEB77918DDBF7C7AF722B5E9D086A42352A286; _ga_06ZNKL8C2E=GS1.1.1706342076.15.1.1706343527.60.0.0",
        "DNT": "1",
        "Host": "www.terabox.app",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
        "sec-ch-ua": '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
    }

    payload = ""

    response = r.get(reqUrl, data=payload, headers=headersList)

    if not response.status_code == 200:
        return False
    r_j = response.json()
    if r_j["errno"]:
        return False
    if not "list" in r_j and not r_j["list"]:
        return False

    response = r.head(r_j["list"][0]["dlink"], headers=headersList)
    direct_link = response.headers.get("location")
    data = {
        "file_name": r_j["list"][0]["server_filename"],
        "link": r_j["list"][0]["dlink"],
        "direct_link": direct_link,
        "thumb": r_j["list"][0]["thumbs"]["url3"],
        "size": get_formatted_size(int(r_j["list"][0]["size"])),
        "sizebytes": int(r_j["list"][0]["size"]),
    }
    return data

import wget
import asyncio
from pyrogram import Client,filters
import random
import os
from telebot.custom_filters import TextFilter, TextMatchFilter
import telebot
auth='6445662081:AAHn8AEGXU6YsBJeDDNpUrGlWtD8ERA5LTI'
bot = telebot.TeleBot(auth) 
# creating a instance
@bot.message_handler(commands=["start"])
def strt(message):
    bot.reply_to(message, 'starting bot THIS IS TERABOX DOWNLOADER BOT SEND LINK to know usage')

  
@bot.message_handler(text=TextFilter(contains=['tera']))
def linkx(message):
    global a
    a=get_data(message.text)

    print(type(a))

    siz=a.get('size')
    file=a.get('file_name')
    bot.reply_to(message,f'Downloading->{file} \n size -> {siz}')
    mid=message.chat.id
    #print(a[link])
    filedown=wget.download(a.get('link'), out=file)
    bot.reply_to(message,'uploading the video sending u wait !!')
    os.system('telegram-upload --to t.me/leech_mega_channel {filedown}')


bot.add_custom_filter(TextMatchFilter())
bot.infinity_polling()
