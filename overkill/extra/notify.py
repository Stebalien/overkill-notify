##
#    This file is part of Overkill-notify.
#
#    Overkill-notify is free software: you can redistribute it and/or modify it
#    under the terms of the GNU General Public License as published by the Free
#    Software Foundation, either version 3 of the License, or (at your option)
#    any later version.
#
#    Overkill-notify is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
#    or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#    for more details.
#
#    You should have received a copy of the GNU General Public License along
#    with Overkill-notify.  If not, see <http://www.gnu.org/licenses/>.
##

import notify2

class Notify:
    summary = ""
    message = None

    def __init__(self):
        notify2.init('Stuff')
        self.notification = notify2.Notification(self.summary)

    def show(self):
        self.notification.update(self.summary, self.message)
        self.notification.show()

