#%%
from matplotlib.patches import Circle, Rectangle, Arc
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import misc
import urllib, cStringIO
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import LinearSegmentedColormap

def court(ax=None, color='black', lw=4, outer_lines=False,direction='up'):
    '''
    Plots an NBA court
    outer_lines - accepts False or True. Plots the outer side lines of the court.
    direction - 'up' or 'down' depending on how you like to view the court
    Original function from http://savvastjortjoglou.com/
    '''
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        if direction=='up':
            ax = plt.gca(xlim = [-30,30],ylim = [43,-7],xticks=[],yticks=[],aspect=1.0)
            plt.text(22,44,'By: Doingthedishes',color='black',horizontalalignment='center',fontsize=20,fontweight='bold')
        elif direction=='down':
            ax = plt.gca(xlim = [30,-30],ylim = [-7,43],xticks=[],yticks=[],aspect=1.0)
            plt.text(-22,-7,'By: Doingthedishes',color='black',horizontalalignment='center',fontsize=20,fontweight='bold')
        else:
            ax = plt.gca()
    # Create the various parts of an NBA basketball court

    # Create the basketball hoop
    # Diameter of a hoop is 1.5 
    hoop = Circle((0, 0), radius=0.75, linewidth=lw/2, color=color, fill=False)

    # Create backboard
    backboard = Rectangle((-3, -0.75), 6, -0.1, linewidth=lw, color=color)

    # The paint
    # Create the outer box of the paint, width=16ft, height=19ft
    outer_box = Rectangle((-8, -5.25), 16, 19, linewidth=lw, color=color,
                          fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-6, -5.25), 12, 19, linewidth=lw, color=color,
                          fill=False)

    # Create free throw top arc
    top_free_throw = Arc((0, 13.75), 12, 12, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 13.75), 12, 12, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 8, 8, theta1=0, theta2=180, linewidth=lw,
                     color=color)

    # Three point line
    corner_three_a = Rectangle((-22, -5.25), 0, np.sqrt(23.75**2-22.0**2)+5.25, linewidth=lw,
                               color=color)
    corner_three_b = Rectangle((22, -5.25), 0, np.sqrt(23.75**2-22.0**2)+5.25, linewidth=lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    three_arc = Arc((0, 0), 47.5, 47.5, theta1=np.arccos(22/23.75)*180/np.pi, theta2=180.0-np.arccos(22/23.75)*180/np.pi, linewidth=lw,
                    color=color)

    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc]

    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-25, -5.25), 50, 46.75, linewidth=lw,
                                color=color, fill=False)
        center_outer_arc = Arc((0, 41.25), 12, 12, theta1=180, theta2=0,
                                linewidth=lw, color=color)
        center_inner_arc = Arc((0, 41.25), 4, 4, theta1=180, theta2=0,
                                linewidth=lw, color=color)
        court_elements = court_elements + [outer_lines,center_outer_arc,center_inner_arc]
    else:
        plt.plot([-25,25],[-5.25,-5.25],linewidth=lw,color=color)
    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)
#    ax.axis('off')
    return ax

