create table if not exists public.users (
  id serial primary key,
  name text not null unique,
  password text not null,
  metadata jsonb,
  active boolean default true
)