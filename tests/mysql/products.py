expectations = [
    {"set": {"sql_mode": "no_auto_value_on_zero"}},
    {"start_transaction": {}},
    {"set": {"time_zone": "+00:00"}},
    None,
    None,
    None,
    None,
    {"drop": {"if_exists": True, "table": "product"}},
    {"create table": {
        "replace": False,
        "name": "product",
        "columns": [
            {"name": "prod_id", "type": {"int": {}}, "nullable": False, "auto_increment": True},
            {"name": "prod_no", "type": {"int": {}}, "default": {"null": {}}},
            {"name": "prod_vat", "type": {"unsigned": True, "int": {}}, "default": {"null": {}}},
            {"name": "prod_lfdnr", "type": {"unsigned": True, "smallint": {}}, "nullable": False},
            {"name": "prod_description", "type": "longtext"},
            {"name": "prod_match", "type": {"char": 10}, "nullable": False},
            {"name": "prod_active", "type": {"tinyint": 1}, "nullable": False, "default": {"literal": "1"}},
            {"name": "prod_foreign_items", "type": {"unsigned": True, "bigint": {}}, "default": {"literal": "0"}},
            {"name": "prod_created_date", "type": {"date": {}}, "nullable": False},
            {"name": "prod_created_time", "type": {"time": {}}, "nullable": False, "default": {"literal": "18:00:00"}},
            {"name": "prod_last_send", "type": {"datetime": {}}, "default": {"null": {}}},
            {
                "name": "prod_last_sold",
                "type": {"decimal": [16, 2]},
                "nullable": False,
                "default": {"literal": "0.00"},
            },
            {"name": "prod_timestamp", "type": {"timestamp": {}}, "nullable": True, "default": {"null": {}}},
            {"name": "prod_average_price", "type": {"double": [16, 3]}, "nullable": False},
            {"name": "prod_icon", "type": {"blob": {}}},
            {"name": "prod_image", "type": "longblob"},
            {
                "name": "prod_key",
                "type": {"varchar": 255},
                "collate": "utf8mb3_unicode_ci",
                "nullable": False,
                "default": {"literal": ""},
                "character_set": "utf8mb3",
            },
            {
                "name": "prod_type",
                "type": {"enum": [{"literal": "product"}, {"literal": "consumable"}, {"literal": "internal"}]},
                "character_set": "utf8mb3",
                "collate": "utf8mb3_unicode_ci",
                "nullable": False,
                "default": {"literal": "product"},
            },
            {
                "name": "prod_production",
                "type": {"set": [{"literal": "own production"}, {"literal": "purchased product"}]},
                "default": {"null": {}},
            },
            {
                "name": "prod_multilingual",
                "type": {"unsigned": True, "tinyint": {}},
                "nullable": False,
                "default": {"literal": "0"},
            },
        ],
        "constraint": [
            {"primary_key": {"columns": "prod_id"}},
            {"index": {"unique": True, "name": "prod_key", "columns": ["prod_key", "prod_type"]}},
            {"index": {"name": "artikelnr", "columns": "prod_no"}},
        ],
        "engine": "MyISAM",
        "auto_increment": 4,
        "default_charset": "utf8mb3",
    }},
    {
        "columns": [
            "prod_id",
            "prod_no",
            "prod_vat",
            "prod_lfdnr",
            "prod_description",
            "prod_match",
            "prod_active",
            "prod_foreign_items",
            "prod_created_date",
            "prod_created_time",
            "prod_last_send",
            "prod_last_sold",
            "prod_timestamp",
            "prod_average_price",
            "prod_icon",
            "prod_image",
            "prod_key",
            "prod_type",
            "prod_production",
            "prod_multilingual",
        ],
        "query": {"select": [
            {"value": 3},
            {"value": 1},
            {"value": 1},
            {"value": 1},
            {"value": {"literal": "TEST öäüÖÄÜß€@"}},
            {"value": {"literal": ""}},
            {"value": 1},
            {"value": 1},
            {"value": {"literal": "2023-12-17"}},
            {"value": {"literal": "18:00:00"}},
            {"value": {"literal": "2006-02-14 22:04:36"}},
            {"value": {"literal": "4.80"}},
            {"value": {"literal": "2023-12-17 21:46:31"}},
            {"value": 4.3},
            {"value": {"hex": "ff"}},
            {"value": {"hex": "ff"}},
            {"value": {"literal": "KEY"}},
            {"value": {"literal": "product"}},
            {"value": {"literal": "own production"}},
            {"value": 1},
        ]},
        "insert": "product",
    },
    {"commit":{}},
]
