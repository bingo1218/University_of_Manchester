library(tidyverse)
library(Hmisc)
library(performance)

crime <- read_csv("https://raw.githubusercontent.com/ajstewartlang/09_glm_regression_pt1/master/data/crime_dataset.csv")
head(crime)

crime <- separate(crime, col = "City, State", into = c("City", "State") )
head(crime)

crime <- crime %>%
  rename(House_price = "index_nsa") %>%
  rename(Violent_Crimes = "Violent Crimes")
head(crime)

crime %>%
  ggplot(aes(x = Population, y = Violent_Crimes)) + 
  geom_point() + 
  geom_smooth(method = 'lm', se = FALSE) + 
  theme_minimal() + 
  theme(text = element_text(size = 13)) + 
  labs( x = "Population", 
        y = "Violent Crimes")

rcorr(crime$Population, crime$Violent_Crimes)

crime_filtered = filter(crime, Population < 2000000)

crime_filtered %>%
  ggplot(aes(x = Population, y = Violent_Crimes)) + 
  geom_point(alpha = .25) + 
  geom_smooth(method = "lm", se = FALSE) +
  theme_minimal() +
  theme(text = element_text(size = 13)) +
  labs(x = "Population", 
       y = "Violent Crimes")

rcorr(crime_filtered$Population, crime_filtered$Violent_Crimes)

crime_filtered <- filter(crime_filtered, Year == 2015)

crime_filtered %>%
  ggplot(aes(x = Population, y = Violent_Crimes, label = City)) + 
  geom_point() + 
  geom_text(nudge_y = 500, check_overlap = TRUE) + 
  geom_smooth(method = "lm", se = FALSE) + 
  xlim(0, 1800000) +
  theme_minimal() +
  theme(text = element_text(size = 13)) +
  labs(x = "Population", 
       y = "Violent Crimes")

rcorr(crime_filtered$Population, crime_filtered$Violent_Crimes)

model1 <- lm(Violent_Crimes ~ 1, data = crime_filtered)
model2 <- lm(Violent_Crimes ~ Population, data = crime_filtered)

check_model(model2)

anova(model1, model2)

summary(model2)


