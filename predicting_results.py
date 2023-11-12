import pandas as pd

matches = pd.read_csv("matches_statistics.csv", index_col=0)#spesifing that the first column is an index
#curious fact: if I edit the csv file using excel using the "text to columns" tool and then I try to read it as a csv then I will have problems
#because the file is not longer csv.

#missing data. In theory we should have 1520 rows because: 38 matches a season for each team and 2 seasons (38*20*2)=1520
matches["team"].value_counts()#counting the number of matches for each team
#from here we spect that 6 teams have 38 matches as they are allocated to premier league coming from second division (ascienden)
matches.head()
#counting the number of matches for each match week
matches["comp"].value_counts()

#now we will start the cleaning process of the data for the machine learning algorithm
matches.dtypes#checking data types for values
#as a curious fact, machine learning algorithms work only with numerical data (float64 or int64)
#so now we need to find a way to convert all data into a numerical factor
#for the data column we will convert it into date time format
matches["date"] = pd.to_datetime(matches["date"])#here I am just changing the value of the date column
#now we create predictors which are "predictor" which are variables that affect directly to the outcome for example if a team plays in its homw
#stadium or if not
matches["venue_code"] = matches["venue"].astype("category").cat.codes#astype converts to categorical data. Then .cat.codes converts to numerical data
#                                       #this will convert the data into categorical as there are only 2 typees of data. Then we convert it into integers using .cat.codes
matches["opp_code"] = matches["opponent"].astype("category").cat.codes#now each opponent has a code
matches["hour"] = matches["time"].str.replace(":.+","", regex=True).astype("int")#getting only the hour of the match because some teams play better at some hours
matches["day_code"] = matches["date"].dt.dayofweek#here I assign a number for each day of the week

#now we crate our target
matches["target"] = (matches["result"] == "W").astype("int")
#this is the variable we want to predict


#the next step is to create the first machine learning algorith
from sklearn.ensemble import RandomForestClassifier
#this algorithm is able to identify the non linear relationship between the data.
rf = RandomForestClassifier(n_estimators=50, min_samples_split=10, random_state=1)
#In the random forest I have several decision tress with different parameters each one.
#n_estimators number of individual decision tress we will train. The higher this number the more accurate it will be and also the longer it will take to run
#the sample size on each leaf of the decision tree before spliting the branch. If this number is very high likelyhood of overfiting is low(overfiting is when the model give us good
# results when we use known data but bad results when we want to predict the future). So if this number is very high the accuracy over the training data will be low
#random_state=1 means that we will get the same result if we run the model several times as long as the data is the same


#now we are going to select our train and test data from the data set we had at the beginning
train = matches[matches["date"] < "2022-01-01"]#data we will use to train our model
test = matches[matches["date"] > "2022-01-01"]#data used to test the efficacy of the model
#important, this is time series data. So, we are going to use historical data (data before 2022) to predict the future
#(after 2022). Because we cannot use data in the future to predict what is going to happen in the past. We do the other way around




#predictor: is a list of the predictors we created before
predictors = ["venue_code", "opp_code", "hour", "day_code"]
#which is just a list with all the predictors

#then we will fit out model
rf.fit(train[predictors], train["target"])
#here we are training the model useing the predictors to predict our target



#now we will start doing predictions
preds = rf.predict(test[predictors])

#now we have to determine how to determine the accuracy of the model. As this is very important step we are going to consider several variables
#and then we will pick up the one that makes more sense

