create table if not exists public.users (
  id serial primary key,
  name text not null,
  pass text not null,
  active boolean default true
)