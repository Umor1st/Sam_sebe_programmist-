import csv

movies = [["Звездные войны", "Терминатор", "Искусственный интеллект"], ["Дурак", "Матильда", "Левиафан"], ["Люди в черном", "Я - робот", "Эволюция"]]
with open("movie.csv", "w") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(movies[0])
    w.writerow(movies[1])
    w.writerow(movies[2])
