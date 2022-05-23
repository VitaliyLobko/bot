def decorator(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            print ('waiting from you: add phone')
        except KeyError:
            print('can`t find this key')
    return wrapper


@decorator
def hello(*args):
    return "How can I help you?"

@decorator
def add(param):

    if ADDRESS_BOOK.get(param[0]) != None:
        print('already exist! rewrite? y/n')
        anwser = input().strip()
        if anwser == 'y':
            ADDRESS_BOOK[param[0]] = param[1]
        return f'changed, now: {param[0]} - {param[1]}'
    else:
        ADDRESS_BOOK[param[0]] = param[1]
        return f'added: {param[0]} - {param[1]}'

@decorator
def change(param):
    if len(param) < 2:
        return 'waiting from you: name phone'
    ADDRESS_BOOK[param[0]] = param[1]
    return f'changed, now: {param[0]} - {param[1]}'

@decorator
def phone(param):
    ph = (ADDRESS_BOOK.get(param[0]))
    return f'{param} -  {ph}'

@decorator
def show_all(*args):
    print(ADDRESS_BOOK)



ADDRESS_BOOK = {'vitaliy': '+380 050 616 33 99', 'andriy': '+380 050 646 33 92'}

COMMANDS = {
    hello: "hello",
    add: "add",
    phone: "phone",
    show_all: "show", #show all
    change: "change"
}


def main():
    while True:
        command,  *param = list(input(">>>").lower().split())

        if command == '.' or 'good bye':
            print('Good bye!')
            break

        for k, v in COMMANDS.items():
            if v == command:
                print(k(param))

if __name__ == "__main__":
    main()
