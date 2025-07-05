import time
import uuid
import sqlite3

class Challenge:
    def __init__(self, id, start_date, day_count):
        if day_count < 7 or day_count > 366:
            raise ChallengeValidationError("Challenge length must be between 7 and 366, you n00b.")
        self.start_date = time.strptime(start_date + " +00:00", "%Y-%m-%d %z")
        self.end_date = time.gmtime(time.mktime(self.start_date) + day_count * 24 * 60 * 60)
        if id == None:
            self.id = uuid.uuid4()
        else: 
            self.id = id
        # self.organizer = organizer
    # def validate(self):
    #     raise ChallengeValidationError("You fail")
    @staticmethod
    def list():
        conn = sqlite3.connect("e30x.db")
        cursor = conn.execute('select * from challenge')
        results = cursor.fetchall()
        challenges = []
        for i in range(len(results)):
            result = results[i]
            id = result[0]
            start_date = time.strptime(result[1] + " +00:00", "%Y-%m-%d %z")
            end_date = time.strptime(result[2] + " +00:00", "%Y-%m-%d %z")
            day_count = (time.mktime(end_date) - time.mktime(start_date)) / (24 * 60 * 60)
            challenges.append(Challenge(id, result[1], day_count))
        conn.commit()
        conn.close()
        return challenges
    def save(self):
        conn = sqlite3.connect("e30x.db")

        conn.execute(
            """
                insert into challenge
                values(?, ?, ?)
            """, 
            (self.get_id(), self.get_start_date(), self.get_end_date())
        )
        conn.commit()
        conn.close()

    def get_id(self):
        return str(self.id)

    def get_start_date(self):
        return time.strftime("%Y-%m-%d", self.start_date)
    
    def get_end_date(self):
        return time.strftime("%Y-%m-%d", self.end_date)
        
class ChallengeValidationError(Exception):
    def __init__(self, message):
        self.message = message
