create table users (
    name text not null,
    hash text not null,
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    cash NUMERIC NOT NULL DEFAULT 0,
    -- deuration of each task
    deuration INTEGER not null
);
create table tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    -- there is two stats of each task
    status Boolean DEFAULT 0,
    quantity INTEGER not null,
    focusedtime NUMERIC NOT NULL DEFAULT 0,
    estematedtime NUMERIC NOT NULL,
    priorty INTEGER not null,
    name text not null,
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
create table projects(
    user_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name text not null,
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status Boolean DEFAULT 0,
    priorty INTEGER not null,
    FOREIGN KEY (user_id)
       REFERENCES users (id),
    FOREIGN KEY (task_id)
       REFERENCES tasks (id)
);
create table doingtask(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    user_id INTEGER NOT NULL,
    task_id INTEGER NOT NULL,
    focusedtime NUMERIC NOT NULL DEFAULT 0,
    estematedtime NUMERIC NOT NULL,
    FOREIGN KEY (user_id)
       REFERENCES users (id),
    FOREIGN KEY (task_id)
       REFERENCES tasks (id)
);