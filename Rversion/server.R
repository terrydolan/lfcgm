library(shiny)
library(ggplot2)
library(dplyr)

# create the dflfcgm dataframe
dflfcgm <- read.csv('data/lfc_scorers_tl_pos_age.csv', header=TRUE)

ggplot_age_vs_lgoals <- function(df, players) {
  # Return ggplot of Age vs League Goals for given players in dataframe.
  #
  #  Given the low number of points, ggplot's geom_smooth uses
  #  the loess method with default span.
  TITLE <- 'LFCGMR Age vs League Goals'
  XLABEL <- 'Age at Midpoint of Season'
  YLABEL <- 'League Goals per Season'
  EXEMPLAR_PLAYERS <- c('Ian Rush', 'Kenny Dalglish', 'Roger Hunt', 'David Johnson', 
                        'Harry Chambers', 'John Toshack', 'John Barnes', 'Kevin Keegan')
  EXEMPLAR_TITLE <- 'LFCGMR Example Plot, The Champions: Age vs League Goals'
  
  # if players vector is empty then set the default exemplar options
  if (length(players) == 0) {
    players <- EXEMPLAR_PLAYERS
    TITLE <- EXEMPLAR_TITLE
  } else {
    title <- TITLE
  }
  
  
  # create dataframes to plot...
  # filter those players with only 2 points and those with more than 2
  this_df <- df[df$player %in% players, ]
  this_dfeq2 <- this_df %>% group_by(player) %>% filter(n()==2)
  this_dfgt2 <- this_df %>% group_by(player) %>% filter(n()>2) 
  
  # produce the plot and return it
  this_plot <- ggplot(this_df, aes(x=age, y=league, color=player, shape=player)) + 
    geom_point(size=2) + 
    geom_line(data=this_dfeq2, size=0.2) +
    geom_smooth(data=this_dfgt2, se=FALSE, size=0.2) + 
    xlab(XLABEL) + 
    ylab(YLABEL) + 
    ggtitle(TITLE) + 
    scale_shape_manual(values=0:length(players)) 
  return (this_plot)
}

shinyServer(function(input, output) {
  
  # output a plot of the selected players in dataframe dflfcgm
  output$plot1 <- renderPlot({
    # set players to character vector of values selected in the player input dropdowns
    # note use of the syntax input[['dd1']] instead of input$dd1, because we have
    # to construct the id as a character string, then use it to access the value;
    players <- unlist(lapply(1:DD_NUMBER, function (i) input[[paste0('dd', i)]]))
    print(players)
    
    # if players is full of empty values then set the players to the empty vecor
    if (all(players == EMPTY)) {
      print ('all player selections empty, so set players to empty vector')
      players <- c()
    }
    
    # plot the age vs league goals for selected players
    plt <- ggplot_age_vs_lgoals(dflfcgm, players)
    print(plt)
  })
    
  # output the 'about' for app
  output$about <- renderText({  
    readLines("about.html")  
  })
    
})
