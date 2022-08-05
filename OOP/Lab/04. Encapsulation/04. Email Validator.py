class EmailValidator:
    def __init__(self, min_length, mails, domains):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __is_name_valid(self, name):
        self.is_name_valid = len(name) >= self.min_length
        return self.is_name_valid

    def __is_mail_valid(self, mail):
        self.is_mail_valid = mail in self.mails
        return self.is_mail_valid

    def __is_domain_valid(self, domain):
        self.is_domain_valid = domain in self.domains
        return self.is_domain_valid

    def validate(self, email):
        mail, domain = email.split("@")[1].split(".")
        name = email.split("@")[0]

        is_valid = self.__is_name_valid(name) and self.__is_mail_valid(mail) and self.__is_domain_valid(domain)
        return is_valid


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))



