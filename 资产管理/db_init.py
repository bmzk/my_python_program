port_line=[['D1',2]
]


def init(db:DB):
    # 创建 网线接口和 端口 对照表
    db.creat_table(_table='PORT',_str='ID INT PRIMARY KEY  NOT NULL , Line TEXT , PORT INT')

