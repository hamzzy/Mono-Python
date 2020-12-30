
class MonoUser:
    def __init__(self, user_id=None):
        """
        Setter & Getter Class for User Id response
        """
        self.user_id = user_id

    def SetUserId(self, id):
        """
        This function set a return user id
        """
        self.user_id = id

    def GetUserId(self):
        """
         This function get a  user id

         """
        return self.user_id
