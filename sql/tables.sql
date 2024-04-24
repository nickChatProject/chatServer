create table friends
(
    id         int auto_increment
        primary key,
    user_id1   int         not null,
    user_id2   int         not null,
    status     varchar(50) null,
    created_at datetime    null
);

create table messages
(
    id          int auto_increment
        primary key,
    type        varchar(50)  null,
    sender_id   int          null,
    receiver_id int          null,
    content     varchar(500) null,
    created_at  datetime     null
);

create table organization_company
(
    id         int auto_increment
        primary key,
    name       varchar(100) not null,
    is_active  tinyint(1)   not null,
    created_at datetime(6)  not null,
    updated_at datetime(6)  not null,
    constraint name
        unique (name)
);

create table organization_department
(
    id         int auto_increment
        primary key,
    name       varchar(100) not null,
    company_id int          not null,
    constraint organization_departm_company_id_0ca6d3ca_fk_organizat
        foreign key (company_id) references organization_company (id)
);

create table user_client
(
    cid        int auto_increment
        primary key,
    email      varchar(254) not null,
    account    varchar(20)  not null,
    password   varchar(50)  not null,
    name       varchar(50)  not null,
    company_id int          null,
    picture    varchar(100) null,
    created_at datetime(6)  not null,
    updated_at datetime(6)  not null,
    dept_id    int          null,
    constraint account
        unique (account),
    constraint email
        unique (email)
);



