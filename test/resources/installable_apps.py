"""INSTALLABLE_APPS"""
from projector_installer.products import Product, IDEKind

INSTALLABLE_APPS = \
    [Product('IntelliJ IDEA Community 2019.3.4',
             'https://download.jetbrains.com/idea/ideaIC-2019.3.4.tar.gz',
             IDEKind.Idea_Community),
     Product('IntelliJ IDEA Community 2020.1.1',
             'https://download.jetbrains.com/idea/ideaIC-2020.1.1.tar.gz',
             IDEKind.Idea_Community),
     Product('IntelliJ IDEA Community 2020.2',
             'https://download.jetbrains.com/idea/ideaIC-2020.2.tar.gz',
             IDEKind.Idea_Community),
     Product('IntelliJ IDEA Community 2020.3.2',
             'https://download.jetbrains.com/idea/ideaIC-2020.3.2.tar.gz',
             IDEKind.Idea_Community),
     Product('IntelliJ IDEA Ultimate 2019.3.4',
             'https://download.jetbrains.com/idea/ideaIU-2019.3.4.tar.gz',
             IDEKind.Idea_Ultimate),
     Product('IntelliJ IDEA Ultimate 2020.2',
             'https://download.jetbrains.com/idea/ideaIU-2020.2.tar.gz',
             IDEKind.Idea_Ultimate),
     Product('IntelliJ IDEA Ultimate 2020.3.2',
             'https://download.jetbrains.com/idea/ideaIU-2020.3.2.tar.gz',
             IDEKind.Idea_Ultimate),
     Product('CLion 2019.3.5',
             'https://download.jetbrains.com/cpp/CLion-2019.3.5.tar.gz',
             IDEKind.CLion),
     Product('CLion 2020.2',
             'https://download.jetbrains.com/cpp/CLion-2020.2.tar.gz',
             IDEKind.CLion),
     Product('CLion 2020.3.2',
             'https://download.jetbrains.com/cpp/CLion-2020.3.2.tar.gz',
             IDEKind.CLion),
     Product('GoLand 2019.3.4',
             'https://download.jetbrains.com/go/goland-2019.3.4.tar.gz',
             IDEKind.GoLand),
     Product('GoLand 2020.2.2',
             'https://download.jetbrains.com/go/goland-2020.2.2.tar.gz',
             IDEKind.GoLand),
     Product('GoLand 2020.3.2',
             'https://download.jetbrains.com/go/goland-2020.3.2.tar.gz',
             IDEKind.GoLand),
     Product('DataGrip 2019.3.4',
             'https://download.jetbrains.com/datagrip/datagrip-2019.3.4.tar.gz',
             IDEKind.DataGrip),
     Product('DataGrip 2020.2',
             'https://download.jetbrains.com/datagrip/datagrip-2020.2.tar.gz',
             IDEKind.DataGrip),
     Product('DataGrip 2020.3.2',
             'https://download.jetbrains.com/datagrip/datagrip-2020.3.2.tar.gz',
             IDEKind.DataGrip),
     Product('PhpStorm 2019.3.4',
             'https://download.jetbrains.com/webide/PhpStorm-2019.3.4.tar.gz',
             IDEKind.PhpStorm),
     Product('PhpStorm 2020.2',
             'https://download.jetbrains.com/webide/PhpStorm-2020.2.tar.gz',
             IDEKind.PhpStorm),
     Product('PhpStorm 2020.3.2',
             'https://download.jetbrains.com/webide/PhpStorm-2020.3.2.tar.gz',
             IDEKind.PhpStorm),
     Product('PyCharm Community 2019.3.4',
             'https://download.jetbrains.com/python/pycharm-community-2019.3.4.tar.gz',
             IDEKind.PyCharm_Community),
     Product('PyCharm Community 2020.2',
             'https://download.jetbrains.com/python/pycharm-community-2020.2.tar.gz',
             IDEKind.PyCharm_Community),
     Product('PyCharm Community 2020.3.3',
             'https://download.jetbrains.com/python/pycharm-community-2020.3.3.tar.gz',
             IDEKind.PyCharm_Community),
     Product('PyCharm Professional 2019.3.4',
             'https://download.jetbrains.com/python/pycharm-professional-2019.3.4.tar.gz',
             IDEKind.PyCharm_Professional),
     Product('PyCharm Professional 2020.2',
             'https://download.jetbrains.com/python/pycharm-professional-2020.2.tar.gz',
             IDEKind.PyCharm_Professional),
     Product('PyCharm Professional 2020.3.3',
             'https://download.jetbrains.com/python/pycharm-professional-2020.3.3.tar.gz',
             IDEKind.PyCharm_Professional),
     Product('RubyMine 2020.3.2',
             'https://download.jetbrains.com/ruby/RubyMine-2020.3.2.tar.gz',
             IDEKind.RubyMine),
     Product('WebStorm 2020.3.2',
             'https://download.jetbrains.com/webstorm/WebStorm-2020.3.2.tar.gz',
             IDEKind.WebStorm),
     Product('Rider 2020.3.3',
             'https://download.jetbrains.com/rider/JetBrains.Rider-2020.3.3.tar.gz',
             IDEKind.Rider),
     Product('DataSpell EAP 2021.1',
             'https://download.jetbrains.com/python/jetbrains-data-spell-212.443.21.tar.gz',
             IDEKind.DataSpell),
     Product('MPS 2020.3',
             'https://download.jetbrains.com/mps/2020.3/MPS-2020.3.3.tar.gz',
             IDEKind.MPS)]