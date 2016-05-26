# The contents of this file are subject to the Common Public Attribution
# License Version 1.0. (the "License"); you may not use this file except in
# compliance with the License. You may obtain a copy of the License at
# http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
# License Version 1.1, but Sections 14 and 15 have been added to cover use of
# software over a computer network and provide for limited attribution for the
# Original Developer. In addition, Exhibit A has been modified to be consistent
# with Exhibit B.
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
# the specific language governing rights and limitations under the License.
#
# The Original Code is reddit.
#
# The Original Developer is the Initial Developer.  The Initial Developer of
# the Original Code is reddit Inc.
#
# All portions of the code written by reddit are Copyright (c) 2006-2015 reddit
# Inc. All Rights Reserved.
###############################################################################

from __future__ import absolute_import

import random, string

from Captcha.Base import randomIdentifier
from Captcha.Visual import Text, Backgrounds, Distortions, ImageCaptcha

IDEN_LENGTH = 32
SOL_LENGTH = 6

class RandCaptcha(ImageCaptcha):
    defaultSize = (120, 50)
    fontFactory = Text.FontFactory(18, "vera/VeraBd.ttf")

    def getLayers(self, solution="blah"):
        self.addSolution(solution)
        return ((Backgrounds.Grid(size=8, foreground="white"),
                 Distortions.SineWarp(amplitudeRange=(5,9))),
                (Text.TextLayer(solution,
                               textColor = 'white',
                               fontFactory = self.fontFactory),
                 Distortions.SineWarp()))

def make_solution():
    return randomIdentifier(alphabet=string.ascii_letters, length = SOL_LENGTH).upper()

def get_image():
    solution = make_solution()
    return RandCaptcha(solution=solution).render(), solution

def main():
	image,solution = get_image()
	f = "%s.png"%solution
	image.save(f, "PNG")
	return 0
    
if __name__ == "__main__":
	main()
        