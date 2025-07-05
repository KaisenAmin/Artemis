from src.parser import Artemis_ArgParser 


if __name__ == "__main__":
    try:
        parser = Artemis_ArgParser()
        parser.run()

    except Exception as err:
        print(err)

    


