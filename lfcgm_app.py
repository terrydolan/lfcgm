# LFC Goal Machine App
# author: Terry Dolan, @lfcsorted
#
from spyre import server
import os
import pandas as pd
from ggplot import *

# create list of players for dropdown
LT = "&#060" # HTML escape character for '<'
GT = "&#062" # HTML escape character for '>'
LFCGM_DROPDOWN = os.path.relpath('data/lfcgm_app_dropdown.csv')
dd_options_list = [{"label": LT+"Select Player"+GT, "value": "Empty"}]
dd_options_list.extend(pd.read_csv(LFCGM_DROPDOWN).to_dict(orient='records'))

class LFCGoalMachine(server.App):
    """Spyre LFC Goal Machine App."""
    title = "The LFC Goal Machine"

    inputs = [{"type": 'dropdown',
               "label": 'Select LFC players from dropdown lists', 
               "options" : dd_options_list,
               "key": 'selected_p1',
               "action_id": "update_data"},
              
              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": 'selected_p2',
               "action_id": "update_data"},
              
              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": 'selected_p3',
               "action_id": "update_data"},
              
              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": 'selected_p4',
               "action_id": "update_data"},
              
              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": 'selected_p5',
               "action_id": "update_data"},

              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": 'selected_p6',
               "action_id": "update_data"},

              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": 'selected_p7',
               "action_id": "update_data"},
              
              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": 'selected_p8',
               "action_id": "update_data"},

              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": 'selected_p9',
               "action_id": "update_data"},
              
              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": 'selected_p10',
               "action_id": "update_data"}]

    controls = [{"type": "hidden",
                "id": "update_data"}]

    tabs = ["Plot", "About"]

    outputs = [{"type": "plot",
                "id": "plot_id",
                "control_id": "update_data",
                "tab": "Plot"},
               {"type" : "html",
                "id" : "simple_html_output",
                "control_id" : "update_data",
                "tab" : "About"}]

    def __init__(self):
        """Load pandas dataframe of lfc scorers.

           For example, the dataframe contains:
           | season    | player         | league | position   | age  |
           | 2014-2015 | Steven Gerrard | 9      | Midfielder | 34.6 |

           league is the number of league goals by player in season
           age is the player's age at the season midpoint.

           Data source: www.lfchistory.com."""
        LFCGM_DATA = os.path.relpath('data/lfc_scorers_tl_pos_age.csv')
        self.df = pd.DataFrame.from_csv(LFCGM_DATA, sep=',')

    def ggplot_age_vs_lgoals(self, df, players):
        """Return ggplot of Age vs League Goals for given list of players in dataframe.

           Given the low number of points, ggplot's geom_smooth uses
           the loess method with default span."""

        TITLE = 'Age vs League Goals'
        XLABEL = 'Age at Midpoint of Season'
        YLABEL = 'League Goals per Season'
        EXEMPLAR_PLAYERS = ['Robbie Fowler', 'Ian Rush', 'Roger Hunt', \
                            'John Aldridge', 'Luis Suarez', 'Fernando Torres']
        EXEMPLAR_TITLE = 'Example Plot: ' + TITLE
        
        # if all the selected players are 'Empty' then set the default exemplar options
        if all(p == 'Empty' for p in players):
            players = EXEMPLAR_PLAYERS
            TITLE = EXEMPLAR_TITLE
            
        # fiter dataframe for given players and plot
        this_df = df[df.player.isin(players)]
        this_plot = ggplot(this_df, aes(x='age', y='league', color='player', shape='player')) + \
                        geom_point() + \
                        geom_smooth(se=False) + \
                        xlab(XLABEL) + \
                        ylab(YLABEL) + \
                        scale_y_discrete(limits=(0, this_df.league.max() + 1)) + \
                        ggtitle(TITLE)
        return this_plot

    def getPlot(self, params):
        """Return the plot object."""
        print '\n', '-'*60, '\n', params, '\n', '-'*60

        players = [params['selected_p1'], params['selected_p2'], params['selected_p3'], \
                   params['selected_p4'], params['selected_p5'], params['selected_p6'], \
                   params['selected_p7'], params['selected_p8'], params['selected_p9'], \
                   params['selected_p10']]

        # plot the selected players
        ggplt = self.ggplot_age_vs_lgoals(self.df, players)

        # Spyre (v0.2) cannot handle a ggplot object so
        # return a matplotlib (matplotlib.figure.Figure) object
        return ggplt.draw()

    def getHTML(self,params):
        """Return html that describes the app."""
        
        html = """
        <!DOCTYPE html>
        <html>
        <body>

        <p>LFC Goal Machine app by @lfcsorted, your feedback is welcome.</p>
        <a href="https://twitter.com/lfcsorted" class="twitter-follow-button" data-show-count="false">Follow @lfcsorted</a>
        <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)
        ?'http':'https';if(!d.getElementById(id))
        {js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}
        (document, 'script', 'twitter-wjs');</script>
        <br>
        
        <p>The app takes the selected LFC player and plots the
        player's Age against League Goals per season.
        You can generate your own plots simply by selecting 1 or more players
        from the dropdown list on the Plot tab.
        You can compare players across any era. Enjoy :-).</p>
        
        <p>
        The player dropdown list contains all of the LFC players who
        have scored 1 or more top level league goals in 2 or more seasons
        from 1894-1895 to 2014-15. 
        The top level is the old 1st Division or the Premier League. That's 233
        LFC players, from Alan A'Court to Yossi Benayoun.
        The player's age used in the plots is their age at the season mid-point,
        taken to be 1st January.
        </p>

        <p>Special thanks to @lfchistory for the base LFC data.</p>

        <p>The app uses python, spyre, pandas, ggplot and heroku.
        For more information on the data analysis, the app source code, and
        how it is deployed see Terry Dolan's
        <a href="https://github.com/terrydolan/lfcgm">lfcgm github repository</a>.
        The summary line for each player is a smoothed conditional mean
        using ggplot's geom_smooth.
        Given the small number of data points for each player, this uses
        a loess method with a default span.</p>

        <p>Terry Dolan<br>
        February 2016</p>
        
        </body>
        </html>
        """
        return html

if __name__ == '__main__':
    app = LFCGoalMachine()
    app.launch(host='0.0.0.0', port=int(os.environ.get('PORT', '5000')))
