VERSION = "0.2.1"

TOOLS_SETTINGS_ARRAY = [
    {"name": "Режим добавления вершин", "side": "left",
     "icon": "resources/icons/add_vertex.png"},
    {"name": "Режим добавления рёбер", "side": "left",
     "icon": "resources/icons/add_edge.png"},
    {"name": "Режим добавления дуг", "side": "left",
     "icon": "resources/icons/add_edge_org.png"},
    {"name": "Режим расщепления вершиины", "side": "left",
     "icon": "resources/icons/dividing_vertex.png"},
    {"name": "Режим слияния вершиин", "side": "left",
     "icon": "resources/icons/merging_vertices.png"},
    ]

ABOUT_STRINGS = [
    "GraphHelper - Приложение для работы с графами, их \
    построения и выполнения ряда операций над ними.",
    "При создании использовались:\n•tkinter",
    "Звягин Сергей Алексеевич, студент группы КИ19-08б \
    Института космических и информациооных технологий \
    Сибирского федерального университета"
    ]

ALLOWED_CHARACTERS = ["\n", " ", "-", "0", "1", "2"]

MESSAGES = {
    "GREETING": "Создайте или загрузите граф",
    "WARNING_TOO_CLOSE": "Слишком близко к уже существующей вершине",
    "WARNING_CREATE": "Граф уже создан"
    }
