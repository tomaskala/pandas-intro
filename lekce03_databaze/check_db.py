import argparse

try:
    import snowflake.connector
    from snowflake.connector import DatabaseError, ProgrammingError
except ImportError:
    print(">>> Neni nainstalovany snowflake connector.")
    print(">>> Napis do terminalu tohle a opakuj postup:")
    print("pip install snowflake-connector-python")
    exit(1)
except Exception as e:
    print(
        ">>> Nastala neocekavana chyba (1). Vezmi chybu nize a posli ji "
        "na czechichat."
    )
    print(e)
    exit(1)


DATABASE = "COURSES"
HOST = "https://ip68917.eu-west-1.snowflakecomputing.com/"
SCHEMA = "SCH_CZECHITA"
WAREHOUSE = "COMPUTE_WH"
ACCOUNT = "ip68917.eu-west-1"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--password", required=True)

    args = parser.parse_args()

    name = args.name
    password = args.password
    role = "ROLE_" + name.upper()

    try:
        conn = snowflake.connector.connect(
            user=name,
            password=password,
            account=ACCOUNT,
            warehouse=WAREHOUSE,
            database=DATABASE,
            schema=SCHEMA,
            role=role,
        )
    except DatabaseError as e:
        print(
            ">>> Nastala chyba pri pripojeni k databazi. Patrne spatne jmeno nebo heslo."
        )
        print(
            ">>> Podivej se na chybu, ktera se zobrazuje pod timhle textem. Pokud se tam "
            "pise, ze mas spatne jmeno nebo heslo, zadej spravne. Hint: pis oboji do "
            "uvozovek."
        )
        print(">>> Pokud se tam pise neco jineho, posli na tu chybu na czechichat.")
        print(e)
        exit(1)
    except Exception as e:
        print(
            ">>> Nastala neocekavana chyba (2). Vezmi chybu nize a posli ji "
            "na czechichat."
        )
        print(e)
        exit(1)

    with conn.cursor() as cursor:
        try:
            cursor.execute("SELECT current_version()")
            one_row = cursor.fetchone()
        except ProgrammingError as e:
            print(
                ">>> Chyba v SQL dotazu. To by se nemelo stat. Vezmi chybu nize "
                "a posli ji na czechichat."
            )
            print(e)
            exit(1)
        except Exception as e:
            print(
                ">>> Nastala neocekavana chyba (3). Vezmi chybu nize a posli ji "
                "na czechichat."
            )
            print(e)
            exit(1)
        else:
            print(">>> Vse v poradku!.")

    conn.close()


if __name__ == "__main__":
    main()
