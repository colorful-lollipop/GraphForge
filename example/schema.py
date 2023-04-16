from GraphForge.schema import Entity, Relation

NAME_MAP: dict[str, str] = {
    'Music': '音乐',
    'name': '名字',
    "value": "值",
    'Human': '发行时间',

}


class Music(Entity):
    name: str


class Time(Entity):
    value: int


class Human(Entity):
    name: str
    birthday: str
    hometown: str


class Album(Entity):
    name: str


class Sing(Relation):  # 演唱
    _subject: Human
    _object: Music


class Write(Relation):  # 作词
    _subject: Human
    _object: Music


class Compose(Relation):  # 作曲
    _subject: Human
    _object: Music


class Arrange(Relation):  # 谱曲
    _subject: Human
    _object: Music


class PublishOn(Relation):
    _subject: Music
    _object: Time
