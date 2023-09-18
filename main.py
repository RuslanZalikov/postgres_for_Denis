import psycopg2
import json
from config import *

def get_trb():

    try:
        connection = psycopg2.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=db_name
        )
        print("Мы внутри OK")

        with connection.cursor() as cur:
            cur.execute(
                """
                select transcription
                from ats_organisation_workspace_audio
                where ats_organisation_workspace_audio.transcription is not null;
                """
            )
            data = cur.fetchall()
        print("Без ошибок OK")
        for index, value in enumerate(data[:500]):
            with open(f"./files/file_{index}.json", "w", encoding="utf-8") as file:
                json.dump(value, file, ensure_ascii=False)

    except Exception as e:
        print("Badabum beda ERROR", e)

    finally:
        if connection:
            connection.close()
            print("Закрылись OK")

if __name__ == "__main__":
    print(get_trb())