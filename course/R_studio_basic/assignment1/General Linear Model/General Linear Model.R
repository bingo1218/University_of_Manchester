#VIF = variance inflation factor: by function in R: 
#vif() if the value > 10 (or 5 if be more conservative),
# we should pay attention to the multicollinearity

#1 resudual should be normal
#homoscedasticity problem could be corrected by using weighted(generalised ) least squares regression instead of OLS regression
#outlinear >mean±2.5sd
#influential cases can be detected easily via Cook's distance

#
library(tidyverse) # Load the tidyverse packages
library(Hmisc) # Needed for correlation
library(MASS) # Needed for maths functions
library(car) # Needed for VIF calculation
library(olsrr) # Needed for stepwise regression 
library(performance) # Needed to check model assumptions

#
MRes_tut2 <- read_csv("https://raw.githubusercontent.com/ajstewartlang/10_glm_regression_pt2/master/data/MRes_tut2.csv")

ggplot(MRes_tut2, aes(x = age, y = corr_spell)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  theme_minimal() +
  theme(text = element_text(size = 13)) 

ggplot(MRes_tut2, aes(x = RA, y = corr_spell)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  theme_minimal() +
  theme(text = element_text(size = 13)) 

ggplot(MRes_tut2, aes(x = std_RA, y = corr_spell)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  theme_minimal() +
  theme(text = element_text(size = 13)) 

ggplot(MRes_tut2, aes(x = std_SPELL, y = corr_spell)) + 
  geom_point() + 
  geom_smooth(method = "lm", se = FALSE) +
  theme_minimal() +
  theme(text = element_text(size = 13)) 

model0 <- lm(corr_spell ~ 1, data = MRes_tut2)
model1 <- lm(corr_spell ~ age + RA + std_RA + std_SPELL, data = MRes_tut2)
anova(model0, model1)

check_model(model1)

MRes_tut2_drop10 <- filter(MRes_tut2, case != "10")

model2 <- lm(corr_spell ~ age + RA + std_RA + std_SPELL, data = MRes_tut2_drop10)
check_model(model2)

vif(model2)

rcorr(MRes_tut2_drop10$RA, MRes_tut2_drop10$std_RA)

model3 <- lm(corr_spell ~ age + std_RA + std_SPELL, data = MRes_tut2_drop10)

vif(model3)

check_model(model3)

summary(model3)

model0 <- lm(corr_spell ~ 1, data = MRes_tut2_drop10)
anova(model3, model0)

model0 <- lm(corr_spell ~ 1, data = MRes_tut2_drop10)
model1 <- lm(corr_spell ~ age + std_RA + std_SPELL, data = MRes_tut2_drop10)
steplimitsf <- step(model0, scope = list (lower = model0, upper = model1), direction = "forward")
summary(steplimitsf)

steplimitsb <- step(model1, direction = "back")
summary(steplimitsb)

steplimitsboth <- step(model0, scope = list (upper = model1), direction = "both")

check_model(steplimitsboth)

summary(steplimitsboth)

install.packages("olsrr")
library(olsrr)
pmodel <- ols_step_forward_p(model1)
pmodel
