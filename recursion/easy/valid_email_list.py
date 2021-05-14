def validEmailList(emailList):
    validEmails = []
    for email in emailList:
        if email.count('@') > 1 or email.count(' '):
            continue
        splitEmail = email.split('@')
        if splitEmail[1].count('.') == 1:
            validEmails.append(email)

    return validEmails
