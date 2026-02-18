from pyscript import document



def signUp(event):
    letters = 0
    numbers = 0
    username_input = document.getElementById("usernameInput").value
    if len(username_input) < 7:
        displayErrorSignUp("The username length is less than 7. Try again.")
        return

    password_input = document.getElementById("passwordInput").value

    for char in password_input:
        if char.isdigit():
            numbers += 1
        if char.isalpha():
            letters += 1

    if numbers == 0 :
        displayErrorSignUp("The password does not contain any number.  Try again.")
        return
    if letters == 0:
        displayErrorSignUp("The password does not contain any letter.  Try again.")
        return
    if len(password_input) < 10:
        displayErrorSignUp("The password length is less than 10.  Try again.")
        return
    displayErrorSignUp("Sign Up Success!")
    return

def displayErrorSignUp(message):
    error_message_element = document.getElementById("errorMessage")
    error_message_element.innerHTML = message
    return
