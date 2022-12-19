# this file needs to contain a single function, called "menu"
# that function will get a list of strings

def menu(strings):
    user_choice = input(f'Enter one of {strings}').strip()
    
    if user_choice in strings:
        return user_choice

    return ''  