'''print(namo.print_detals())
def class_9_D(Name,Roll_no,Call_number):
    return (

                f"Name - {Name}\n"
                f"Class - 9\n"
                f"Sec - D\n"
                f"Roll no - {Roll_no}\n"
                f"Call no - {Call_number}\n........................................................................"

                )

print(class_9_D("Abhishek",3,9155039949))'''

class ninth_D:
    no_of_students=41
    def __init__(self,name,roll_no,Class,sec,call_number):
        self.Name=name
        self.Roll_no=roll_no
        self.Class=Class
        self.Sec=sec
        self.Call_number=call_number
    def print_detals(self):
        return (

                f"Name - {self.Name}\n"
                f"Class - {self.Class}\n"
                f"Sec - {self.Sec}\n"
                f"Roll no - {self.Roll_no}\n"
                f"Call no - {self.Call_number}\n........................................................................"

                )
    @classmethod
    def w(cls,String):
        return cls(*String.split("-"))


class ten_D(ninth_D):
    def __init__(self,name,roll_no,Class,sec,call_number,school):
        self.Name=name
        self.Roll_no=roll_no
        self.Class=Class
        self.Sec=sec
        self.Call_number=call_number
        self.School=school
    def print_detals(self):
        return (

                f"Name - {self.Name}\n"
                f"Class - {self.Class}\n"
                f"Sec - {self.Sec}\n"
                f"Roll no - {self.Roll_no}\n"
                f"Call no - {self.Call_number}\n"
                f"School - {self.School}\n........................................................................"

                )

a=ninth_D.w("Abhishek-9-D-3-9155039949")
b=ten_D.w("Abhishek-10-D-3-9155039949-K.V.No:.1")
print(b.print_detals())
print(a.print_detals())
