from pyscript import document



classmatesNames = [
    'Andrian Joseph Abayon',
    'Erin Gayla Antes',
    'Caitlyn Apostol',
    'Kyla Limuelle Banaag',
    'Oscar Robert Barrientos',
    'Clarisse Casal',
    'Thomas Taylor Coeli',
    'Ivan David',
    'Aurelia De Mata',
    'Franzeska Dela Cruz',
    'Jalena Rhein Dela Cruz',
    'Keisha May Dellejero',
    'Hikari Fukuda',
    'Ashley Gozum',
    'Juanico Ibay',
    'Angela Bridget Lim',
    'Ma. Jullie Ann Lozano',
    'James Mamauag',
    'Maria Sofia Navarro',
    'Yciar Precones',
    'Gino Benedict Ramos',
    'Gurnoor Sidhu',
    'Julia Isabel Tiu',
    'Erich Villamayor',
    'Annika Zaragoza',
]


def showPlayerlist(event):
    document.getElementById('playerlist').innerHTML = " "
    for name in classmatesNames:
        nameElement = "<p class='player_list_name'>" + name + "</p>"
        document.getElementById('playerlist').innerHTML += nameElement


    return