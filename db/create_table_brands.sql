create table if not exists public.brands (
    id serial primary key,
    name text,
    company_id int,
    country_id text,
    prefix_code text,
    metadata jsonb
);