def zones(**kwargs):
    '''
    Plots zones on the court as per NBA.com
    the plot adds to the last plot used or starts a new figure
    '''
    ax = plt.gca()
    zone1 = Arc((0, 0), 16.0, 16.0,theta1 = -41.0,theta2 = 180.0+41.0,**kwargs)
    zone2 = Arc((0, 0), 32.0, 32.0,theta1 = -19.2,theta2 = 180.0+19.2, **kwargs)
    ax.add_patch(zone1)
    ax.add_patch(zone2)
    ang = 60.0
    ax.plot([np.cos(ang/180*np.pi)*8, np.cos(ang/180*np.pi)*16],
             [np.sin(ang/180*np.pi)*8, np.sin(ang/180*np.pi)*16],**kwargs)
    ang = 120.0
    ax.plot([np.cos(ang/180*np.pi)*8, np.cos(ang/180*np.pi)*16],
             [np.sin(ang/180*np.pi)*8, np.sin(ang/180*np.pi)*16],**kwargs)
    ax.plot([22,25],[14-5.25,14-5.25],**kwargs)
    ax.plot([-22,-25],[14-5.25,14-5.25],**kwargs)
    ang = 36.0
    ax.plot([np.cos(ang/180*np.pi)*16, np.cos(ang/180*np.pi)*23.75],
             [np.sin(ang/180*np.pi)*16, np.sin(ang/180*np.pi)*23.75],**kwargs)
    ang = 72.0
    ax.plot([np.cos(ang/180*np.pi)*16, np.cos(ang/180*np.pi)*24],
             [np.sin(ang/180*np.pi)*16, np.sin(ang/180*np.pi)*24],**kwargs)
    ang = 72.0+36.0
    ax.plot([np.cos(ang/180*np.pi)*16, np.cos(ang/180*np.pi)*24],
             [np.sin(ang/180*np.pi)*16, np.sin(ang/180*np.pi)*24],**kwargs)
    ang = 72.0*2
    ax.plot([np.cos(ang/180*np.pi)*16, np.cos(ang/180*np.pi)*23.75],
             [np.sin(ang/180*np.pi)*16, np.sin(ang/180*np.pi)*23.75],**kwargs)
    ang = 72.0
    ax.plot([np.cos(ang/180*np.pi)*24, np.cos(ang/180*np.pi)*41.25],
             [np.sin(ang/180*np.pi)*24, 41.25],**kwargs)
    ang = 72.0+36.0
    ax.plot([np.cos(ang/180*np.pi)*24, np.cos(ang/180*np.pi)*41.25],
             [np.sin(ang/180*np.pi)*24, 41.25],**kwargs)
        
def text_in_zone(string,zone,box_alpha = 0.75,**kwargs):
    '''
    Adds text to zones. 
    Input: 
    string - text to be added
    zone - specify zone (tuple)
    Options:
    box_alpha - string box transparency 
    '''
    if zone == ('Less Than 8 ft.','Center(C)') :
        t = plt.text(0,2,string,horizontalalignment='center',verticalalignment='center',**kwargs)
        t.set_bbox(dict(color='white', alpha=box_alpha))
    elif zone[0] ==  '8-16 ft.':
        if zone[1] == 'Center(C)':
            t = plt.text(0,12,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] == 'Right Side(R)' :
            t = plt.text(12,0,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] == 'Left Side(L)':
            t = plt.text(-12,0,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
    elif zone[0] == '16-24 ft.':
        if zone[1] == 'Center(C)':
            t = plt.text(0,20,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] == 'Right Side(R)':
            t = plt.text(18,7.3,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] ==  'Left Side(L)':
            t = plt.text(-18,7.3,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] == 'Right Side Center(RC)':
            t = plt.text(12,15.5,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] == 'Left Side Center(LC)':
            t = plt.text(-12,15.5,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
    elif zone[0] == '24+ ft.':
        if zone[1] == 'Center(C)':
            t = plt.text(0,28,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] == 'Right Side(R)':
            t = plt.text(27,0,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] == 'Left Side(L)':
            t = plt.text(-27,0,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] == 'Right Side Center(RC)':
            t = plt.text(19,24,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))
        elif zone[1] == 'Left Side Center(LC)':
            t = plt.text(-19,24,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha)) 
    if zone == ('Back Court Shot', 'Back Court(BC)') :
            t = plt.text(0,39,string,horizontalalignment='center',verticalalignment='center',**kwargs)
            t.set_bbox(dict(color='white', alpha=box_alpha))

def players_picture(player_id):
    URL = "http://stats.nba.com/media/players/230x185/%d.png" %player_id
    file = cStringIO.StringIO(urllib.urlopen(URL).read())
    return misc.imread(file)

