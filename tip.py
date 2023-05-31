def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    remove_dolar = d.replace("$", "")
    number = float(remove_dolar)
    return (round(number, 1))


def percent_to_float(p):
    # TODO
    remove_percent = p.replace("%", "")
    percent =float(remove_percent)
    convert_decimal = percent / 100
    return (round(convert_decimal, 2))

main()