from sklearn.metrics import accuracy_score #accuracy score is a metric that tells me how many times I predict a loose and it acutally hapened
#and also how many times I predicted a win and it happened
acc = accuracy_score(test["target"], preds)
#print(acc) In my case I got 6.05 which is ok
#but now we want to know in which cases we predicted what was going to happen and in which situations we did not
combined = pd.DataFrame(dict(actual=test["target"], predicted = preds))
#we are going to create a data frame that combines our actual values with our predicted values so we can see the difference
#then lets create a 2 ways table(table showing the frequencies of 2 diff categories of data collected from the same sample)
pd.crosstab(index=combined["actual"], columns=combined["predicted"])
#index are the rows of the crosstable
#we have a problem. We want to predict wins. But my model in this case is not very accurate. So we are going to use another metric to 
#meausure our accuracy
from sklearn.metrics import precision_score#this will tell: when we predict an outcome, what percentage of time that outcome actually happened
precision_score(test["target"], preds)


#until now our scores are not the best ones, this is why we are going to improve this model
#frist create more predictor to increase the accuracy of the model
grouped_matches = matches.groupby("team")#this will create a df for every squad in our data set


def rolling_averages(group, cols, new_cols):
    group = group.sort_values("date")
    #here the oldest come first. As we need data of the oldest matches to compute the rolling averages of the newest matches.
    rolling_stats = group[cols].rolling(3, closed ="left").mean()#the last paramiter makes sure that the time perios(ex:match week) in which we currently are is not included in the rolling average
    #here we take a set of columns group[cols]. compute the rolling average (.rolling). 
    group[new_cols] = rolling_stats#we assign the rolling averages to the new columns
    group = group.dropna(subset = new_cols)
    #what this paramiter does is that imagine we are in week 2 and we tell the function to calculate the moving average of the last 3 weeks what it would do is to include missing values for the values that does not yet exist
    return group

#the columns we want to create moving average are
cols = ["gf", "ga", "sh", "sot", "dist", "fk", "pk", "pkatt"]
new_cols = [f"{c}_rolling" for c in cols]
#we are going to prove the function with just one group(manchester city)
group = grouped_matches.get_group("Manchester City")
rolling_averages(group, cols, new_cols)

#now that we know how to make it with one group we are going to scale it up for all the teams
matches_rolling = matches.groupby("team").apply(lambda x: rolling_averages(x, cols, new_cols))
#the above code creates a df for each team in the data set. Then applys the function rolling_averages
#if we notice after the code above we have created a new index column. This is why we are going to get rid of it
matches_rolling = matches_rolling.droplevel("team")
#we get rid of this extra index because in pandas to access a specific row we need its index. So if we have 2 indices then we need to refer
#to two indices to get one row
#however now we do not have unique indices. This is why we will use the next line of code to get them
matches_rolling.index = range(matches_rolling.shape[0])
#the .shape method gets the dimension of the data set. However, it would include 2 values, the first is the # of rows and the second the number
#of columns. This is why we use the [0]


#now we will train again our model. For such purpose we will create a function that allow us to make several predictions and then we will measure its accuracy
def make_predictions(matches, predictors):
    #spliting data between training and predicting one
    train = matches[matches["date"] < "2022-01-01"]
    test = matches[matches["date"] > "2022-01-01"]
    #then we fit our random forest
    rf.fit(train[predictors], train["target"])
    #create predictions
    preds = rf.predict(test[predictors])
    #combining our predictions in a data frame to measure accuracy
    combined = pd.DataFrame(dict(actual= test["target"], predicted = preds), index=test.index)
    precision = precision_score(test["target"], preds)
    return combined, precision

combined, precision = make_predictions(matches_rolling, predictors + new_cols)
#to make the most out of the combined data we need to compare it with the mathces data set. So we know exactly how many time we were correct
combined = combined.merge(matches_rolling[["date", "team", "opponent", "result"]], left_index=True, right_index=True)#last 2 arguments to merge according to indices
print(combined)


#the final step consit on merging data of matches in house and matches outside. With this we pretend to improve the accuracy of our model
#however, there is a problem with the names of some teams. Sometimes, when a team is as a guest and its name is long, the premier league shorten its name
#class MissingDict(dict):#this is a class that inherits from the dictionary class
    #__missing__ = lambda self, key:key
    