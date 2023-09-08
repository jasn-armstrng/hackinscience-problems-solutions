import csv
import datetime
from pprint import pprint


def generate_csv(input: list[tuple]) -> None:
    headers = [i[0] for i in input[0]]

    with open('results.csv', 'w', newline='') as csvfile:
        results_writer = csv.writer(csvfile, delimiter=',', quotechar='"')
        results_writer.writerow(headers)
        for t in input:
            temperature = t[0][1]
            date = t[1][1].strftime("%m/%d/%Y")
            locations = ",".join(t[2][1])
            weather = t[3][1]
            results_writer.writerow([temperature, date, locations, weather])


# CSV Sample:
# firstname,Lastname,Birthdate,Marks,Comments
# Ada,Lovelace,12/10/1815,"4242,1010",The first one
# Linus,Torvald,12/28/1969,"42,21",Have a problem with penguin
# Theo,De Raadt,05/19/1968,"18,19,20",This guy is just crazy
# Dennis,Ritchie,09/09/1941,"20,20,20",Like a boss
# Alan,Turing,06/23/1912,"42,42,42",Shouldn't eat apple
def parse_student_data_csv(path_to_csv: str) -> list[dict]:
    with open(path_to_csv, newline='') as csvfile:
        csv_parser = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        students = []
        for row in csv_parser:
            students.append({
                'Firstname': row['Firstname'],
                'Lastname':  row['Lastname'],
                'Birthdate': datetime.datetime.strptime(row['Birthdate'], "%m/%d/%Y").date(),
                'Marks':     [int(x) for x in row['Marks'].split(',')],
                'Comments':  row['Comments']
                })

    return students


def main() -> None:
    meteo = [(('temperature', 42),
              ('date', datetime.date(2017, 1, 22)),
              ('locations', ('Berlin', 'Paris')),
              ('weather', 'sunny')),
             (('temperature', -42),
              ('date', datetime.date(2017, 1, 22)),
              ('locations', ('Marseille', 'Moscow')),
              ('weather', 'cloudy'))]

    generate_csv(meteo)

    students = parse_student_data_csv("files/students.csv")
    pprint(students)


if __name__ == "__main__":
    main()
