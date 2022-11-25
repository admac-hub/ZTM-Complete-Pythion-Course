# Well, a good use case is perhaps when you're collecting emails, maybe you're creating a startup.
# This startup wants to collect, let's say, emails of interested customers.
# Now we want to make sure that whoever is interested in our startup enters proper email addresses, right?
# Because we don't want anybody to fill our databases or our Excel sheets with random.
# Words.
# We want to make sure that something is a correct email.
# Otherwise it says, Hey, this is not a correct email.
# Please try again.

import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = 'andrer'

a = pattern.search(string)
print(a)


