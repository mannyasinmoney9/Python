from mable.person import Person

class Patient (Person):
    def __init__(self, person_id, name, age, gender, medical_history):
        super().__init__(person_id, name, age  , gender)
        self.medical_history = medical_history