list_of_numbers = []


while True:
    try:
        m_str = input()
        m_int = int(m_str)
    except ValueError:
        print("The input must be a valid number")

    list_of_numbers.append(m_int)

    if m_int < 0:
        print(sum(list_of_numbers))
        exit()
