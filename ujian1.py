# nomor 1

def Hashtag(string):
    words = string.split()
    words_capitalize = [word.capitalize() for word in words]
    words_length = sum([len(word) for word in string])
    final_words = ''.join(words_capitalize)

    if words_length < 1 or words_length > 140:
        return False
    else:
        return '#' + final_words
        
# nomor 2

def create_phone_number(number):

    if type(number) == list:
        length = len(number)
        if length == 10:
            return "({}{}{}) {}{}{}-{}{}{}{}".format(number[0], number[1], number[2], number[3], number[4], number[5], number[6], number[7], number[8], number[9]) 
        else:
            return False
    else:
        return False


# nomor 3

def sort_odd_even(number):

    odd_even = ['even' if num % 2 == 0 else 'odd' for num in number]
    ascending_odd = sorted([num for num in number if num % 2 != 0])
    descending_even = sorted([num for num in number if num % 2 == 0])[::-1]  # reverse


    return odd_even


print(sort_odd_even([5,3,2,8,1,4]))

# nomor 4

number = int(input('Please insert number: '))

k = 3
for row in range(1, number+1):
    for col in range(1, 2*number):
        if  row+col == number+1 or col-row == number-1:
            print('#', end='')
        elif row == number and col != k:
            print('#', end='')
            k += 2
        else:
            print(end='_')
    print()