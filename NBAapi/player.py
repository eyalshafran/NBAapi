import requests
import pandas as pd

def stats(college='',conference='',country='',datefrom='',dateto='',division='',          
          draftpick='',draftyear='',gamescope='',gamesegment='',height='',
          lastngames=0,leagueid='00',location='',measuretype='Base',month=0,
          opponentteamid=0,outcome='',poround=0,paceadjust='N',permode='Totals',
          period=0,playerexperience='',playerposition='',plusminus='N',rank='N',
          season='2016-17',seasonsegment='',seasontype='Regular Season',shotclockrange='',
          starterbench='',teamid=0,vsconference='',vsdivision='',weight=''):
    url = 'http://stats.nba.com/stats/leaguedashplayerstats?'
    api_param = {
        'College' : college,
        'Conference' : conference,
        'Country' : country,
        'DateFrom' : datefrom,
        'DateTo' : dateto,
        'Division' : division,
        'DraftPick' : draftpick,
        'DraftYear' : draftyear,
        'GameScope' : gamescope,
        'GameSegment' : gamesegment,
        'Height' : height,
        'LastNGames' : lastngames,
        'LeagueID' : leagueid,
        'Location' : location,
        'MeasureType' : measuretype,
        'Month' : month,
        'OpponentTeamID' : opponentteamid,
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
        'VsConference' : vsconference,
        'VsDivision' : vsdivision,
        'Weight' : weight,
        }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    
def biostats(college='', conference='', country='', datefrom='', dateto='', division='',
             draftpick='', draftyear='', gamescope='', gamesegment='', height='',
             lastngames=0, leagueid='00', location='', month=0, opponentteamid=0,
             outcome='', poround=0, permode='PerGame', period=0, playerexperience='',
             playerposition='', season='2015-16', seasonsegment='',
             seasontype='Regular Season', shotclockrange='', starterbench='', teamid=0,
             vsconference='', vsdivision='', weight=''):
    url = 'http://stats.nba.com/stats/leaguedashplayerbiostats?'
    api_param = {
         'College': college,
         'Conference' :  conference,
         'Country' : country,
         'DateFrom' : datefrom,
         'DateTo' : dateto,
         'Division' : division,
         'DraftPick' : draftpick,
         'DraftYear' : draftyear,
         'GameScope' : gamescope,
         'GameSegment' : gamesegment,
         'Height' :  height,
         'LastNGames' : lastngames,
         'LeagueID' : leagueid,
         'Location' : location,
         'Month' : month,
         'OpponentTeamID' : opponentteamid,
         'Outcome' : outcome,
         'PORound' :  poround,
         'PerMode' : permode,
         'Period' : period,
         'PlayerExperience' : playerexperience,
         'PlayerPosition' : playerposition,
         'Season' : season,
         'SeasonSegment' : seasonsegment,
         'SeasonType' : seasontype,
         'ShotClockRange' : shotclockrange,
         'StarterBench' : starterbench, 
         'TeamID' : teamid,
         'VsConference' : vsconference,
         'VsDivision' : vsdivision,
         'Weight' : weight,
         }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    
def commonallplayers(currentseason=0,leagueid='00',season='2015-16'):
    url = 'http://stats.nba.com/stats/commonallplayers?'
    api_param = {
        'IsOnlyCurrentSeason' : currentseason,
        'LeagueID' : leagueid,
        'Season' : season,             
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    
def careerstats(playerid,permode='PerGame',leagueid='00'):
    url = 'http://stats.nba.com/stats/playercareerstats?'
    api_param = {
        'PerMode' : permode,
        'LeagueID' : leagueid,
        'PlayerID' : playerid,             
    }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    
def gamelog(playerid,DateFrom='',DateTo='',LeagueID='00',Season='2016-17',SeasonType='Regular Season'):
    url = 'http://stats.nba.com/stats/playergamelog?'
    api_param = {
        'DateFrom' : DateFrom,
        'DateTo' : DateTo,
        'LeagueID' : LeagueID,
        'PlayerID' : playerid,
        'Season' : Season,
        'SeasonType' : SeasonType,
        }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    
def dashptreb(playerid,DateFrom='',DateTo='',GameSegment='',LastNGames='0',LeagueID='00',Location='',Month='0',
              OpponentTeamID='0',Outcome='',PORound='0',PerMode='PerGame',Period='0',
              Season='2016-17',SeasonSegment='',SeasonType='Regular Season',TeamID='0',VsConference='',
              VsDivision=''):
    url = 'http://stats.nba.com/stats/playerdashptreb?'
    api_param = {
        'DateFrom' : DateFrom,
        'DateTo' : DateTo,
        'GameSegment' : GameSegment,
        'LastNGames' : LastNGames,
        'LeagueID' : LeagueID,
        'Location' : Location,
        'Month' : Month,
        'OpponentTeamID' : OpponentTeamID,
        'Outcome' : Outcome,
        'PORound' : PORound,
        'PerMode' : PerMode,
        'Period' : Period,
        'PlayerID' : playerid,
        'Season' : Season,
        'SeasonSegment' : SeasonSegment,
        'SeasonType' : SeasonType,
        'TeamID' : TeamID,
        'VsConference' : VsConference,
        'VsDivision' : VsDivision,
        }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    
def hustlestatsplayer(College='',Conference='',Country='',DateFrom='',DateTo='',
                      Division='',DraftPick='',DraftYear='',GameScope='',Height='',
                      LastNGames='0',LeagueID='00',Location='',Month='0',
                      OpponentTeamID='0',Outcome='',PORound='0',PaceAdjust='N',
                      PerMode='PerGame',PlayerExperience='',PlayerPosition='',
                      PlusMinus='N',Rank='N',Season='2016-17',SeasonSegment='',
                      SeasonType='Regular Season',TeamID='0',VsConference='',
                      VsDivision='',Weight=''):
    url = 'http://stats.nba.com/stats/leaguehustlestatsplayer?'
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
        'PlayerExperience' : PlayerExperience,
        'PlayerPosition' : PlayerPosition,
        'PlusMinus' : PlusMinus,
        'Rank' : Rank,
        'Season' : Season,
        'SeasonSegment' : SeasonSegment,
        'SeasonType' : SeasonType,
        'TeamID' : TeamID,
        'VsConference' : VsConference,
        'VsDivision' : VsDivision,
        'Weight' : Weight,
        }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    return pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])

