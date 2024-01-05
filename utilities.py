
def unos_intervala(min, max):
    while True:
        try:
            broj = int(input(f"Unesite cijeli broj u inervalu {min}-{max}: "))

            if broj<min or broj>max:
                raise Exception(f"Unesite broj unutar intervala {min}-{max}.")

        except ValueError:
            print('Unesli ste znak a ne cijeli broj.')
        except Exception as e:
            print(e)
        else:
            return broj