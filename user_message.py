def user_message(context):

    message_01 = "You have logged in successfully!"
    message_02 = "You have successfully registered a new account."
    message_03 = "Password has been reset"
    message_04 = "No such user exists, please try again."
    message_05 = "No such user exists, please try again."
    message_06 = "This user already exists"

    if context == 1:
        output_message = message_01
    elif context == 2:
        output_message = message_02
    elif context == 3:
        output_message = message_03
    elif context == 4:
        output_message = message_04
    elif context == 5:
        output_message = message_05
    else:
        output_message = message_06
    
    return output_message