create table if not exists public.images (
    id serial primary key,
    parent_id int,
    parent_table text,
    url text,
    metadata jsonb
);