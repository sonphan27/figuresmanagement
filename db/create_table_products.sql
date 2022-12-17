CREATE TYPE public.e_shipping_status AS ENUM (
    'wished',
    'pre-ordered',
    'ordered',
    'shipping',
    'shipped',
    'sold'
);
CREATE TYPE public.e_status AS ENUM (
    'new',
    '2nd',
    '2nd (no box)'
);

create table if not exists public.products (
    id serial primary key,
    code text,
    name text,
    brand_id int,
    company_id int,
    bought_price float,
    sold_price float,
    series_id int,
    status e_status default 'new',
    shipping_status e_shipping_status default 'shipped',
    bought_from text,
    active boolean default true,
    metadata jsonb
)