if __name__ == '__main__':
    N = int(input("Enter:"))
    a= []
    for i in range(N):
        string = list(input("Enter:").split(' '))
        match (string[0]):
            case 'insert':
                a.insert(int(string[1]),int(string[2]))
            case 'print':
                print(a)
            case 'remove':
                a.remove(int(string[1]))
            case 'append':
                a.append(int(string[1]))
            case 'sort':
                a.sort()
            case 'pop':
                a.pop()
            case 'reverse':
                a.reverse()
