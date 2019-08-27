upper_case = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X','Y', 'Z']
lower_case = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']
spec_char = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '_', '/', '?']
number = ['1','2','3','4','5','6','7','8','9','0']

def HasUppercase(password):
    for letter in password:
        if letter in upper_case:
            return True
            
    else:
        return False

    
def HasLowercase(password):
    for letter in password:
        if letter in lower_case:
            return True
            
    else:
        return False

def HasSpecialChar(password):
    for letter in password:
        if letter in spec_char:
            return True
            break
    else:
        return False


def HasNumber(password):
    for letter in password:
        if letter in number:
            return True
            break
    else:
        return False

pasw = str(input('Enter your password: '))
#validate_pass(pasw)
if len(pasw) >= 8 and len(pasw) <= 16:
    if HasLowercase(pasw) == True:
        if HasUppercase(pasw) == True:
            if HasSpecialChar(pasw) == True:
                if HasNumber(pasw) == True:
                    print('your password qualifies all conditions')
                else:
                    print('must have atleast one number!')
            else:
                print('Your Password must contain atleast one special character,try again')
        else:
            print('Your Password must contain atleast one upper case letters,try again')
    else:
        print('Your Password must contain atleast one lower case letters,try again')
else:
    print("invalid password.\nYour password must have minimum 8 and maximum 16 characters")