# nyc_weather.csv contains new york city weather for first few days in the month of January. Write a program that can answer following,
# What was the average temperature in first week of Jan
# What was the maximum temperature in first 10 days of Jan
# Figure out data structure that is best for this problem

jan = [{'January 1st': 34}, {'January 2nd': 37}, {
    'January 3rd': 32}, {'January 4th': 35}, {'January 5th': 41}, {'January 6th': 39}, {'January 7th': 38}, {'January 8th': 29}, {'January 9th': 31}, {'January 10th': 32}]


def average(lst):
    number_storage = []
    for element in lst:
        number_storage.append(list(element.values())[0])
    avg = sum(number_storage) / len(number_storage)
    max_temp = max(number_storage)
    return f'Average temp: {avg}\nHighest temperature: {max_temp}'


print(average(jan))
