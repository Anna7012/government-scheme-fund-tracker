# Government Scheme Fund Utilization Tracker
# R Visualization Module

# Load processed data
data <- read.csv("../data/processed/mgnrega_expenditure_clean.csv")

# Check data
print(head(data))
print(str(data))

# Convert Financial Year to factor
data$Financial_Year <- as.factor(data$Financial_Year)

# -----------------------------------------
# 1. Year-wise Total Expenditure
# -----------------------------------------

year_total <- aggregate(
  Expenditure_Crore ~ Financial_Year,
  data = data,
  FUN = sum
)

print(year_total)

png("../results/year_wise_expenditure.png",
    width = 1000, height = 600)

plot(
  year_total$Financial_Year,
  year_total$Expenditure_Crore,
  type = "o",
  xlab = "Financial Year",
  ylab = "Total Expenditure (Crore)",
  main = "Year-wise Total Government Scheme Expenditure"
)

dev.off()


# -----------------------------------------
# 2. District-wise Total Expenditure
# -----------------------------------------

district_total <- aggregate(
  Expenditure_Crore ~ District,
  data = data,
  FUN = sum
)

district_total <- district_total[
  order(district_total$Expenditure_Crore, decreasing = TRUE),
]

print(district_total)

png("../results/district_wise_expenditure.png",
    width = 1200, height = 700)

barplot(
  district_total$Expenditure_Crore,
  names.arg = district_total$District,
  las = 2,
  cex.names = 0.7,
  xlab = "District",
  ylab = "Total Expenditure (Crore)",
  main = "District-wise Total Government Scheme Expenditure"
)

dev.off()


# -----------------------------------------
# 3. Year-wise Average Expenditure
# -----------------------------------------

year_average <- aggregate(
  Expenditure_Crore ~ Financial_Year,
  data = data,
  FUN = mean
)

print(year_average)

png("../results/year_wise_average.png",
    width = 1000, height = 600)

plot(
  year_average$Financial_Year,
  year_average$Expenditure_Crore,
  type = "o",
  xlab = "Financial Year",
  ylab = "Average Expenditure (Crore)",
  main = "Year-wise Average Expenditure"
)

dev.off()


# -----------------------------------------
# 4. Top 5 Districts
# -----------------------------------------

top5 <- head(district_total, 5)

print(top5)

png("../results/top5_districts.png",
    width = 1000, height = 600)

barplot(
  top5$Expenditure_Crore,
  names.arg = top5$District,
  las = 2,
  cex.names = 0.8,
  xlab = "District",
  ylab = "Total Expenditure (Crore)",
  main = "Top 5 Districts by Total Expenditure"
)

dev.off()


# -----------------------------------------
# Completed
# -----------------------------------------

cat("\nR visualizations generated successfully!\n")
