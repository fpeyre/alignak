#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2015-2015: Alignak team, see AUTHORS.txt file for contributors
#
# This file is part of Alignak.
#
# Alignak is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Alignak is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Alignak.  If not, see <http://www.gnu.org/licenses/>.
#
#
# This file incorporates work covered by the following copyright and
# permission notice:
#
#  Copyright (C) 2009-2010:
#     Jean Gabes, naparuba@gmail.com

#  This file is part of Shinken.
#
#  Shinken is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Affero General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Shinken is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Affero General Public License for more details.
#
#  You should have received a copy of the GNU Affero General Public License
#  along with Shinken.  If not, see <http://www.gnu.org/licenses/>.

#
# This file is used to test reading and processing of config files
#

from alignak_test import *


class TestConfig(AlignakTest):

    def setUp(self):
        self.setup_with_file(['etc/alignak_groups_pickle.cfg'])

    def test_dispatch(self):
        
        
        sub_confs = self.conf.confs
        print "NB SUB CONFS", len(sub_confs)
        
        vcfg = None
        # Find where hr1 is
        for cfg in sub_confs.values():
            if 'HR1' in [h.get_name() for h in cfg.hosts]:
                print 'FOUNCED', len(cfg.hosts)
                vcfg = cfg
                

        # Look ifthe hg in the conf is valid
        vhg = vcfg.hostgroups.find_by_name('everyone')
        self.assert_(len(vhg.members) == 1)
        
        hr1 = [h for h in vcfg.hosts if h.get_name() == "HR1"][0]
        print hr1.hostgroups
        hg1 = None
        for hg in hr1.hostgroups:
            if vcfg.hostgroups[hg].get_name() == 'everyone':
                hg1 = vcfg.hostgroups[hg]


                
        print "Founded hostgroup", hg1
        print 'There should be only one host there'
        self.assert_(len(hg1.members) == 1)
        print 'and should be the same than the vcfg one!'
        self.assert_(hg1 == vhg)


if __name__ == '__main__':
    unittest.main()
