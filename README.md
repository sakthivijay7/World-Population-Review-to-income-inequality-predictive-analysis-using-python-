# WorldPopulationReview-to-income-inequality-predictive-analysis-using-python
#### Date:May27 -2025
- **Data Collection:**
BeautifulSoup to scrapping the fresh data in the WorldPopulationReview site using multiple URLs to scrap multiple pages
`Population page,Crime page,education page,GDP (GrossDomesticProduct)page,agriculture page,economic page,billionaire page`.
save all files in csv format.

- **Data Handle:**
Excel power query editor to merged all files by country and remove unnecessary columns and named it clean.

- **Data read:**
1.Pandas to read the merged dataset and describe the statistical report of numerical values.

2.clean the column values only contains numerical values other noisy signs {"$",","} and values {"Tn","Bn","Mn"}are removed

- **Null values:**
SimpleImputer mean and median to fill in the nullvalues. 

- **Data Features(Input):**
{"CrimeIndex","Spend on Education %","GlobalPeaceIndex(GPI)2024(1-5)","GDP(IMF'24)","GDP PER CAPITAL"}

- **Data Target(output):**
"Gini coefficient(World_bank)%" is this defines inequality. 

- **Data Split:**
Features and Target split by train 75%, test 25%

- **Algorithms:**
used algorithms `DecisionTreeRegressor,RandomForestRegressor,XGBRegressor`  and it's parameters 

- **Cross_validation:**
1.cross validation split by 5 and check flow of mean_squared_error,r2_score
2.XGBRegressor work well.

- **Model save:**
Model save in the pickle file for prediction.

- **Result:**
`xgboost MSE: 0.0241
Xgboost r2_score: 0.9995
xgboost less mse and high r2_score.`

- **Validation:**
 result<=25: "Very Low Inequality"
 result<=30: "Low Inequality"
 result<=40: "Moderate Inequality" 
 result<=45: "High Inequality"
 result<=50:  "Very high Inequality"
 result>50:  "Extreme Inequality"

This conditions apply to classifing in the result.
               









