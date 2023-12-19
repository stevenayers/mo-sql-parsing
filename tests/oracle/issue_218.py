expectations = [
    {"set": {"names": "utf8mb4"}},
    {"set": [{"@old_unique_checks": "@@unique_checks"}, {"unique_checks": 0}]},
    {"set": [{"@old_foreign_key_checks": "@@foreign_key_checks"}, {"foreign_key_checks": 0}]},
    {"set": [{"@old_sql_mode": "@@sql_mode"}, {"sql_mode": {"literal": "TRADITIONAL"}}]},
    {"drop": {"schema": "sakila", "if_exists": True}},
    {"create_schema": {"name": "sakila"}},
    {"use": "sakila"},
    {"create table": {
        "columns": [
            {
                "auto_increment": True,
                "name": "actor_id",
                "nullable": False,
                "type": {"smallint": {}, "unsigned": True},
            },
            {"name": "first_name", "nullable": False, "type": {"varchar": 45}},
            {"name": "last_name", "nullable": False, "type": {"varchar": 45}},
            {
                "default": "CURRENT_TIMESTAMP",
                "name": "last_update",
                "nullable": False,
                "on_update": "CURRENT_TIMESTAMP",
                "type": {"timestamp": {}},
            },
        ],
        "constraint": [
            {"primary_key": {"columns": "actor_id"}},
            {"index": {"columns": "last_name", "name": "idx_actor_last_name"}},
        ],
        "default_charset": "utf8mb4",
        "engine": "InnoDB",
        "name": "actor",
        "replace": False,
    }},
    {"create table": {
        "columns": [
            {
                "auto_increment": True,
                "name": "address_id",
                "nullable": False,
                "type": {"smallint": {}, "unsigned": True},
            },
            {"name": "address", "nullable": False, "type": {"varchar": 50}},
            {"default": {"null": {}}, "name": "address2", "type": {"varchar": 50}},
            {"name": "district", "nullable": False, "type": {"varchar": 20}},
            {"name": "city_id", "nullable": False, "type": {"smallint": {}, "unsigned": True}},
            {"default": {"null": {}}, "name": "postal_code", "type": {"varchar": 10}},
            {"name": "phone", "nullable": False, "type": {"varchar": 20}},
            {
                "default": "CURRENT_TIMESTAMP",
                "name": "last_update",
                "nullable": False,
                "on_update": "CURRENT_TIMESTAMP",
                "type": {"timestamp": {}},
            },
        ],
        "constraint": [
            {"primary_key": {"columns": "address_id"}},
            {"index": {"columns": "city_id", "name": "idx_fk_city_id"}},
            {
                "foreign_key": {
                    "columns": "city_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "city_id", "table": "city"},
                },
                "name": "fk_address_city",
            },
        ],
        "default_charset": "utf8mb4",
        "engine": "InnoDB",
        "name": "address",
    }},
    {"create table": {
        "columns": [
            {
                "auto_increment": True,
                "name": "category_id",
                "nullable": False,
                "type": {"tinyint": {}, "unsigned": True},
            },
            {"name": "name", "nullable": False, "type": {"varchar": 25}},
            {
                "default": "CURRENT_TIMESTAMP",
                "name": "last_update",
                "nullable": False,
                "on_update": "CURRENT_TIMESTAMP",
                "type": {"timestamp": {}},
            },
        ],
        "constraint": {"primary_key": {"columns": "category_id"}},
        "default_charset": "utf8mb4",
        "engine": "InnoDB",
        "name": "category",
    }},
    {"create table": {
        "columns": [
            {"auto_increment": True, "name": "city_id", "nullable": False, "type": {"smallint": {}, "unsigned": True}},
            {"name": "city", "nullable": False, "type": {"varchar": 50}},
            {"name": "country_id", "nullable": False, "type": {"smallint": {}, "unsigned": True}},
            {
                "default": "CURRENT_TIMESTAMP",
                "name": "last_update",
                "nullable": False,
                "on_update": "CURRENT_TIMESTAMP",
                "type": {"timestamp": {}},
            },
        ],
        "constraint": [
            {"primary_key": {"columns": "city_id"}},
            {"index": {"columns": "country_id", "name": "idx_fk_country_id"}},
            {
                "foreign_key": {
                    "columns": "country_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "country_id", "table": "country"},
                },
                "name": "fk_city_country",
            },
        ],
        "default_charset": "utf8mb4",
        "engine": "InnoDB",
        "name": "city",
    }},
    {"create table": {
        "columns": [
            {
                "auto_increment": True,
                "name": "country_id",
                "nullable": False,
                "type": {"smallint": {}, "unsigned": True},
            },
            {"name": "country", "nullable": False, "type": {"varchar": 50}},
            {
                "default": "CURRENT_TIMESTAMP",
                "name": "last_update",
                "nullable": False,
                "on_update": "CURRENT_TIMESTAMP",
                "type": {"timestamp": {}},
            },
        ],
        "constraint": {"primary_key": {"columns": "country_id"}},
        "default_charset": "utf8mb4",
        "engine": "InnoDB",
        "name": "country",
    }},
    {"create table": {
        "columns": [
            {
                "auto_increment": True,
                "name": "customer_id",
                "nullable": False,
                "type": {"smallint": {}, "unsigned": True},
            },
            {"name": "store_id", "nullable": False, "type": {"tinyint": {}, "unsigned": True}},
            {"name": "first_name", "nullable": False, "type": {"varchar": 45}},
            {"name": "last_name", "nullable": False, "type": {"varchar": 45}},
            {"default": {"null": {}}, "name": "email", "type": {"varchar": 50}},
            {"name": "address_id", "nullable": False, "type": {"smallint": {}, "unsigned": True}},
            {"default": True, "name": "active", "nullable": False, "type": {"boolean": {}}},
            {"name": "create_date", "nullable": False, "type": {"datetime": {}}},
            {
                "default": "CURRENT_TIMESTAMP",
                "name": "last_update",
                "on_update": "CURRENT_TIMESTAMP",
                "type": {"timestamp": {}},
            },
        ],
        "constraint": [
            {"primary_key": {"columns": "customer_id"}},
            {"index": {"columns": "store_id", "name": "idx_fk_store_id"}},
            {"index": {"columns": "address_id", "name": "idx_fk_address_id"}},
            {"index": {"columns": "last_name", "name": "idx_last_name"}},
            {
                "foreign_key": {
                    "columns": "address_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "address_id", "table": "address"},
                },
                "name": "fk_customer_address",
            },
            {
                "foreign_key": {
                    "columns": "store_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "store_id", "table": "store"},
                },
                "name": "fk_customer_store",
            },
        ],
        "default_charset": "utf8mb4",
        "engine": "InnoDB",
        "name": "customer",
    }},
    {"create table": {
        "columns": [
            {"auto_increment": True, "name": "film_id", "nullable": False, "type": {"smallint": {}, "unsigned": True}},
            {"name": "title", "nullable": False, "type": {"varchar": 128}},
            {"default": {"null": {}}, "name": "description", "type": {"text": {}}},
            {"default": {"null": {}}, "name": "release_year", "type": "YEAR"},
            {"name": "language_id", "nullable": False, "type": {"tinyint": {}, "unsigned": True}},
            {"default": {"null": {}}, "name": "original_language_id", "type": {"tinyint": {}, "unsigned": True}},
            {"default": 3, "name": "rental_duration", "nullable": False, "type": {"tinyint": {}, "unsigned": True}},
            {"default": 4.99, "name": "rental_rate", "nullable": False, "type": {"decimal": [4, 2]}},
            {"default": {"null": {}}, "name": "length", "type": {"smallint": {}, "unsigned": True}},
            {"default": 19.99, "name": "replacement_cost", "nullable": False, "type": {"decimal": [5, 2]}},
            {
                "default": {"literal": "G"},
                "name": "rating",
                "type": {"enum": [
                    {"literal": "G"},
                    {"literal": "PG"},
                    {"literal": "PG-13"},
                    {"literal": "R"},
                    {"literal": "NC-17"},
                ]},
            },
            {
                "default": {"null": {}},
                "name": "special_features",
                "type": {"set": [
                    {"literal": "Trailers"},
                    {"literal": "Commentaries"},
                    {"literal": "Deleted Scenes"},
                    {"literal": "Behind the Scenes"},
                ]},
            },
            {
                "default": "CURRENT_TIMESTAMP",
                "name": "last_update",
                "nullable": False,
                "on_update": "CURRENT_TIMESTAMP",
                "type": {"timestamp": {}},
            },
        ],
        "constraint": [
            {"primary_key": {"columns": "film_id"}},
            {"index": {"columns": "title", "name": "idx_title"}},
            {"index": {"columns": "language_id", "name": "idx_fk_language_id"}},
            {"index": {"columns": "original_language_id", "name": "idx_fk_original_language_id"}},
            {
                "foreign_key": {
                    "columns": "language_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "language_id", "table": "language"},
                },
                "name": "fk_film_language",
            },
            {
                "foreign_key": {
                    "columns": "original_language_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "language_id", "table": "language"},
                },
                "name": "fk_film_language_original",
            },
        ],
        "default_charset": "utf8mb4",
        "engine": "InnoDB",
        "name": "film",
    }},
    {"create table": {
        "columns": [
            {"name": "actor_id", "nullable": False, "type": {"smallint": {}, "unsigned": True}},
            {"name": "film_id", "nullable": False, "type": {"smallint": {}, "unsigned": True}},
            {
                "default": "CURRENT_TIMESTAMP",
                "name": "last_update",
                "nullable": False,
                "on_update": "CURRENT_TIMESTAMP",
                "type": {"timestamp": {}},
            },
        ],
        "constraint": [
            {"primary_key": {"columns": ["actor_id", "film_id"]}},
            {"index": {"columns": "film_id", "name": "idx_fk_film_id"}},
            {
                "foreign_key": {
                    "columns": "actor_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "actor_id", "table": "actor"},
                },
                "name": "fk_film_actor_actor",
            },
            {
                "foreign_key": {
                    "columns": "film_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "film_id", "table": "film"},
                },
                "name": "fk_film_actor_film",
            },
        ],
        "default_charset": "utf8mb4",
        "engine": "InnoDB",
        "name": "film_actor",
    }},
    {"create table": {
        "columns": [
            {"name": "film_id", "nullable": False, "type": {"smallint": {}, "unsigned": True}},
            {"name": "category_id", "nullable": False, "type": {"tinyint": {}, "unsigned": True}},
            {
                "default": "CURRENT_TIMESTAMP",
                "name": "last_update",
                "nullable": False,
                "on_update": "CURRENT_TIMESTAMP",
                "type": {"timestamp": {}},
            },
        ],
        "constraint": [
            {"primary_key": {"columns": ["film_id", "category_id"]}},
            {
                "foreign_key": {
                    "columns": "film_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "film_id", "table": "film"},
                },
                "name": "fk_film_category_film",
            },
            {
                "foreign_key": {
                    "columns": "category_id",
                    "on_delete": "restrict",
                    "on_update": "cascade",
                    "references": {"columns": "category_id", "table": "category"},
                },
                "name": "fk_film_category_category",
            },
        ],
        "default_charset": "utf8mb4",
        "engine": "InnoDB",
        "name": "film_category",
    }},
    {"set": {"@old_default_storage_engine": "@@default_storage_engine"}},
    {"set": {"@@default_storage_engine": {"literal": "MyISAM"}}},
    None,
    {"create table": {
        "columns": [
            {"name": "film_id", "nullable": False, "type": {"smallint": {}, "unsigned": True}},
            {"name": "title", "nullable": False, "type": {"varchar": 255}},
            {"name": "description", "type": {"text": {}}},
        ],
        "constraint": [
            {"primary_key": {"columns": "film_id"}},
            {"fulltext_key": {"columns": ["title", "description"], "name": "idx_title_description"}},
        ],
        "default_charset": "utf8mb4",
        "name": "film_text",
    }},
    {"set": {"@@default_storage_engine": "@old_default_storage_engine"}},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
    {},
]
