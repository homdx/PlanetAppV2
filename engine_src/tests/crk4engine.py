# requires cplanet build in this directory
from crk4engine import CRk4Engine
import unittest
import time


class CPlanetTests(unittest.TestCase):

    def setUp(self):
        self.keeper = CRk4Engine()

    def tearDown(self):
        del self.keeper

    def test_basic(self):
        '''
        very simple test to see if index is returned
        '''
        pos = (0, 0)
        vel = (0, 0)
        mass = 1
        density = 1
        newindex = self.keeper.create_planet(
            pos_x=pos[0],
            pos_y=pos[1],
            vel_x=vel[0],
            vel_y=vel[1],
            mass=mass,
            density=density
        )
        self.assertEqual(newindex, 0)

    def test_multi(self):
        '''
        check for body limit of 1000
        '''
        for index in xrange(1000):
            pos = (index, index)
            vel = (index, index)
            mass = index
            density = index
            newindex = self.keeper.create_planet(
                pos_x=pos[0],
                pos_y=pos[1],
                vel_x=vel[0],
                vel_y=vel[1],
                mass=mass,
                density=density
            )
        self.assertEqual(newindex, 999)
        newindex = self.keeper.create_planet(
            pos_x=pos[0],
            pos_y=pos[1],
            vel_x=vel[0],
            vel_y=vel[1],
            mass=mass,
            density=density
        )
        self.assertEqual(newindex, -1)

    def test_load(self):
        '''
        simple load test to measure engine improvements
        '''
        for _ in xrange(100):
            for index in xrange(1000):
                newindex = self.keeper.create_planet(
                    pos_x=index,
                    pos_y=index,
                    vel_x=index,
                    vel_y=index,
                    mass=index + 1,
                    density=index + 1
                )
            tick_start = time.time()
            self.keeper.tick(1)
            tick_took = time.time() - tick_start
            print('Tick %s/100 took %s seconds' % (_ + 1, round(tick_took, 3)))


if __name__ == '__main__':
    unittest.main()
