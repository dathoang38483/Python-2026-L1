class Student :
    def __init__(self,id,name,Dob):
        self.__name = name
        self.__id  = id
        self.__Dob = Dob
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_dob(self):
        return self.__Dob
    def list_info(self):
        print("ID: ",self.__id)
        print("Name: ",self.__name)
        print("Date of Birth: ",self.__Dob)