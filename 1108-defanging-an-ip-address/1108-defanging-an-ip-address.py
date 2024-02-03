class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        #just replace every "." with "[.]" using the replace method
        return address.replace(".", "[.]")