-- company 1
insert ignore into organization_company(id, name, is_active, created_at, updated_at)
values(1, 'fakebook', 1, '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');

insert ignore  into organization_department(id, name, company_id)
values(1,'dept1', 1);
insert ignore  into organization_department(id, name, company_id)
values(2, 'dept2', 1);
insert ignore  into organization_department(id, name, company_id)
values(3, 'dept3', 1);

insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('nick3435@mail.com', 'nick3435', '273eb9e115085e81b75d79f26c82487d', 'nick', 1, 1,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('john1234@mail.com', 'john1234', '273eb9e115085e81b75d79f26c82487d', 'john', 1, 1,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('janny5467@mail.com', 'janny5467', '273eb9e115085e81b75d79f26c82487d', 'janny', 1, 1,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('hen6657@mail.com', 'hen6657', '273eb9e115085e81b75d79f26c82487d', 'hen', 1, 2,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('amy978445@mail.com', 'amy978445', '273eb9e115085e81b75d79f26c82487d', 'amy', 1, 2,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('joe9028476@mail.com', 'joe9028476', '273eb9e115085e81b75d79f26c82487d', 'joe', 1, 2,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('ken3029874@mail.com', 'ken3029874', '273eb9e115085e81b75d79f26c82487d', 'ken', 1, 3,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('edward2345114@mail.com', 'edward2345114', '273eb9e115085e81b75d79f26c82487d', 'edward', 1, 3,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('jason57783@mail.com', 'jason57783', '273eb9e115085e81b75d79f26c82487d', 'jason', 1, 3,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');

-- company 2
insert ignore into organization_company(id, name, is_active, created_at, updated_at)
values(2, 'twitcher', 1, '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');

insert ignore into organization_department(id, name, company_id)
values(4,'部門1', 2);
insert ignore into organization_department(id, name, company_id)
values(5, '部門2', 2);

insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('amber4356@mail.com', 'amber4356', '273eb9e115085e81b75d79f26c82487d', 'amber', 2, 4,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('carol90807@mail.com', 'carol90807', '273eb9e115085e81b75d79f26c82487d', 'carol', 2, 4,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('david5467@mail.com', 'david5467', '273eb9e115085e81b75d79f26c82487d', 'david', 2, 4,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('henry6657@mail.com', 'henry6657', '273eb9e115085e81b75d79f26c82487d', 'henry', 2, 4,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('cook9999@mail.com', 'cook9999', '273eb9e115085e81b75d79f26c82487d', 'cook', 2, 4,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('joe74147@mail.com', 'joe74147', '273eb9e115085e81b75d79f26c82487d', 'joe', 2, 5,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('danny0987@mail.com', 'danny0987', '273eb9e115085e81b75d79f26c82487d', 'danny', 2, 5,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('henson0000@mail.com', 'henson0000', '273eb9e115085e81b75d79f26c82487d', 'henson', 2, 5,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('jackson57783@mail.com', 'jackson57783', '273eb9e115085e81b75d79f26c82487d', 'jackson', 2, 5,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');

-- company 3

insert ignore into organization_company(id, name, is_active, created_at, updated_at)
values(3, 'amason', 1, '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');

insert ignore into organization_department(id, name, company_id)
values(6,'finance', 3);

insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('ava4356@mail.com', 'ava4356', '273eb9e115085e81b75d79f26c82487d', 'ava', 3, 6,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('chris90807@mail.com', 'chris90807', '273eb9e115085e81b75d79f26c82487d', 'chris', 3, 6,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('bid5467@mail.com', 'bid5467', '273eb9e115085e81b75d79f26c82487d', 'bid', 3, 6,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('anne6657@mail.com', 'anne6657', '273eb9e115085e81b75d79f26c82487d', 'anne', 3, 6,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('ada9999@mail.com', 'ada9999', '273eb9e115085e81b75d79f26c82487d', 'ada', 3, 6,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('dot74147@mail.com', 'dot74147', '273eb9e115085e81b75d79f26c82487d', 'dot', 3, 6,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('eva0987@mail.com', 'eva0987', '273eb9e115085e81b75d79f26c82487d', 'eva', 3, 6,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('cora0000@mail.com', 'cora0000', '273eb9e115085e81b75d79f26c82487d', 'cora', 3, 6,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
insert ignore into user_client(email, account, password, name, company_id, dept_id, created_at, updated_at)
values('ella57783@mail.com', 'ella57783', '273eb9e115085e81b75d79f26c82487d', 'ella', 3, 6,
        '2024-05-01 22:34:37.000000', '2024-05-01 22:34:37.000000');
