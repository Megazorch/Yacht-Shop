-- Create the user 'roman' with password 'Romashka234=+'
CREATE USER roman WITH ENCRYPTED PASSWORD 'Romashka234=+';

-- Create the database 'yacht_shop' and grant all privileges to user 'roman'
CREATE DATABASE yacht_shop;
GRANT ALL PRIVILEGES ON DATABASE yacht_shop TO roman;

-- Grant Permissions to the 'public' schema
GRANT USAGE ON SCHEMA public TO roman;

-- Additionally, grant privileges to the user on all existing tables in the 'public' schema:
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO roman;