def grantland_shotchart(shotchart,leagueavergae):
    LA = leagueavergae.loc[:,'SHOT_ZONE_AREA':'FGM'].groupby(['SHOT_ZONE_RANGE','SHOT_ZONE_AREA']).sum()
    LA['FGP'] = 1.0*LA['FGM']/LA['FGA']
    player = shotchart.groupby(['SHOT_ZONE_RANGE','SHOT_ZONE_AREA','SHOT_MADE_FLAG']).size().unstack(fill_value=0)
    player['FGP'] = 1.0*player.loc[:,1]/player.sum(axis=1)
    player_vs_league = (player.loc[:,'FGP'] - LA.loc[:,'FGP'])*100
    x,y = 1.0*shotchart.LOC_X.values/10, 1.0*shotchart.LOC_Y.values/10
    plt.figure(figsize=(15,12.5),facecolor='white')
    ax = court(outer_lines=False)
    ax.axis('off')
    poly_hexbins = plt.hexbin(x,y, gridsize=35, extent=[-25,25,-6.25,50-6.25])
    counts = poly_hexbins.get_array()
    verts = poly_hexbins.get_offsets()
    plt.colorbar()
    plt.close()
    plt.figure(figsize=(14,11.67),facecolor='white') #(0,0.17,0.57)
    ax = plt.gca(xlim = [30,-30],ylim = [-10,40],xticks=[],yticks=[],aspect=1.0)
    plt.text(0,-7,'By: Doingthedishes',color='black',horizontalalignment='center',fontsize=20,fontweight='bold')
    court(ax,outer_lines=False,color='black',lw=4.0,direction='down')
    ax.axis('off')
    #nba.plot.zones()
    #s=0.8747731368853422
    s = 0.85
    bins = np.concatenate([[-np.inf],np.linspace(-9,9,8),[np.inf]])
    colors = [(0.66, 0.75, 0.66),(0.9,1.0,0.6), (0.8, 0, 0)]
    cm = LinearSegmentedColormap.from_list('my_list', colors, N=len(bins)-1)
    xy = s*np.array([np.cos(np.linspace(np.pi/6,np.pi*330/180,6)),np.sin(np.linspace(np.pi/6,np.pi*330/180,6))]).T
    b = np.zeros((6,2))
    counts_norm = np.zeros_like(counts)
    counts_norm[counts>=5] = 1
    counts_norm[(counts>=2) & (counts<5)] = 0.5
    counts_norm[(counts>=1) & (counts<2)] = 0.3
    patches=[]
    colors=[]
    for offc in xrange(verts.shape[0]):
        if counts_norm[offc] != 0:
            xc,yc = verts[offc][0],verts[offc][1] 
            b[:,0] = xy[:,0]*counts_norm[offc] + xc
            b[:,1] = xy[:,1]*counts_norm[offc] + yc
            p_diff = player_vs_league.loc[shot_zone(xc,yc)]
            inds = np.digitize(p_diff, bins,right=True)-1
            patches.append(Polygon(b))
            colors.append(inds)
          
    for i in range(len(bins)-1):
        xc = 23-2*0.76*i
        yc = -7
        b[:,0] = xy[:,0] + xc
        b[:,1] = xy[:,1] + yc
        patches.append(Polygon(b))
        colors.append(i)
    plt.text(23,-8.5,'Cold',horizontalalignment='center',verticalalignment='center')
    plt.text(23-2*0.76*(len(bins)-2),-8.5,'Hot',horizontalalignment='center',verticalalignment='center')
    
    xc = -14.5
    yc = -7.0
    plt.text(xc,-8.5,'Less',horizontalalignment='center',verticalalignment='center')
    b[:,0] = xy[:,0]*0.3 + xc
    b[:,1] = xy[:,1]*0.3 + yc
    patches.append(Polygon(b))
    colors.append(2)
    xc = -16
    b[:,0] = xy[:,0]*0.60 + xc
    b[:,1] = xy[:,1]*0.60 + yc
    patches.append(Polygon(b))
    colors.append(2)
    xc = -18
    b[:,0] = xy[:,0] + xc
    b[:,1] = xy[:,1] + yc
    plt.text(xc,-8.5,'More',horizontalalignment='center',verticalalignment='center')
    
    patches.append(Polygon(b))
    colors.append(2)
    p = PatchCollection(patches,cmap=cm,alpha=1)
    p.set_array(np.array(colors))
    ax.add_collection(p)
    p.set_clim([0, len(bins)-1])
    
    pic = players_picture(shotchart.loc[0,'PLAYER_ID'])
    plt.imshow(pic,extent=[15,25,30,37.8261])
    plt.text(20,29,shotchart.loc[0,'PLAYER_NAME'],fontsize=16,horizontalalignment='center',verticalalignment='center')
    
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
