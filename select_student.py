from rich import print as rprint


def select_student(students: list, threshold: int) -> list:
    results: dict = {
        'Accepted': [],
        'Refused':  []
    }

    for student in students:
        if student[1] > threshold:
            results['Accepted'].append(student)
        else:
            results['Refused'].append(student)

    # Sort results in place
    results['Accepted'].sort(key=lambda x: x[1], reverse=True)  # Desc
    results['Refused'].sort(key=lambda x: x[1])                 # Asc
    return results


def main() -> None:
    my_class: list = [['Kermit Wade', 27], ['Hattie Schleusner', 67], ['Ben Ball', 5], ['William Lee', 2]]
    rprint(select_student(students=my_class, threshold=20))


if __name__ == "__main__":
    main()
