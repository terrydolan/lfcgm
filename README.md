# lfcgm

The Liverpool Football Club Goal Machine (lfcgm) is an interactive python web app that takes a selected LFC player and plots the player's age against the league goals that the player scored in a top level season. The app knows about every LFC player who scored a top level league goal in more than one season, from 1894-95 to 2014-15. 

## Try the app

The lfcgm web app is deployed at [lfcgm.herokuapp.com](http://lfcgm.herokuapp.com). Have a play! You can use the app to compare players across different seasons and eras. Simply select one or more players and take a look at their graph. 

## Data analysis and app construction

The [lfcgm notebook](http://nbviewer.ipython.org/github/terrydolan/lfcgm/blob/master/lfcgm.ipynb) describes the data analysis and how the app was built and deployed.

## Building blocks

The analysis and the app use python, ipython notebook, pandas, ggplot and spyre. The app is deployed using heroku.

[Spyre](https://github.com/adamhajari/spyre) is a web app framework for providing a simple user interface for Python data projects.

[Ggplot](http://ggplot.yhathq.com) is a python plotting library based on R's ggplot2.

[Pandas](http://pandas.pydata.org) is a python data analysis library.

[Heroku](https://www.heroku.com/platform) is a cloud platform for deploying and running web apps.

The app uses the [heroku scipy buildpack](https://github.com/thenovices/heroku-buildpack-scipy).

## Data source

Special thanks to [lfchistory.net](http://www.lfchistory.net) who provided the base LFC data.

## Licence

MIT. 

## Acknowledgements

Thanks to the providers of the tools and data.


Terry Dolan, @lfcsorted  
blog: [www.lfcsorted.com](http://www.lfcsorted.com)