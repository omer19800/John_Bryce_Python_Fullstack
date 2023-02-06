import book
import dates
# dates.today_date()
# dates.current_time()
import datetime

class Loan:

    def __init__(self, customer_id, book_id):
        self.customer_id = customer_id
        self.book_id = book_id
        self.loan_date = None
        self.return_date = None

    def __str__(self):
        pass

    def get_loaner_id(self):
        return self.customer_id

    def get_loaned_book_id(self):
        return self.book_id

    #loan dates methods

    def get_loan_date(self):
        # date = dates.format_date_dmy(self.loan_date)
        # return date
        return self.loan_date

    def set_loan_date_today(self):
        self.loan_date = dates.todays_date()

    def update_loan_date(self, new_date):
        old_loan_date = self.loan_date
        self.loan_date = dates.format_date_dmy(new_date)

    def extend_loan_time(self, how_many_days):
        old_loan_date = self.loan_date
        new_loan_date = old_loan_date + datetime.timedelta(days= int(how_many_days))
        self.loan_date = new_loan_date

#need to figre out how to get the return date of a certain book through the loan function
# maybe dict where key is book id and the date is one of the values in the ictonary that makes the value of the book id
    #NEED TO BE REWORKED - IDEA IS GOOD
    def get_return_date(self, book:object):
        # if isinstance(self.return_date, str) is True:
        #     return self.return_date
        # else:
        #     if book.check_if_loaned == True:
        if book.check_if_loaned() is True:
            self.return_date


        #timedelta via book type for expected return date? just straight up return facts?

#return date - through the dates class dealing with datetime extract the book
        #type from the book id to check how long it can be loaned for and then calculate

        #loan date - through the datetime module deal with this

        #loan should record itself into a file as a log, after return log return
        #should have a method do indicate if late if datetimetoday is more than the return date
