def fireEmployees(employees, unemployed):
    result = []
    for e in employees:
        if e not in unemployed:
            result.append(e)

    return result
