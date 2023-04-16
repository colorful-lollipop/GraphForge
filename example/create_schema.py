from GraphForge.KnowledgeGraph import Creator, Type

kg = Creator('音乐知识图谱1')
kg.add_entity_type('人', {
    '名字': Type.STRING,
    '出生地': Type.STRING,
    '国籍': Type.STRING,
})
kg.add_entity_type('音乐')
kg.add_entity_type('专辑')
kg.add_entity_type('年份', Type.INT)
kg.add_relation_type(['人', '演唱', '音乐'])
kg.add_relation_type(['音乐', '所属专辑', '专辑'])
kg.add_relation_type(['人', '作词', '音乐'])
kg.add_relation_type(['人', '作曲', '音乐'])
kg.add_relation_type(['人', '谱曲', '音乐'])
kg.add_relation_type(['音乐', '发行于', '年份'])
kg.create()
