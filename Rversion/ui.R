library(shiny)

# create the character vector of players for the player input dropdowns
dflfcgm_dd <- read.csv('data/lfcgm_app_dropdown.csv', header=TRUE)
dd_players <- levels(dflfcgm_dd$value)
dd_players <- c(EMPTY, dd_players)

shinyUI(pageWithSidebar(
  headerPanel('The LFC Goal Machine'),
  sidebarPanel(
    helpText('Select LFC players from dropdown list:'),
    # create the player input dropdowns
    lapply(1:DD_NUMBER, function(i) {
      selectInput(paste('dd', i, sep=''), NULL, dd_players, EMPTY)
    }),
    em('lfcgm: R version 1.0'), width=2
  ),
  
  mainPanel(
    tabsetPanel(type = "tabs", 
                tabPanel("Plot", plotOutput("plot1")), 
                tabPanel("About", fluidPage(htmlOutput('about')))
    )
  )
))