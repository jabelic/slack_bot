#https://se.miyabikno-jobs.com/python-schedule-library/


from slacker import Slacker
import bs
import schedule
import time
import os

def settings():
    return Slacker(os.environ['SLACK_API_KEY'])

def detection_str():
    string = bs.weather()
    if "雨" in string:
        return True
    else:
        return False


def notice():
    slack = settings()
    if detection_str():
        slack.chat.post_message('#weather', "@here  雨が降るかもしれないよ！傘を忘れずに！", link_names=1)
    else:
        slack.chat.post_message('#weather', "@here  雨降らないよ！！", link_names=1)

def main():
    schedule.every().day.at("07:30").do(notice)
    while True:
        schedule.run_pending()
        time.sleep(1)         #1sec スリープ

if __name__=="__main__":
    print("starting bot")
    main()



