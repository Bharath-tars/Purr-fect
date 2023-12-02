import smtplib
my_email = "tars4real@gmail.com"
my_pass = "vzwx eavq pfnj knsh"

def shoot_mail(name,email,text_summary,sentences, msg):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=email,
                           msg = f"Subject: | Purr-fect Text Summarizer Report\n\n" \
                            f"Meow {name},\n" \
                            f"Greetings from Purr-fect, where text gets a feline makeover! Your summarized text is ready to pounce.\n" \
                            f"Process status: {msg}\n" \
                            f"->Here's a snippet of Your Summarized Text:\n" \
                            f"{text_summary}\n" \
                            f"->Here's the summarized text in sentence format:\n" \
                            f"{sentences}\n" \
                            f"We hope our meow-gical services have left you feline fantastic! If you have any questions or feedback, we're all ears.\n" \
                            f"Paws and Whiskers,\n" \
                            f"The Purr-fect Team\n\n\n" \
                            f"Don't forget to follow us on Linktree for the latest meow-tastic updates:\n" \
                            f"Linktree: https://linktr.ee/bharath2k35\n"
                            )
        print("Message sent")

def details(NAME,EMAIL,message, summary, full_data):
    text_summary = summary
    sentences = full_data
    msg = message
    name=NAME
    email=EMAIL
    shoot_mail(name,email,text_summary,sentences, msg)
