"""LFC Goal Machine App.

An interactive python Spyre web app that uses ggplot to
plots an LFC player's age against the goals that the player
scored in a top level season.

Example:
    $python lfcgm_app.py
    
"""
from spyre import server
import os
import pandas as pd
from ggplot import *
import logging
import logging.config
import lfcgm_log_config # dict with logging config

__author__ = "Terry Dolan"
__copyright__ = "Terry Dolan"
__license__ = "MIT"
__version__ = "1.0.0"
__email__ = "terry8dolan@gmail.com"
__status__ = "Prototype"

# set up logging
logging.config.dictConfig(lfcgm_log_config.dictLogConfig)
logger = logging.getLogger('lfcgm')

# create list of players for Spyre dropdown
LT = "&#060" # HTML escape character for '<'
GT = "&#062" # HTML escape character for '>'
LFCGM_DROPDOWN = os.path.relpath('data/lfcgm_app_dropdown.csv')
dd_options_list = [{"label": LT+"Select Player"+GT, "value": "Empty"}]
dd_options_list.extend(pd.read_csv(LFCGM_DROPDOWN).to_dict(orient='records'))

# set number of dropdowns
DD_NUMBER = 8

# create list of keys for Spyre dropdown
# key is set to 'selected_pn' where n is dropdown number
DD_KEY_LIST = ['selected_p{}'.format(i) for i in range(1, DD_NUMBER+1)]

# create label for first dropdown
DD_FIRST_LABEL = 'Select LFC players from dropdown lists'


class LFCGoalMachine(server.App):
    """Spyre LFC Goal Machine App."""
    title = "The LFC Goal Machine"

    # create list of inputs for Spyre dropdown
    # the first dropown has a label, the others do not
    inputs = [{"type": 'dropdown',
               "label": DD_FIRST_LABEL,
               "options" : dd_options_list,
               "key": kstr,
               "action_id": "update_data"} if kstr == 'selected_p1' 
                                           else 
              {"type": 'dropdown',
               "options" : dd_options_list,
               "key": kstr,
               "action_id": "update_data"} for kstr in DD_KEY_LIST]

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
        logger.info("LFCGoalMachine.init, creating dataframe from: {}".format(LFCGM_DATA))
        self.df = pd.DataFrame.from_csv(LFCGM_DATA, sep=',')

    def ggplot_age_vs_lgoals(self, df, players):
        """Return ggplot of Age vs League Goals for given list of players in dataframe.

           Given the low number of points, ggplot's geom_smooth uses
           the loess method with default span."""
        TITLE = 'LFCGM Age vs League Goals'
        XLABEL = 'Age at Midpoint of Season'
        YLABEL = 'League Goals per Season'
        EXEMPLAR_PLAYERS = ['Ian Rush', 'Kenny Dalglish', 'Roger Hunt', 'David Johnson',
                            'Harry Chambers', 'John Toshack', 'John Barnes', 'Kevin Keegan']
        EXEMPLAR_TITLE = 'LFCGM Example Plot, The Champions: Age vs League Goals'
        
        # if players list is empty then set the default exemplar options
        if not players:
            logger.info('LFCGoalMachine.ggplot_age_vs_lgoals, players list empty so setting default')
            players = EXEMPLAR_PLAYERS
            TITLE = EXEMPLAR_TITLE
            
        # fiter dataframe for given players and plot
        logger.info('LFCGoalMachine.ggplot_age_vs_lgoals, creating ggplot for: {}'.format(players))
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
        # set players to the values from the dropdowns, filtering out 'Empty' selections
        players = [str(params[keystr]) for keystr in DD_KEY_LIST if params[keystr] != 'Empty']
        logger.info('LFCGoalMachine.getPLot, selected players: {}'.format(players))

        # plot the selected players
        ggplt = self.ggplot_age_vs_lgoals(self.df, players)

        # Spyre (v0.2) cannot handle a ggplot object so
        # return a matplotlib (matplotlib.figure.Figure) object
        logger.info('LFCGoalMachine.getPLot, return plot for selected players')
        return ggplt.draw()

    def getHTML(self,params):
        """Return html that describes the app."""
        html = """
        <!DOCTYPE html>
        <html>
        <body>

        <p>
        LFC Goal Machine app by @lfcsorted, your feedback is welcome.</p>
        <a href="https://twitter.com/lfcsorted" class="twitter-follow-button" data-show-count="false">Follow @lfcsorted</a>
        <script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)
        ?'http':'https';if(!d.getElementById(id))
        {js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}
        (document, 'script', 'twitter-wjs');</script>
        <br><br>
        </p>
        
        <p>
        The app plots a player's age against the league goals that the player scored in a top level season.
        You can generate your own plots simply by selecting one or more players from the dropdown list on the Plot tab.
        You can compare players across different seasons and eras.  Enjoy :-).
        </p>
        
        <p>
        The player dropdown list contains all of the LFC players who have scored a top level league goal in more than one season, from 1894-95 to 2014-15.
        The top level is the old 1st Division or the Premier League.
        That's 233 LFC players, from Alan A'Court to Yossi Benayoun.
        The player's age used in the plots is their age at the season mid-point, taken to be 1st January.
        </p>

        <p>
        <br>
        The app is open source software, built using python, spyre, pandas and ggplot.
        It is deployed on Heroku's cloud application platform.
        For more information on the data analysis, the app source code and how it is deployed see the
        <a href="https://github.com/terrydolan/lfcgm">lfcgm github repository</a>.
        </p>

        <p>
        Special thanks to @lfchistory for the base LFC data.
        </p>
        
        <p>
        Terry Dolan, @lfcsorted<br>
        Blog:  <a href="http://www.lfcsorted.com">www.lfcsorted.com</a><br>
        February 2016
        </p>
        
        </body>
        </html>
        """
        return html

if __name__ == '__main__':
    app = LFCGoalMachine()
    app.launch(host='0.0.0.0', port=int(os.environ.get('PORT', '5000')))
