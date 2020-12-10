from User import Member
from User import Librarian

lib = Librarian('Aditya', 'Bangalore', 24, '9999999999', 'Adi123')
print(lib)
lib.addBook('Concepts of Physics','P.K. Nag', 'June 1989', '1279')
lib.addBookItem('Concepts of Physics', 'BTXPB5929C', 'T101')
lib.addBookItem('Concepts of Physics', 'BTXPB5929C', 'T102')
lib.addBook('Machine', 'R.S. Khurmi', 'Februaru 1990', '2087')
lib.addBookItem('Machine', 'CDFTC6432B', 'M201')
lib.addBookItem('Machine', 'CDFTC6432B', 'M201') 
lib.addBook('Theory of Machines', 'Dr. A.G. Ambekar', 'September 1985', '2745')
lib.addBookItem('Theory of Machines', 'SMNQS6664A', 'TM301')
lib.addBookItem('Theory of Machines', 'SMNQS6664A', 'TM302')
lib.viewBooks()
lib.removeBookItem('SMNQS6664A')
lib.viewBooks()
lib.removeBook('Theory of Machines')
lib.viewBooks()

member1 = Member('Aditya', 'Bangalore', 24, '9999999999', 'ADI942')
member2 = Member('Arins', 'Bangalore', 25, '9999999999', 'Ari123')
print(member2)
member1.viewBooks()
member1.reserveBook('Concepts of Physics')
member2.reserveBook('Machine')
member1.viewBooks()

lib.viewissuedBookItems()
lib.viewIssuerInfo()

member1.returnBook()
member2.returnBook()
member1.viewBooks()

member2.issuedBook('Concepts of Physics')

lib.addMember('Alex', 'Bangalore', '23', '8888888888', 'Ale123')
lib.viewMembers()
lib.searchMember('Alex')
lib.removeMember('Arins')
member1.reserveBook('Machine')
