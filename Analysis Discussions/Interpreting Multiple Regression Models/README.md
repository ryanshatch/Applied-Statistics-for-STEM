## Null Hypothesis (H0): 

#### Neither weight (wt) nor horsepower (hp) have a significant impact on miles per gallon (mpg) and suggests that their coefficients should be zero.

## Alternative Hypothesis (H1):

#### At least one of these predictors, weight or horsepower, significantly affects mpg; indicated by non-zero coefficients.

#### Level of significance (α): **0.05** (5%)

##

## Test statistic and P-value:

#### The F-statistic is 66.05 with a P-value of 3.99e-11. 
#### This extremely low P-value made me reject the null hypothesis, which helped to confirm that at least one of the predictors significantly influences the mpg.

<hr>
<hr>

## <center>Specifics on Predictors:</center>

### Weight (wt):

#### The slope coefficient is -3.7842 with a P-value less than 0.001, clearly under the 0.05 alpha level, making weight a significant predictor at the 5 % significance level.

### Horsepower (hp): 

#### The slope coefficient stands at -0.0334 with a P-value of 0.001, also significant under the 5% threshold.

##

#### While the F-test checks if at least one predictor influences the dependent variable, it doesn't specify which one. Individual t-tests for each predictor address this by testing if their coefficients significantly differ from zero. This approach helps to locate the influence of each predictor separately.

##

### Coefficient of Determination (R-squared): 

#### At 0.830, the model explains 83% of the variability in mpg using weight and horsepower. This high R-squared value indicates a strong fit to the data.

## Statistical Significance vs. Practical Significance: 

#### It's important to remember that while these results show statistical significance, which indicates that there is indeed a relationship between predictors and mpg, they still don't measure the size or practical importance of the effect. Its also important to remember that statistical correlation does not equal up to causation, and other unmeasured factors might also affect the results.