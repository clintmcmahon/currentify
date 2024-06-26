import thecurrent
import datetime
from datetime import timedelta
###
# An example script that is run every Thursday night to pull down the latest Transmission On The Radio show from The Current
###
if __name__ == '__main__':

    # Get the date this is being run
    today = datetime.datetime.today().date()

    # Transmission starts at 10 PM Central Time
    start_date = today.strftime("%Y-%m-%dT22:00:00")

    # Transmission ends at 11 PM Central Time
    # Since we are only getting one hour worth of music, set the end date to the same as start date
    end_date = today.strftime("%Y-%m-%dT22:00:00")

    name = "Transmission On The Radio"
    description = "DJ Jake Rudh's latest Transmission On The Radio set. Updated every Thursday night. Support the music @ TheCurrent.org/donate."
    args = [name, start_date, end_date, description]
    thecurrent.main(args)
