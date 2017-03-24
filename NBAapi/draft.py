import requests
import pandas as pd

def drafthistory(college='',leagueid='00',overallpick='',roundnum='',roundpick='',
                 season='',teamid=0,topx=''):
    url = 'http://stats.nba.com/stats/drafthistory?'
    api_param = {
        'College' : college,
        'LeagueID' : leagueid,
        'OverallPick' : overallpick,
        'RoundNum' : roundnum,
        'RoundPick' : roundpick,
        'Season' : season,
        'TeamID' : teamid,
        'TopX' : topx
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])