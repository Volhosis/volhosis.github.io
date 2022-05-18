import sys, requests, re

def get_logs(username):
    logs = ''
    res = requests.get(f"https://typeracerdata.com/text.analysis?username={username}").text
    gameRegex = re.compile(r'game=(\d+)\"')
    games = gameRegex.findall(res)
    for index, game in enumerate(games):
        res2 = requests.get(f"https://data.typeracer.com/pit/result?id=|tr:{username}|" + game).text
        logRegex = re.compile(r'TLv\d,.+,.+,(.+)\|')
        try:
            log += logRegex.search(res2).group(1)
        except:
            continue
        print(f"{index + 1} / {len(games)}")
    return logs

def analyze(logs):
    pass

if(len(sys.argv) == 2):
    username = sys.argv[1]
    logs = get_logs(username)
    analyze(logs)


else:
    print("Please use the format: getCharSpeeds.py [username]")


