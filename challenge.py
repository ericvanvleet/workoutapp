import time

class Challenge:
    def __init__(self, start_date, day_count, organizer):
        if day_count < 7 or day_count > 366:
            raise ChallengeValidationError("Challenge length must be between 7 and 366, you n00b.")
        self.start_date = time.strptime(start_date + " +00:00", "%Y-%m-%d %z")
        self.end_date = time.gmtime(time.mktime(self.start_date) + day_count * 24 * 60 * 60)
        self.organizer = organizer
    def validate(self):
        raise ChallengeValidationError("You fail")
    def get_start_date(self):
        return time.strftime("%Y-%m-%d", self.start_date)
    def get_end_date(self):
        return time.strftime("%Y-%m-%d", self.end_date)
        
class ChallengeValidationError(Exception):
    def __init__(self, message):
        self.message = message