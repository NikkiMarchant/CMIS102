# Nicole Marchant CMIS 102 6980
# this programs calculates the salary of a person based on how often and how many newspapers are delivered and adds tips

def main():
    news_cost = 2.31  # average cost of digital newspaper subscription
    commission = .05  # 5% commission rate
    print('Calculate your salary for the week.')  # Display text informing them what the calculation will do
    daily_papers = eval(input('Number of papers delivered on the route per day: '))   # papers delivered per day
    day_week = eval(input('Number of days the paper is delivered per week: '))  # number of days per week
    tips = eval(input('Amount of tips received per week: '))  # amount of tips received
    salary = daily_papers*day_week*news_cost*commission+tips  # calculates the salary
    print('Salary:', salary)


main()
