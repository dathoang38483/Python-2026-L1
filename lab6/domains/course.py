class Course:
    def __init__(self,name,id,credits):
        self.__name = name
        self.__id = id
        self.__credits = credits
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    def list_info(self):
        print("Course Name: ",self.__name)
        print("Course ID: ",self.__id)