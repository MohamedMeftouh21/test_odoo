#!/bin/bash

# Set login credentials
ODOO_EMAIL="admin@example.com"  # You can change this
ODOO_PASSWORD="admin123"        # You can change this

echo "Stopping containers..."
docker compose down

echo "Removing old volumes..."
docker volume prune -f

echo "Starting containers..."
docker compose up -d

echo "Waiting for database to be ready..."
sleep 10

echo "Creating database..."
docker exec -it odoo18 createdb -U odoo -h db test_odoo

echo "Compiling Python files to .pyc..."
python3 compile_to_pyc.py

# Set admin password and email
docker exec -it odoo18 psql -U odoo -h db -d test_odoo -c "
    UPDATE res_users 
    SET login='${ODOO_EMAIL}', 
        password='${ODOO_PASSWORD}' 
    WHERE id=1;
"

echo "Updating module in Odoo..."
docker exec -it odoo18 /usr/bin/odoo \
    -d test_odoo \
    -u test_odoo \
    --stop-after-init \
    --db_host=db \
    --db_port=5432 \
    --db_user=odoo \
    --db_password=odoo

echo "Restarting Odoo container..."
docker compose restart odoo

echo "Deployment complete!"
echo "=============================="
echo "Odoo Login Credentials:"
echo "URL: http://localhost:8069"
echo "Database: test_odoo"
echo "Email: ${ODOO_EMAIL}"
echo "Password: ${ODOO_PASSWORD}"
echo "=============================="