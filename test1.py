import cProfile
cp = cProfile.Profile()
cp.enable()

cp.disable()
cp.print_stats()


