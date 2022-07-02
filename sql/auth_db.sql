create table companies
(
    id          integer default nextval('companies_id_seq'::regclass) not null
        constraint companies_pk
            primary key,
    active_flag boolean                                               not null,
    name        varchar(255)                                          not null,
    api_key     varchar(255)
);

create unique index companies_api_key_uindex on companies (api_key);

create table users
(
    id            integer           not null
        constraint users_pk
            primary key,
    email         text,
    first_name    text,
    second_name   text,
    last_name     text,
    password_hash text,
    active_flag   integer default 0 not null,
    company_id    integer
        constraint users_companies_id_fk
            references companies
);


create sequence session_id_seq as integer;

create table sessions
(
    id                      integer default nextval('session_id_seq'::regclass) not null
        constraint session_pkey
            primary key,
    user_id                 integer
        constraint session_user_id_fkey
            references users,
    access_token            text                                                not null
        constraint session_access_token_key
            unique,
    refresh_token           text                                                not null
        constraint session_refresh_token_key
            unique,
    access_expiration_date  timestamp                                           not null,
    refresh_expiration_date timestamp                                           not null
);
