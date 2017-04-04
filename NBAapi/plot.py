#%%
from matplotlib.patches import Circle, Rectangle, Arc
import matplotlib.pyplot as plt
import numpy as np

def court(ax=None, color='black', lw=4, outer_lines=False,direction='up'):
    '''
    Plots an NBA court
    outer_lines - accepts False or True. Plots the outer side lines of the court.
    Original function from http://savvastjortjoglou.com/
    '''
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        if direction=='up':
            ax = plt.gca(xlim = [-30,30],ylim = [43,-7],xticks=[],yticks=[],aspect=1.0)
            plt.text(22,44,'By: Doingthedishes',color='blue',horizontalalignment='center',fontsize=20)
        elif direction=='down':
            ax = plt.gca(xlim = [30,-30],ylim = [-7,43],xticks=[],yticks=[],aspect=1.0)
            plt.text(-22,-7,'By: Doingthedishes',color='blue',horizontalalignment='center',fontsize=20)
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
    the plot add to the last plot used or starts a new figure
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

