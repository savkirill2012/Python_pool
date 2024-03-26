import threading


class Doctor():
    cur_id = 8

    def __init__(self, id=cur_id):
        self.id = id 
        self.__inc_id()
        self.r_screwdriver = Screwdriver()
        self.l_screwdriver = None

    def __inc_id(cls):
        cls.cur_id += 1

    def run(self, l_doc: 'Doctor', r_doc: 'Doctor'):
        self.l_screwdriver = l_doc.r_screwdriver
        l_doc.r_screwdriver = None
        if not self.l_screwdriver or not self.r_screwdriver:
            self.r_screwdriver = r_doc.r_screwdriver
            r_doc.r_screwdriver = None
        print(f'Doctor {self.id}: BLAST!')
                

    # def take_screw_from(self, doc: Doctor):
    #     if doc.num_screwdrivers > 0:
    #         doc.num_screwdrivers -= 1
    #         self.num_screwdrivers += 1
    #         self.have_screwdrivers.append(doc.have_screwdrivers.pop())




class Screwdriver():
    pass 


if __name__ == '__main__':
    pass