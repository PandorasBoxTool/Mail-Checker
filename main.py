import sys
import pop3_checker as p3_cr
import imap_checker as ip_cr

def main():
    txt = input("Path to the TXT with the e-mail addresses? ")
    output = input("Path where the results are to be saved? ")

    email_checker_help = f"""{sys.argv[0]}: [EMAIL-LISTE] [OUTPUT-DATEI]

    Listenformat: EMAIL:PASSWD
    WARNUNG: Das Passwort darf kein ':' enthalten!
    """

    supported_email_providiers = ["gmail.com", "outlook.de",
                                  "yahoo.com", "rambler.ru", "outlook.com", "mail.ru", "yandex.com",
                                  "yandex.de", "hotmail.com", "hotmail.de"]

    sys.argv = [0, 0, 0]
    sys.argv[1] = txt
    sys.argv[2] = output

    Pop3_EmailChecker_GMX = p3_cr.Checker(pop3_server="pop.gmx.net")
    Pop3_EmailChecker_Yahoo = p3_cr.Checker(pop3_server="pop.mail.yahoo.com")
    Pop3_EmailChecker_RamblerRu = p3_cr.Checker(pop3_server="pop3.rambler.ru")
    Imap_EmailChecker_Outlook = ip_cr.Checker(imap_server="outlook.office365.com")
    Imap_EmailChecker_GMail = ip_cr.Checker(imap_server="imap.gmail.com")
    Imap_EmailChecker_Yandex = ip_cr.Checker(imap_server="imap.yandex.com")
    Imap_EmailChecker_MailRu = ip_cr.Checker(imap_server="imap.mail.ru")
    Imap_EmailChecker_RamblerRu = ip_cr.Checker(imap_server="imap.rambler.ru")
    Pop3_EmailChecker_Hotmail = ip_cr.Checker(imap_server="outlook.office365.com")



    with open(sys.argv[1], "r") as email_list:
        emails_data = email_list.read().split("\n")
        with open(sys.argv[2], "w") as output_file:
            for email_data in emails_data:
                email = email_data.split(":")[0]
                password = email_data.split(":")[1]
                email_provider = email.split("@")[1]
                

                if not email_provider in supported_email_providiers:
                    output_file.write(email_data + " " + "Nicht unterstützter Email Provider!\n")
                    continue
                else:
                    if email_provider == "gmail.com":
                        if Imap_EmailChecker_GMail.check_credentials(email, password):
                            output_file.write(email_data + " " + "Login erfolgreich.\n")
                        else:
                            output_file.write(email_data + " " + "Login fehlgeschlagen!\n")
                            
                            
                    if email_provider == "outlook.de" or email_provider == "outlook.com":
                        if Imap_EmailChecker_Outlook.check_credentials(email, password):
                            output_file.write(email_data + " " + "Login erfolgreich.\n")
                        else:
                            output_file.write(email_data + " " + "Login fehlgeschlagen!\n")
                            
                            
                    if email_provider == "yahoo.com":
                        if Pop3_EmailChecker_Yahoo.check_credentials(email, password):
                            output_file.write(email_data + " " + "Login erfolgreich.\n")
                        else:
                            output_file.write(email_data + " " + "Login fehlgeschlagen!\n")
                            
                            
                    if email_provider == "rambler.ru":
                        if Pop3_EmailChecker_RamblerRu.check_credentials(email, password):
                            output_file.write(email_data + " " + "Login erfolgreich.\n")
                        else:
                            output_file.write(email_data + " " + "Login fehlgeschlagen!\n")
                            
                            
                    if email_provider == "mail.ru":
                        if Imap_EmailChecker_MailRu.check_credentials(email, password):
                            output_file.write(email_data + " " + "Login erfolgreich.\n")
                        else:
                            output_file.write(email_data + " " + "Login fehlgeschlagen!\n")
                            

                    if email_provider == "yandex.com" or email_provider == "yandex.de":
                        if Imap_EmailChecker_Yandex.check_credentials(email, password):
                            output_file.write(email_data + " " + "Login erfolgreich.\n")
                        else:
                            output_file.write(email_data + " " + "Login fehlgeschlagen!\n")
                            

                    if email_provider == "gmx.com" or email_provider == "gmx.de":
                        if Imap_EmailChecker_Yandex.check_credentials(email, password):
                            output_file.write(email_data + " " + "Login erfolgreich.\n")
                        else:
                            output_file.write(email_data + " " + "Login fehlgeschlagen!\n")


                    if email_provider == "hotmail.com" or email_provider == "hotmail.de":
                        if Pop3_EmailChecker_Hotmail.check_credentials(email, password):
                            output_file.write(email_data + " " + "Login erfolgreich.\n")
                        else:
                            output_file.write(email_data + " " + "Login fehlgeschlagen!\n")

                                

            output_file.close()
        email_list.close()

    print("Fertig!")

if __name__ == "__main__":
    main()
