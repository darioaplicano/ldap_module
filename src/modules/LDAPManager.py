from ldap3 import Server, Connection

class LDAPManager:
    def __init__(self, server, port, base_dn, user, password):
        """
        Initializes a custom_ldap object.

        Parameters:
        - server (str): The LDAP server address.
        - user (str): The username for authentication.
        - password (str): The password for authentication.
        """
        self.server = server
        self.port = port
        self.base_dn = base_dn
        self.user = user
        self.password = password
        self.conn = None

    def bind(self):
        """
        Binds to the LDAP server using the provided credentials.

        Returns:
        - bool: True if the binding is successful, False otherwise.
        """
        try:
            self.conn = Connection(self.server, user=self.user, password=self.password, auto_bind=True)
            return True     
        
        except Exception as e:          
            print(f"Error al conectar al servidor LDAP: {e}")
            return False

    def unbind(self):
        """
        Unbinds from the LDAP server.

        Returns:
        - bool: True if the unbinding is successful, False otherwise.
        """
        try:
            self.conn.unbind()
            return True     
        
        except Exception as e:          
            print(f"Error al desconectar del servidor LDAP: {e}")
            return False