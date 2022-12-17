create table if not exists public.series (
    id serial primary key,
    name text,
    type text,
    country_id text,
    metadata jsonb
);