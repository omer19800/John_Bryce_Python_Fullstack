class Table:
    def __init__(self, table_id: int, seats_number: int,
                 is_occupied: bool, res_time_limit: str):
        self.__table_id = table_id
        self._seats_number = seats_number
        self.__is_occupied = is_occupied
        self._res_time_limit = res_time_limit
        self.res_start_time = str
        self.occupied_seats = int

    # create update read delete
    def reserve_a_table(self, guests):
        if guests > self._seats_number or self.__is_occupied == True:
            return False
        elif guests <= self._seats_number:
            self.__is_occupied = True
            self.occupied_seats = guests
            return True

    def release_a_table(self):
        now = None
        if self.res_start_time + self._res_time_limit == now:
            self.__is_occupied = False

table_1 = Table(1, 2, False, 90)

if __name__ == '__main__':
