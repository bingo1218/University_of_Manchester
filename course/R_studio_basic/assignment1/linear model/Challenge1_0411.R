## challenge 1
crime %>%
  ggplot(aes(x = Population, y = Robberies)) + 
  geom_point() + 
  geom_smooth(method = 'lm', se = FALSE) +
  theme_minimal() + 
  theme(text = element_text(size = 13)) + 
  labs(x = "Population",
       y = "Roberries")

rcorr(crime$Population, crime$Violent_Crimes)

crime_filtered2 = filter(crime, Population < 2000000)

crime_filtered2 %>%
  ggplot(aes(x = Population, y = Robberies)) + 
  geom_point(alpha = .25) + 
  geom_smooth(method = "lm", se = FALSE) +
  theme_minimal() +
  theme(text = element_text(size = 13)) +
  labs(x = "Population", 
       y = "Robberies")

rcorr(crime_filtered2$Population, crime_filtered2$Robberies)

crime_filtered2 <- filter(crime_filtered2, Year == 2015)

crime_filtered2 %>%
  ggplot(aes(x = Population, y = Robberies, label = City)) + 
  geom_point() + 
  geom_text(nudge_y = 500, check_overlap = TRUE) + 
  geom_smooth(method = "lm", se = FALSE) + 
  xlim(0, 1800000) +
  theme_minimal() +
  theme(text = element_text(size = 13)) +
  labs(x = "Population", 
       y = "Robberies")

model1 <- lm(Robberies ~ 1, data = crime_filtered2)
model2 <- lm(Robberies ~ Population, data = crime_filtered2)

check_model(model2)

anova(model1, model2)

summary(model2)
