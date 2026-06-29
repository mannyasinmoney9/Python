from mable.person import Person

class Doctor(Person):
    def __init__(self, person_id, name, age, gender, specialization):
        super().__init__(person_id, name, age,  gender)
        self.specialization = specialization


        def person_duty(self):
            print(f"Doctor {self.name} is on duty in the {self.specialization} department.")
            print(f"Doctor {self.name} is available for consultations.")

            def prescription(self, patient_name,):
                print(f"Doctor {self.name} is writing a prescription for {patient_name}")