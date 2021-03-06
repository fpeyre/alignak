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
#  Copyright (C) 2009-2014:
#     Jean Gabes, naparuba@gmail.com
#     Hartmut Goebel, h.goebel@goebel-consult.de
#     Grégory Starck, g.starck@gmail.com
#     Sebastien Coavoux, s.coavoux@free.fr

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


class TestObjectsAndNotifWays(AlignakTest):
    def setUp(self):
        self.setup_with_file(['etc/alignak_objects_and_notifways.cfg'])

    # We got strange "objects" for some contacts property when we are using notif ways
    # and asking for  broks. Search why
    def test_dummy(self):
        c_normal = self.sched.contacts.find_by_name("test_contact")
        self.assertIsNot(c_normal, None)
        c_nw = self.sched.contacts.find_by_name("test_contact_nw")
        self.assertIsNot(c_nw, None)

        b = c_normal.get_initial_status_brok()
        b.prepare()
        print "B normal", b
        self.assertEqual([u'd', u'u', u'r', u'f', u's'], b.data['host_notification_options'])
        b2 = c_nw.get_initial_status_brok()
        b2.prepare()
        print "B nw", b2
        self.assertEqual([u''], b2.data['host_notification_options'])


if __name__ == '__main__':
    unittest.main()
