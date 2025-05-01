from models import Company, Dev, Freebie
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Set up the session
engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
session = Session()

# Test - Create Devs and Company
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
company = Company(name="TechCorp", founding_year=2000)

session.add(dev1)
session.add(dev2)
session.add(company)
session.commit()

# Test - Give a freebie to a dev
company.give_freebie(dev1, "T-shirt", 10)

# Test - Print details of the freebie
freebie = session.query(Freebie).first()
print(freebie.print_details())  # Should print "Alice owns a T-shirt from TechCorp"

# Test - Oldest company
oldest = Company.oldest_company()
print(oldest.name)  # Should print the name of the oldest company

# Test - Check if a dev received a specific freebie
print(dev1.received_one("T-shirt"))  # Should return True
print(dev2.received_one("T-shirt"))  # Should return False

# Test - Give away a freebie
dev1.give_away(dev2, freebie)
print(freebie.print_details())  # Should now print "Bob owns a T-shirt from TechCorp"
