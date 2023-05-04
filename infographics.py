#importing important libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#method to return the DataFrame by reading the csv file with the given file name
def return_df(fname):
    '''
    this function takes the file name as parameter and it reads the csv file and 
    returns the data frame

    Parameters
    ----------
    fname : String
        File name to read.

    Returns
    -------
    DataFrame
        the dataframe object read from the given file name.

    '''
    return pd.read_csv(fname)

#method for bar plot
def barplot_usingDF(df,countries,y,ax,title,xlabel,ylabel):
    '''
    method to plot bar plot using the dataFrame object

    Parameters
    ----------
    df : DataFrame
        it is a data frame object from which we plot.
    countries : list object
        the list of countries to plot.
    y : list
        list of years object to plot.
    ax : axis object
        the axis object to plot in the grid.
    title : string
        the title of the plot.
    xlabel : string
        the xlabel of the plot.
    ylabel : string
        the ylabel of the object.

    Returns
    -------
    None.

    '''
    #selecting the sub data frame which countains only specified countries
    df = df.loc[df['Country Name'].isin(countries)]
    #plotting the bar plot
    df.plot.bar("Country Name",y,ax=ax)
    
    #setting up the title, xlabel and ylaebl
    ax.set_title(title)
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.legend(y,loc = "upper right")
    
#piechart
def piechart(x , label , title, ax):
    '''
    method to plot piechart

    Parameters
    ----------
    x : list
        list of values to plot.
    label : list of Strings
         list of stringf for labels.
    title : String
        title of the plot.
    ax : axis object
        axis object to plot in the grid.

    Returns
    -------
    None.

    '''
    #pie function to draw the pie chart
    ax.pie(x , labels = label , autopct = "%1.1f%%")
    #setting the title for the pie graph
    ax.set_title(title)
   
    
#Line plot
def lineplot(years,li,ax,title,xlabel,ylabel):
    '''
    this method takes the list of values to plot a line plot

    Parameters
    ----------
    years : list
        list of years required for plottting.
    li : list
        list of values to plot.
    ax : axis 
        axis object to plot in the grid.
    title : String
        title of the plot.
    xlabel : String
        xlabel for the plot.
    ylabel : String
        ylabel of the plot.

    Returns
    -------
    None.

    '''
    #line plot for the given data
    ax.plot(years,li)
    #setting legen, title, ylabel and xlabel
    ax.legend(loc = "upper right")
    ax.set_title(title)
    ax.set_ylabel(xlabel)
    ax.set_xlabel(ylabel)
   
#converting to numbers of the given columns    
def converttonumbers(df,columns):
    '''
    Method to convert the given columns to numbers

    Parameters
    ----------
    df : Data Frame
        dataframe that need to be converted.
    columns : list of strings
        column names that need to be converted to numeric.

    Returns
    -------
    df : DataFrame
        the modified data frame with the updated.

    '''
    
    #replacing the non numeric values to 0
    df = df.replace(to_replace=".." , value="0")
    #converting the numeric compatable ones to numeric
    df[columns] = df[columns].apply(pd.to_numeric)
    return df

#getting columns as a list
def columnsDF(df):
    '''
    method for getting the columns of the data frame

    Parameters
    ----------
    df : dataframe
        the dataframe for which we need columns.

    Returns
    -------
    list
        list of columns names of the data frame .

    '''
    #getting the column names and returning them
    columns = list(df.columns[1:])
    return [int(x) for x in columns] 

def worldlist(df):
    '''
    method to get the list of values of the world in the given data frame

    Parameters
    ----------
    df : DataFrame
        dataframe in which we need the world data.

    Returns
    -------
    list
        list of world data.

    '''
    return df.loc[df['Country Name'] == 'World'].values.tolist()

def reqData(df,countries,years):
    '''
    method for selecting the data for a particular countries and calculating the 
    rest of the world 

    Parameters
    ----------
    df : Dataframe
        Dataframe from which we need to select particular rows and columns.
    countries : list of strings
        list of countries data one need to select from the data.
    years : list of strings
        list of years data one need to select from the data..

    Returns
    -------
    list
        list of the given countries data and the calculated rest of the countries data.
    list
        list of the countries plus rest of the countries string.

    '''
    xpopulation = df.loc[df['Country Name'].isin(countries)]
    piedf = xpopulation[['Country Name',years]]
    countriespop = 0
    for i in piedf[years]:
        countriespop = countriespop + int(i)
    respop = int(populationDF.loc[populationDF['Country Name'] == 'World'][years]) - countriespop
    return list(piedf[years])+[respop], list(piedf['Country Name'])+['Rest of The World']

