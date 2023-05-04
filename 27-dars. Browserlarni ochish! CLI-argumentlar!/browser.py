import argparse
import webbrowser
import time

parser = argparse.ArgumentParser(description="URL opener: ")

parser.add_argument("--url", type=str, help="URL ni kiriting: ")
parser.add_argument("--open", type=int, help="Ushbu URL necha marta ochilsin?")
parser.add_argument("--sleep",type=int, required=False, help="Har bir sahifa ochilishini necha sekund kutib tursin!")
args = parser.parse_args()
webbrowser.open(args.url)

def open_web_browser(url, open, sleep=1):
    for i in range(open - 1):
        webbrowser.open(url)
        time.sleep(sleep)

if args.sleep == None:
    open_web_browser(args.url, args.open)
else:
    open_web_browser(args.url, args.open, args.sleep)

# ishlatish! python browser.py --url https://youtube.com --open 5 --sleep 3