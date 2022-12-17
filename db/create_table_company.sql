create table if not exists public.companies (
    id serial primary key,
    code text,
    name text,
    country_id text,
    metadata jsonb
);