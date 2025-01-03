"""Email validation."""
# Write your functions here


def has_at_symbol(email: str) -> bool:
    """Check if the email has an @."""
    return "@" in email


def is_valid_username(email: str) -> bool:
    """Check if the email has a valid username."""
    if email.count("@") > 1:
        return False
    email = email.rsplit("@", 1)
    return email[0].replace(".", "").isalnum()


def find_domain(email: str) -> str:
    """Find the domain from the email."""
    email = email.rsplit("@", 1)
    domain = "".join(email[-1])
    return domain


def is_valid_domain(email: str) -> bool:
    """Check if the domain is valid."""
    domain = find_domain(email)

    if domain.count(".") != 1:
        return False
    if not domain.replace(".", "").isalpha():
        return False
    if not 3 <= domain.find(".") <= 10:
        return False
    if not 2 <= domain[::-1].find(".") <= 5:
        return False
    else:
        return True


def is_valid_email_address(email: str) -> bool:
    """Check if the email address is valid."""
    return has_at_symbol(email) and is_valid_username(email) and is_valid_domain(email)


def create_email_address(domain: str, username: str) -> str:
    """Create an email address using the conditions from before."""
    email = username + "@" + domain
    if is_valid_email_address(email):
        return email
    else:
        return "Cannot create a valid email address using the given parameters!"


if __name__ == '__main__':
    print("Email has the @ symbol:")
    print(has_at_symbol("joonas.kivi@gmail.com"))  # -> True
    print(has_at_symbol("joonas.kivigmail.com"))  # -> False

    print("\nUsername has no special symbols:")
    print(is_valid_username("martalumi@taltech.ee"))  # -> True
    print(is_valid_username("marta.lumi@taltech.ee"))  # -> True
    print(is_valid_username("marta lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta&lumi@taltech.ee"))  # -> False
    print(is_valid_username("marta@lumi@taltech.ee"))  # -> False
    print(is_valid_username("karu&pojad@koobas.com"))  # -> False

    print("\nFind the email domain name:")
    print(find_domain("karla.karu@saku.ee"))  # -> saku.ee
    print(find_domain("karla.karu@taltech.ee"))  # -> taltech.ee
    print(find_domain("karla.karu@yahoo.com"))  # -> yahoo.com
    print(find_domain("karla@karu@yahoo.com"))  # -> yahoo.com

    print("\nCheck if the domain is correct:")
    print(is_valid_domain("ohlala@france.eeeeee"))  # -> True
    print(is_valid_domain("pihkva.pihvid@ttu.ee"))  # -> True
    print(is_valid_domain("metsatoll@&gmail.com"))  # -> False
    print(is_valid_domain("ewewewew@i.u.i.u.ewww"))  # -> False
    print(is_valid_domain("pannkook@m.oos"))  # -> False

    print("\nIs the email valid:")
    print(is_valid_email_address("DARJA.darja@gmail.com"))  # -> True
    print(is_valid_email_address("DARJA=darjamail.com"))  # -> False

    print("\nCreate your own email address:")
    print(create_email_address("hot.ee", "vana.ema"))  # -> vana.ema@hot.ee
    print(create_email_address("jaani.org", "lennakuurma"))  # -> lennakuurma@jaani.org
    print(create_email_address("koobas.com", "karu&pojad"))  # -> Cannot create a valid email address using the given parameters!
