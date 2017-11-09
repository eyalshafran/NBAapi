import requests
import pandas as pd

def gamelog(counter = 1000,datefrom='',dateto='',direction='DESC',leagueid='00',
            playerorteam='T',season='2015-16',seasontype='Regular Season',sorter='PTS'):   
    url = 'http://stats.nba.com/stats/leaguegamelog?'
    api_param = {
        'Counter' : counter,
        'DateFrom' :  datefrom,
        'DateTo' : dateto,
        'Direction' : direction,
        'LeagueID' : leagueid,
        'PlayerOrTeam' : playerorteam,
        'Season' : season,
        'SeasonType' : seasontype,
        'Sorter' : sorter,              
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    
def hustlestatsteam(College='',Conference='',Country='',DateFrom='',DateTo='',Division='',DraftPick='',
                    DraftYear='',GameScope='',GameSegment='',Height='',LastNGames='0',LeagueID='00',
                    Location='',Month='0',OpponentTeamID='0',Outcome='',PORound='0',PaceAdjust='N',
                    PerMode='PerGame',Period='0',PlayerExperience='',PlayerPosition='',PlusMinus='N',
                    Rank='N',Season='2016-17',SeasonSegment='',SeasonType='Regular Season',ShotClockRange='',
                    TeamID='0',VsConference='',VsDivision='',Weight=''):
                              
    url = 'http://stats.nba.com/stats/leaguehustlestatsteam?'
    api_param = {
        'College' : College,
        'Conference' : Conference,
        'Country' : Country,
        'DateFrom' : DateFrom,
        'DateTo' : DateTo,
        'Division' : Division,
        'DraftPick' : DraftPick,
        'DraftYear' : DraftYear,
        'GameScope' : GameScope,
        'GameSegment' : GameSegment,
        'Height' : Height,
        'LastNGames' : LastNGames,
        'LeagueID' : LeagueID,
        'Location' : Location,
        'Month' : Month,
        'OpponentTeamID' : OpponentTeamID,
        'Outcome' : Outcome,
        'PORound' : PORound,
        'PaceAdjust' : PaceAdjust,
        'PerMode' : PerMode,
        'Period' : Period,
        'PlayerExperience' : PlayerExperience,
        'PlayerPosition' : PlayerPosition,
        'PlusMinus' : PlusMinus,
        'Rank' : Rank,
        'Season' : Season,
        'SeasonSegment' : SeasonSegment,
        'SeasonType' : SeasonType,
        'ShotClockRange' : ShotClockRange,
        'TeamID' : TeamID,
        'VsConference' : VsConference,
        'VsDivision' : VsDivision,
        'Weight' : Weight
        }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a},timeout=1.0)
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    
def playbyplayv2(gameid,startperiod=0,endperiod=0):
    url = 'http://stats.nba.com/stats/playbyplayv2?'
    api_param = {
        'StartPeriod' : startperiod,
        'EndPeriod' : endperiod, 
        'GameID' : gameid,           
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a},timeout=1.0)
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])