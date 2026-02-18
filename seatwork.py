from pyscript import document
import random

def checkIfEligible(event):
    done_with_reg_radio = document.getElementById("doneWithReg")


    have_med_radio = document.getElementById("haveMedClearance")



    grade_level = document.getElementById("gradeLevel").value

    
    if done_with_reg_radio.checked and have_med_radio.checked and int(grade_level) > 6 and int(grade_level) < 10:
        displayCongratulatory()
    elif not done_with_reg_radio.checked:
        displayInstructionRegister()
    elif not have_med_radio.checked:
        displayInstructionMedical()
    return

    return

def displayCongratulatory():
    message_div = document.getElementById("messageDiv")
    message = document.getElementById("message")
    message_image = document.getElementById("messageImage")

    team_name = ""
    team_image = ""

    team_random_number = random.randint(1, 4)

    if team_random_number == 1:
        team_name = "Blue Bears"
        team_image = "bluebears.jpg"
    elif team_random_number == 2:
        team_name = "Red Bulldogs"
        team_image = "redbulldogs.jpg"
    elif team_random_number == 3:
        team_name = "Yellow Tigers"
        team_image = "yellowtigers.jpg"
    else:
        team_name = "Green Hornets"
        team_image = "greenhornets.jpg"

    message.innerHTML = "Congratulations! You are part of the " + team_name
    message_image.src = team_image

    print("CONGRATS! YOU ARE ELIGIBLE")
    return


def displayInstructionRegister():
    message = document.getElementById("message")
    message_image = document.getElementById("messageImage")

    message.innerHTML = "You should go to the website to register online"
    message_image.src = ""
    return


def displayInstructionMedical():
    message = document.getElementById("message")
    message_image = document.getElementById("messageImage")

    message.innerHTML = "You should get a medical clearance."
    message_image.src = ""
    return