#file names
population = "C:\\Users\\bsyam\\Desktop\\dhdv\\population.csv"
co2 = "C:\\Users\\bsyam\\Desktop\\dhdv\\Total greenhouse gas emissions (kt of CO2 equivalent).csv"
forest = "C:\\Users\\bsyam\\Desktop\\dhdv\\Forest area (sq. km).csv"

#strings
f = "Forest Area"
p = "Population"
c = "Total CO2 Emission"

strcountry = 'Countries'
stryear = 'Years'

#list of countries for plotting
countries = ["India","China","Indonesia","Pakistan","United States"]

#DataFrames 
populationDF = pd.read_csv(population)
co2DF = pd.read_csv(co2)
forestDF = pd.read_csv(forest)
populationDF = converttonumbers(populationDF,list(populationDF.columns[1:]))
co2DF = converttonumbers(co2DF, list(co2DF.columns[1:]))
forestDF = converttonumbers(forestDF,list(forestDF.columns[1:]))

# set style for seaborn plots
sns.set_style("darkgrid")

# create figure and subplot gridspec
fig = plt.figure(figsize=(16, 12), dpi=300)
gs = fig.add_gridspec(3, 3)
fig.suptitle("Environmental Indicators for World and for Selected Countries")

# create subplots
ax1 = fig.add_subplot(gs[0, 0]) 
ax2 = fig.add_subplot(gs[0, 1]) 
ax3 = fig.add_subplot(gs[0, 2])
ax4 = fig.add_subplot(gs[1, 0]) 
ax5 = fig.add_subplot(gs[1, 1]) 
ax6 = fig.add_subplot(gs[1, 2])
ax7 = fig.add_subplot(gs[2, 0:2]) 
ax9 = fig.add_subplot(gs[2, 2]) 

# plot CO2 emissions for selected countries
co2title = "Total CO2 Emissions for Selected Countries"
co2ylabel = "CO2 Emissions (kt of CO2 equivalent)"

#selected years for plotting
years = ['1990','2000','2012','2019']
barplot_usingDF(co2DF,countries,years,ax1,co2title,strcountry,co2ylabel)

# plot forest area for the selected countries
foresttitle = "Total Forest area (sq. km) for Selected Countries"
forestylabel = "Forest area (sq. km)"
barplot_usingDF(forestDF,countries,years,ax2, foresttitle, strcountry,forestylabel)

x,y = reqData(populationDF,countries,'2021')
piechart(x,y, p+' in 2021',ax4)

x,y = reqData(populationDF,countries,'1990')
piechart(x,y, p+' in 1990',ax5)

#line plots for the world 
lineplot(columnsDF(populationDF),worldlist(populationDF)[0][1:] ,ax3, 'World '+p, p, stryear)
lineplot(columnsDF(co2DF), worldlist(co2DF)[0][1:],ax6,'World '+p,c,stryear)
lineplot(columnsDF(forestDF)[:-4], worldlist(forestDF)[0][1:-4],ax9,'World '+f,f,stryear)

#Analysed test 
ax7.text(0, 0.60, "According to the world's line graphs, the population and CO2 emissions are rising with a slope of 1, while the forest area is \ndeclining with a negative slope. As a result, we may conclude that global warming is getting worse.\n\nThe chosen nations are those with the highest population densities.\n\nAccording to the pie charts, the population of India has expanded by the greatest proportion in the globe, followed by \nPakistan and China. The United States has also seen population growth.\n\nChina's CO2 emissions climbed significantly, and they have also increased significantly in India, Indonesia, and Pakistan, \nwhereas they are linear in the United States.\n\nChina's forest area is growing, while Indonesia's is shrinking, and in India, Pakistan, and the United States, it is parallel.",
              ha='left', va='center', wrap=True)

plt.savefig('21061898.png')