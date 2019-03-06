import thecurrent
import pytz, datetime
from datetime import timedelta
###
### An example script that is run every Thursday night to pull down the latest Transmission On The Radio show from The Current
###
if __name__ == '__main__':

    #Get the date this is being run
    #now = datetime.datetime.now()
    now = datetime.date(2019, 2,28)
    #Transmission starts at 10 PM Central Time
    start_date = now.strftime("%Y-%m-%dT22:00:00")

    #Swingin doors ends at 11 PM Central Time
    #Since we are only getting one hour worth of music, set the end date to the same as start date
    end_date = start_date

    #name = "Transmission On The Radio"
    name = "Test Playlist"
    description = "Updated every Friday. Support the music and donate @ TheCurrent.org"
    args = [name,start_date, end_date, description]
    thecurrent.main(args)

