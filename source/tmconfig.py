class TMConfig:

    title = u"Cours d'introduction à la compression d'images"
    first_name = 'Romain'
    last_name = 'De Groote'
    author = f'{first_name} {last_name}'
    year = u'2022'
    month = u'April'
    seminary_title = u'Développement d’outils ou matériel d’enseignement de l’informatique'
    tutor = u"Cédric Donner"
    release = "Version finale"
    repository_url = "https://github.com/MatsuneMikuroi"

    @classmethod
    def date(cls):
        return cls.month + " " + cls.year

tmconfig = TMConfig()