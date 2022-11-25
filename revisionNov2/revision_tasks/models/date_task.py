from odoo import api, fields, models
from datetime import date,timedelta

class DateTask(models.Model):
    _name = "date.task"
    _description = "Date Task"

    name = fields.Char(string = "Name")
    date = fields.Date(string = "Date",compute="generate_date",readonly=False)
    number_of_days = fields.Integer(string = "Enter Number")

    @api.onchange('number_of_days')
    def generate_date(self):
        cnt=0
        flag=1
        for i in range(self.number_of_days+2):
            current_date=date.today()-timedelta(days=i+1)
            # print("_______current date",current_date)
            print("____________day number",current_date.weekday())
            if current_date.weekday()==5 or current_date.weekday()==6:
                cnt+=1
            else:
                flag+=1
        print("flag___________before",flag)
        flag+=cnt
        print("flag___________after",flag)
        print("flag___________cnt",cnt)
        print("The date Including Working Days Is",date.today()-timedelta(days=flag))
        self.date = date.today()-timedelta(days=flag)






        #     current_date = date.today() 
        #     required_date=current_date - timedelta(days=self.number_of_days) 

        # print("_____________________________________0897",required_date)