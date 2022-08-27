crime %>%
  ggplot(aes(x = Population, y = House_price)) + 
  geom_point() + 
  geom_smooth(method = 'lm', se = FALSE) +
  theme_minimal() + 
  theme(text = element_text(size = 13)) + 
  labs(x = "Population",
       y = "House price")

rcorr(crime$Population, crime$House_price)

crime_filtered4 <- filter(crime, Year == 2015)

crime_filtered4 %>%
  ggplot(aes(x = Population, y = House_price, label = City)) + 
  geom_point() + 
  geom_text(nudge_y = 10, check_overlap = TRUE) + 
  geom_smooth(method = "lm", se = FALSE) + 
  xlim(0, 3000000) +
  theme_minimal() +
  theme(text = element_text(size = 13)) +
  labs(x = "Population", 
       y = "House price")

rcorr(crime_filtered4$Population, crime_filtered4$House_price)

model1 <- lm(House_price ~ 1, data = crime_filtered4)
model2 <- lm(House_price ~ Population, data = crime_filtered4)

check_model(model2)

anova(model1, model2)

summary(model2)
