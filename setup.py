from distutils.core import setup
setup(
  name = 'periodify_pdb',         # How you named your package folder (MyLib)
  packages = ['periodify_pdb'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A package that places a pdb structure into a periodic box',   # Give a short description about your library
  author = 'Brandon Mendoza',                   # Type in your name
  author_email = 'brandonamendoza@icloud.com',      # Type in your E-Mail
  url = 'https://github.com/brandonamendoza/periodify_pdb',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/brandonamendoza/periodify_pdb/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['pdb', 'periodic', 'file prep'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'openmm',
          'MDAnalysis'
      ],
)
