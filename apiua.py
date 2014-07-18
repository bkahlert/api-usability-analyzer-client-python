#!/usr/bin/env python

# Python based data collection client for the API Usability Analyzer Server
# Copyright (c) 2014 Björn Kahlert
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import os
import webbrowser
from bkahlert import DiffCollector

def main():
    # sys.argv[1]: event name
    # sys.argv[2]: build directory (e.g. ./build/Debug)
    # sys.argv[3]: directory to be observed (typically the source directory ./src)
    diffCollector = DiffCollector(sys.argv[2], sys.argv[3])
    id = diffCollector.getID().get()
    url = "https://your.server/APIUAsrv/static/register.html?SUAid=" + id
        
    # inital run
    if(sys.argv[1] == "init"):
        diffCollector.prepare()
        print("---- ID: " + id)
        print("---- DATA: " + diffCollector.userdata_dir)
        
        # register ID if never happened before
        if(diffCollector.getID().isLinked()):
            #print("---- Your ID has been linked on "
            #    + diffCollector.getID().getLinkedDate().strftime("%Y-%m-%d %H:%M:%S")
            #    + ". You can always refresh your link by opening\n       " + url)
            sys.path
        else:
            if(not webbrowser.open(url=url, new=2)):
                print("\n\n")
                print("  Please register your ID:")
                print("  ------------------------")
                print("  1) Open your favorite browser")
                print("  2) Enter the following website:\n")
                print("     >>>   " + url + "   <<<\n")
                print("  3) Press ENTER when you have finished to continue ...")
                print("\n\n")
                raw_input("")
            diffCollector.getID().link()
        
        diffCollector.build()
        return 0

    # build (only called no matter how many target need to be rebuild)
    if(sys.argv[1] == "build"):
        diffCollector.prepare()
        diffCollector.build()
        return 0

    return 0

if __name__ == '__main__':
    sys.exit(main())
    