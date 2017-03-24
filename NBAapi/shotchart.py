import requests
import pandas as pd
import numpy as np

def shotchartdetail(leagueid='00',season='2016-17',seasontype='Regular Season',teamid=0,
                    playerid=0,gameid='',outcome='',location='',month=0,
                    seasonseg='',datefrom='',dateto='',oppteamid=0,vsconf='',
                    vsdiv='',pos='',gameseg='',per=0,lastngames=0,aheadbehind='',
                    contextmeasure='FGM',clutchtime='',rookieyear=''):
    url = 'http://stats.nba.com/stats/shotchartdetail?'
    api_param = {
         'LeagueID': leagueid,
         'Season' :  season,
         'SeasonType' : seasontype,
         'TeamID' : teamid,
         'PlayerID' : playerid,
         'GameID' : gameid,
         'Outcome' : outcome,
         'Location' : location,
         'Month' : month,
         'SeasonSegment' : seasonseg,
         'DateFrom' :  datefrom,
         'DateTo' : dateto,
         'OpponentTeamID' : oppteamid,
         'VsConference' : vsconf,
         'VsDivision' : vsdiv,
         'PlayerPosition' : pos,
         'GameSegment' : gameseg,
         'Period' :  per,
         'LastNGames' : lastngames,
         'AheadBehind' : aheadbehind,
         'ContextMeasure' : contextmeasure,
         'ClutchTime' : clutchtime,
         'RookieYear' : rookieyear
         }
    u_a = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36"
    response = requests.get(url,params=api_param,headers={"USER-AGENT":u_a})
    data = response.json()
    Shot_Chart_Detail = pd.DataFrame(data['resultSets'][0]['rowSet'],columns=data['resultSets'][0]['headers'])
    LeagueAverage = pd.DataFrame(data['resultSets'][1]['rowSet'],columns=data['resultSets'][1]['headers'])
    return Shot_Chart_Detail,LeagueAverage
    
def shot_zone(X,Y):
    '''
    Uses shot coordinates x and y (in feet - divide by 10 if using the shotchart units)
    and returns a tuple with the zone location
    '''
    r = np.sqrt(X**2+Y**2)
    a = np.arctan2(Y,X)*180.0/np.pi
    if (Y<0) & (X > 0):
        a = 0
    elif (Y<0) & (X < 0):
        a = 180
    if r<=8:
        z = ('Less Than 8 ft.','Center(C)')
    elif (r>8) & (r<=16):
        if a < 60:
            z = ('8-16 ft.','Right Side(R)')
        elif (a>=60) & (a<=120):
            z = ('8-16 ft.','Center(C)')
        else:
            z = ('8-16 ft.','Left Side(L)')
    elif (r>16) & (r<=23.75):
        if a < 36:
            z = ('16-24 ft.','Right Side(R)')
        elif (a>=36) & (a<72):
            z = ('16-24 ft.','Right Side Center(RC)')
        elif (a>=72) & (a<=108):
            z = ('16-24 ft.','Center(C)')
        elif (a>108) & (a<144):
            z = ('16-24 ft.','Left Side Center(LC)')
        else:
            z = ('16-24 ft.','Left Side(L)')
    elif r>23.75:
        if a < 72:
            z = ('24+ ft.','Right Side Center(RC)')
        elif (a>=72) & (a<=108):
            z = ('24+ ft.','Center(C)')
        else:
            z = ('24+ ft.','Left Side Center(LC)')
    if (np.abs(X)>=22):
        if (X > 0) & (np.abs(Y)<8.75):
            z = ('24+ ft.','Right Side(R)')
        elif (X < 0) & (np.abs(Y)<8.75):
            z = ('24+ ft.','Left Side(L)')
        elif (X > 0) & (np.abs(Y)>=8.75):
            z = ('24+ ft.','Right Side Center(RC)')
        elif (X < 0) & (np.abs(Y)>=8.75):
            z = ('24+ ft.','Left Side Center(LC)')
    if Y >= 40:
        z = ('Back Court Shot', 'Back Court(BC)')
    return z