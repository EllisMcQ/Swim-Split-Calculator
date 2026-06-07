import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Race:

    def __init__(self, race_id, stroke, distance, course, date, total_time):
        self.race_id = race_id
        self.stroke = stroke
        self.distance = distance
        self.course = course
        self.date = date
        self.total_time = total_time
        self.splits = []  # list of dicts: {"distance": x, "segment_split": x, "cumulative_split": x}


    def save_race(self):
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
    
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO races (stroke, distance, pool, total_time, date) VALUES (%s, %s, %s, %s, %s) RETURNING race_id",
            (self.stroke, self.distance, self.course, self.total_time, self.date))
        self.race_id = cursor.fetchone()[0]

        for split in self.splits:
            cursor.execute(
                "INSERT INTO splits (race_id, segment_distance, segment_split, cumulative_split) VALUES (%s, %s, %s, %s)",
                (self.race_id, split["distance"], split["segment_split"], split["cumulative_split"])
            )

        connection.commit()
        cursor.close()
        connection.close()