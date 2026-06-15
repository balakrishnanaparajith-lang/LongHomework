class Patient:
    def __init__(self, name, weight, height, current_illness, medication=False):
        self.name = name
        self.weight = weight
        self.height = height
        self.current_illness = current_illness
        self.medication = medication
        self.doctor = None
        self.admitted = False

    def admit_patient(self, illness):
        self.current_illness = illness
        self.admitted = True
        print(f"Patient is admitted for {self.current_illness}")

        task = input("Is the patient undergoing any medication (yes/no): ").lower()
        if task == "yes":
            self.medication = True
            print("Medication status updated. Further examination will be done.")
        else:
            self.medication = False

    def assign_doctor(self, doctor_name):
        if not self.admitted:
            print("Patient is not admitted. Admitting now.")
            illness = input("Enter illness: ")
            self.admit_patient(illness)

        self.doctor = doctor_name
        print(f"The patient will be assigned to doctor {doctor_name}")

    def show_details(self):
        print("\n--- Patient Details ---")
        print(f"Name: {self.name}")
        print(f"Weight: {self.weight}")
        print(f"Height: {self.height}")
        print(f"Current Illness: {self.current_illness}")
        print(f"Medication: {self.medication}" )
        print(f"Doctor Assigned: {self.doctor}" )
        print(f"Admitted: {self.admitted}" )
pat = Patient("Harry",100,6.2,"Flu",)
while True:
    print("1. Admit Patient")
    print("2, Assign Doctor")
    print("3. Show Details")
    print("4. Exit")
    bob = int(input("Pick An Option"))
    if bob == 1:
        pat.admit_patient(illness=input("Enter your illness"))
    elif bob == 2:
        pat.assign_doctor(doctor_name="Rob")
    elif bob == 3:
        pat.show_details()
    else:
        print("Thanks for coming to the hospital")
        break

