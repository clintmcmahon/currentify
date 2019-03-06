import thecurrent
import pytz, datetime
from datetime import timedelta
###
### An example script that is run every Thursday night to pull down the latest Transmission On The Radio show from The Current
###
if __name__ == '__main__':

    #Get the date this is being run
    #now = datetime.datetime.now()
    now = datetime.date(2019, 3, 3)

    #The Local Show starts at 6 PM Central Time
    start_date = now.strftime("%Y-%m-%dT18:00:00")

    #The Local Show ends at 8 PM Central Time
    end_date = now.strftime("%Y-%m-%dT19:00:00")

    name = "The Local Show On The Current"
    description = "Andrea Swensson's latest Sunday Night Local Show on The Current. Spinning all the best from Minnesota's local music scene, both past and present. Updated every Sunday night. Support the music @ TheCurrent.org "
    args = [name,start_date, end_date, description]
    thecurrent.main(args)