import requests
import pandas as pd

def stats(conference='',datefrom='',dateto='',div='',gamescope='',gamesegment='',lastngames=0,
          leagueid='00',location='',measuretype='Base',month=0,oppenentteamid=0,outcome='',
          poround=0,paceadjust='N',permode='PerGame',period=0,playerexperience='',
          playerposition='',plusminus='N',rank='N',
          season='2015-16',seasonsegment='',seasontype='Regular Season',shotclockrange='',
          starterbench='',teamid=0,vsconference='',vsdivision=''):
    url = 'http://stats.nba.com/stats/leaguedashteamstats?'
    api_param = {
        'Conference' :conference,
        'DateFrom' :  datefrom,
        'DateTo' : dateto,
        'Division' : div,
        'GameScope' : gamescope,
        'GameSegment' : gamesegment,
        'LastNGames' : lastngames,
        'LeagueID' : leagueid,
        'Location' : location,
        'MeasureType' : measuretype,
        'Month' : month,
        'OpponentTeamID' : oppenentteamid,
        'Outcome' : outcome,
        'PORound' : poround,
        'PaceAdjust' : paceadjust,
        'PerMode' : permode,
        'Period' : period,
        'PlayerExperience' : playerexperience,
        'PlayerPosition' : playerposition,
        'PlusMinus' : plusminus,
        'Rank' : rank,
        'Season' : season,
        'SeasonSegment' : seasonsegment,
        'SeasonType' : seasontype,
        'ShotClockRange' : shotclockrange,
        'StarterBench' : starterbench,
        'TeamID' : teamid,
        'VsConference': vsconference,
        'VsDivision' : vsdivision              
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    
def gamelog(teamid,seasontype='Regular Season',leagueid='00',season='2016-17'):
    url = 'http://stats.nba.com/stats/teamgamelog?'
    api_param = {
        'SeasonType' : seasontype,
        'LeagueID' : leagueid,
        'Season' : season,
        'teamID' : teamid,              
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    

def commonteamyears(leagueid='00'):   
    url = 'http://stats.nba.com/stats/commonteamyears?'
    api_param = {
        'LeagueID' : leagueid,            
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])

def roster(teamid,season='2016-17',leagueid='00'):
    url = 'http://stats.nba.com/stats/commonteamroster?'
    api_param = {
        'LeagueID' : leagueid,
        'Season' : season,
        'teamID' : teamid,              
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])    
    
    

    