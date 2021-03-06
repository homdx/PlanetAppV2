# distutils: language = c
# distutils: sources = planet.c

cdef extern from "planet.h":
    ctypedef struct Planet:
        double pos_x, pos_y, vel_x, vel_y, mass, density, radius
        int fixed
        int index

    ctypedef struct PlanetKeeper:
        int *planets[1000]
        int maxindex

    PlanetKeeper* create_planetkeeper()

    void free_planetkeeper(PlanetKeeper *planetkeeper)

    int create_planet(PlanetKeeper *planetkeeper, double pos_x, double pos_y, double vel_x, double vel_y, double mass, double density)

    void delete_planet(PlanetKeeper *planetkeeper, int index)

    double get_planet_mass(PlanetKeeper *planetkeeper, int index)
    void set_planet_mass(PlanetKeeper *planetkeeper, int index, double mass)

    double get_planet_density(PlanetKeeper *planetkeeper, int index)
    void set_planet_density(PlanetKeeper *planetkeeper, int index, double density)

    double get_planet_radius(PlanetKeeper *planetkeeper, int index)
    void set_planet_radius(PlanetKeeper *planetkeeper, int index, double radius)

    double get_planet_pos_x(PlanetKeeper *planetkeeper, int index)
    double get_planet_pos_y(PlanetKeeper *planetkeeper, int index)

    double get_planet_vel_x(PlanetKeeper *planetkeeper, int index)
    double get_planet_vel_y(PlanetKeeper *planetkeeper, int index)

    double calc_third_root(PlanetKeeper *planetkeeper, double value)
    double calc_root(PlanetKeeper *planetkeeper, double value)
    double calc_force(PlanetKeeper *planetkeeper, int index1, int index2, double dist)
    void fix_planet(PlanetKeeper *planetkeeper, int index)
    void unfix_planet(PlanetKeeper *planetkeeper, int index)

    void tick(PlanetKeeper *planetkeeper, double ratio)

    int planet_exists(PlanetKeeper *planetkeeper, int index)

cdef class CPlanetKeeper:

    cdef PlanetKeeper *planetkeeper

    def __cinit__(self):
        self.planetkeeper = create_planetkeeper()

    def __dealloc__(self):
        free_planetkeeper(self.planetkeeper)

    def create_planet(self, double pos_x, double pos_y, double vel_x, double vel_y, double mass, double density):
        return create_planet(self.planetkeeper, pos_x, pos_y, vel_x, vel_y, mass, density)

    def delete_planet(self, int index):
        delete_planet(self.planetkeeper, index)

    def get_planet_mass(self, int index):
        return get_planet_mass(self.planetkeeper, index)

    def set_planet_mass(self, int index, double mass):
        set_planet_mass(self.planetkeeper, index, mass)

    def get_planet_density(self, int index):
        return get_planet_density(self.planetkeeper, index)

    def set_planet_density(self, int index, double density):
        set_planet_density(self.planetkeeper, index, density)

    def get_planet_radius(self, int index):
        return get_planet_radius(self.planetkeeper, index)

    def set_planet_radius(self, int index, double radius):
        set_planet_radius(self.planetkeeper, index, radius)

    def get_planet_pos_x(self, int index):
        return get_planet_pos_x(self.planetkeeper, index)

    def get_planet_pos_y(self, int index):
        return get_planet_pos_y(self.planetkeeper, index)

    def get_planet_vel_x(self, int index):
        return get_planet_vel_x(self.planetkeeper, index)

    def get_planet_vel_y(self, int index):
        return get_planet_vel_y(self.planetkeeper, index)

    def calc_third_root(self, double value):
        return calc_third_root(self.planetkeeper, value)

    def calc_root(self, double value):
        return calc_root(self.planetkeeper, value)

    def calc_force(self, int index1, int index2, double dist):
        return calc_force(self.planetkeeper, index1, index2, dist)

    def fix_planet(self, int index):
        fix_planet(self.planetkeeper, index)

    def unfix_planet(self, int index):
        unfix_planet(self.planetkeeper, index)

    def tick(self, double ratio):
        tick(self.planetkeeper, ratio)

    def planet_exists(self, int index):
        return planet_exists(self.planetkeeper, index)
