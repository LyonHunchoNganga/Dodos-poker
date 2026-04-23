create table if not exists player(
    id uuid primary key default gen_random_uuid(),
    name varchar(250) not null,
    email varchar(500) not null unique,
    created_at timestamp not null default current_timestamp,
    updated_at timestamp not null default current_timestamp
);

create table if not exists player_password(
    id uuid primary key default gen_random_uuid(),
    player_id uuid not null unique references player(id) on delete cascade,
    password text not null,
    updated_at timestamp not null default current_timestamp
);