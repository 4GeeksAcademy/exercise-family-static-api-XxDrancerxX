
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        print("This is the member", member)
        if "id" not in member:
            member["id"] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        print(f"Looking for member with ID: {id}")
        for index, member in enumerate(self._members):
            if member["id"] == id:
                deleted = self._members.pop(index)
                print(f"Deleted member: {deleted}")
                return deleted
        print("No member found with that ID.")
        return None

    def get_member(self, urlID):

        # fill this method and update the return
        for member in self._members:
            member_id = member["id"]
            print(member_id, "member_id!!!!!")
            if urlID == member_id:
                return member
        return None

    # this method is done, it returns a list with all the family members

    def get_all_members(self):
        return self._members
