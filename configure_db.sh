psql postgres -c "CREATE DATABASE blog;"
echo Enter admin password:
read password
psql postgres -c "CREATE USER admin WITH PASSWORD '$password';"
echo psql postgres -c "CREATE USER admin WITH PASSWORD '$password';"
psql postgres -c "CREATE DATABASE test_blog;"
psql postgres -c "ALTER ROLE admin SET client_encoding TO 'utf8';"
psql postgres -c "ALTER ROLE admin SET default_transaction_isolation TO 'read committed';"
psql postgres -c "ALTER ROLE admin SET timezone TO 'UTC';"
psql postgres -c "ALTER ROLE admin CREATEDB;"
psql postgres -c "GRANT ALL PRIVILEGES ON DATABASE blog TO admin;"
