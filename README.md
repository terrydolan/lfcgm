# lfcgm

<<<<<<< HEAD
The LFC Goal Machine (lfcgm) is an interactive python web app that takes a selected Liverpool Football Club player and plots the player's age against the league goals that the player scored in a top level season. The app knows about every LFC player who scored a top level league goal in more than one season, from 1894-95 to 2014-15. 
=======
The Liverpool Football Club Goal Machine (lfcgm) is an interactive python web app that takes a selected LFC player and plots the player's age against the league goals that the player scored in a top level season. The app knows about every LFC player who scored a top level league goal in more than one season, from 1894-95 to 2015-16. 
>>>>>>> hdata

## Try the app

The lfcgm web app is deployed at [lfcgm.lfcsorted.com](http://lfcgm.lfcsorted.com). Have a play! You can use the app to compare players across different seasons and eras. Simply select one or more players and take a look at their graph. 

## Graphic detail

For a discussion of some interesting graphs from the lfcgm see this lfcsorted blog post [The LFC Goal Machine - Graphic Detail](http://www.lfcsorted.com/2016/03/the-lfc-goal-machine-graphic-detail.html).

## Data analysis and app construction

The [lfcgm notebook](http://nbviewer.ipython.org/github/terrydolan/lfcgm/blob/master/lfcgm.ipynb) describes the data analysis and how the app was built and deployed.

## Building blocks

The analysis and the app use python, ipython notebook, pandas, ggplot and spyre. The app is deployed using heroku.

[Spyre](https://github.com/adamhajari/spyre) is a web app framework for providing a simple user interface for Python data projects.

[Ggplot](http://ggplot.yhathq.com) is a python plotting library based on R's ggplot2.

[Pandas](http://pandas.pydata.org) is a python data analysis library.

[Heroku](https://www.heroku.com/platform) is a cloud platform for deploying and running web apps.

The app uses the [heroku scipy buildpack](https://github.com/thenovices/heroku-buildpack-scipy).

## R version

The Rversion folder contains the source code for the R version of the lfcgm, with an enhanced UI. 
You can try the app at [lfcgmR](https://terrydolan.shinyapps.io/lfcgmR). 
This version is built using R, RStudio, shiny, ggplot and dplyr. It is deployed on R Studio's platform. 

## Data source

Special thanks to [lfchistory.net](https://http://www.lfchistory.net) who provided the base LFC data.

## Licence

MIT. 

## Acknowledgements

Thanks to the providers of the tools and data.


Terry Dolan, @lfcsorted
blog: www.lfcsorted.com
