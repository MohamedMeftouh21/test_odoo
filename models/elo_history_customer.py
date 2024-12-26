from odoo import models, fields, api, tools
from ..utils.encryption import generate_global_key  # Import from the 'utils' directory
# Global Encryption Key
GLOBAL_ENCRYPTION_KEY = generate_global_key()

class EloHistoryCustomer(models.Model):
    _name = 'elo.history.customer'
    _description = 'Historique du client'

    name = fields.Char(string='Nom', tracking=True)
    date_of_attempt = fields.Datetime('Dernière tentative', tracking=True)
    data = fields.Text('Données', tracking=True)

    def _encrypt_value(self, value):
        if not value:
            return value
        self.env.cr.execute("""
            SELECT encode(
                pgp_sym_encrypt(%s::text, %s, 'compress-algo=1, cipher-algo=aes256')::bytea, 
                'base64'
            )
        """, (value, GLOBAL_ENCRYPTION_KEY))
        return self.env.cr.fetchone()[0]

    def _decrypt_value(self, encrypted_value):
        if not encrypted_value:
            return encrypted_value
        self.env.cr.execute("""
            SELECT pgp_sym_decrypt(
                decode(%s, 'base64')::bytea, 
                %s
            )::text
        """, (encrypted_value, GLOBAL_ENCRYPTION_KEY))
        return self.env.cr.fetchone()[0]

    @api.model
    def create(self, vals):
        # Encrypt sensitive data before storing
        if vals.get('name'):
            vals['name'] = self._encrypt_value(vals['name'])
        if vals.get('data'):
            vals['data'] = self._encrypt_value(vals['data'])
        return super(EloHistoryCustomer, self).create(vals)

    def write(self, vals):
        # Encrypt sensitive data before updating
        if vals.get('name'):
            vals['name'] = self._encrypt_value(vals['name'])
        if vals.get('data'):
            vals['data'] = self._encrypt_value(vals['data'])
        return super(EloHistoryCustomer, self).write(vals)

    def read(self, fields=None, load='_classic_read'):
        # Decrypt data when reading
        result = super(EloHistoryCustomer, self).read(fields, load=load)
        for record in result:
            if 'name' in record:
                try:
                    record['name'] = self._decrypt_value(record['name'])
                except:
                    record['name'] = 'Decryption Error'
            if 'data' in record:
                try:
                    record['data'] = self._decrypt_value(record['data'])
                except:
                    record['data'] = 'Decryption Error'
        return result

    # Test method to verify encryption
    @api.model
    def test_encryption(self):
        test_value = "Test Value"
        encrypted = self._encrypt_value(test_value)
        decrypted = self._decrypt_value(encrypted)
        return {
            'original': test_value,
            'encrypted': encrypted,
            'decrypted': decrypted,
            'encryption_key_length': len(GLOBAL_ENCRYPTION_KEY),
            'success': test_value == decrypted
        }