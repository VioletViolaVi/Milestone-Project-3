class Validator:

    def valid_username(self, username):

        if len(username) < 4 or len(username) > 14:

            return False

        return True
