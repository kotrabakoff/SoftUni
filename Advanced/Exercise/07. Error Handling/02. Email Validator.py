class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

acceptable_domains = ["com", "bg", "org", "net"]

email = input()

while email != "End":
    if "@" in email:
        current = email.split("@")
        name = current[0]
        domain = current[1]
        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")
            continue

        domain = domain.split(".")
        domain_extension = domain[1]
        if domain_extension in acceptable_domains:
            print("Email is valid")
        else:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        raise MustContainAtSymbolError("Email must contain @")

    email = input()