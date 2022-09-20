import cProfile
import profile

cp = cProfile.Profile()
cp.enable()


@profile
def write_sorted_letters(nb_letters=10**7):
    return nb_letters


write_sorted_letters()

cp.disable()
cp.print_stats()


