crime %>%
  ggplot(aes(x = Violent_Crimes, y = House_price)) + 
  geom_point() + 
  geom_smooth(method = 'lm', se = FALSE) +
  theme_minimal() + 
  theme(text = element_text(size = 13)) + 
  labs(x = "Violent crimes",
       y = "House price")

crime_filtered3 = filter(crime, Violent_Crimes < 30000)

crime_filtered3 %>%
  ggplot(aes(x = Violent_Crimes, y = House_price)) + 
  geom_point() + 
  geom_smooth(method = 'lm', se = FALSE) +
  theme_minimal() + 
  theme(text = element_text(size = 13)) + 
  labs(x = "Violent crimes",
       y = "House price")

rcorr(crime_filtered3$Violent_Crimes, crime_filtered3$House_price)

crime_filtered3 <- filter(crime_filtered3, Year == 2015)

crime_filtered3 %>%
  ggplot(aes(x = Violent_Crimes, y = House_price, label = City)) + 
  geom_point() + 
  geom_text(nudge_y = 10, check_overlap = TRUE) + 
  geom_smooth(method = "lm", se = FALSE) + 
  xlim(0, 26000) +
  theme_minimal() +
  theme(text = element_text(size = 13)) +
  labs(x = "Violent crimes", 
       y = "House price")

rcorr(crime_filtered3$Violent_Crimes, crime_filtered3$House_price)

model1 <- lm(House_price ~ 1, data = crime_filtered3)
model2 <- lm(House_price ~ Violent_Crimes, data = crime_filtered3)

check_model(model2)

anova(model1, model2)

summary(model2)
