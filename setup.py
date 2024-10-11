from distutils.core import setup
setup(
  name = 'oirFileReader',         # How you named your package folder (MyLib)
  packages = ['oirFileReader'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='GPLv3',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Read Olympus .oir image files in python',   # Give a short description about your library
  author = 'Dominik Schneidereit',                   # Type in your name
  author_email = 'dominik.schneidereit@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/sidoschn/oirFileReader',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/sidoschn/oirFileReader/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['Olympus', 'OIR', '.oir', 'reader'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'OSI Approved :: GNU General Public License v3 (GPLv3)',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
  ],
)