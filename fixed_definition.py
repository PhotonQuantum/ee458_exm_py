from typing import Optional


class Account:
    def __init__(self, name: str):
        self.name = name
        self.owner: Optional["Advertiser"] = None

    def __repr__(self):
        return f'<Account "{self.name}" owner={"None" if self.owner is None else self.owner.name}>'

    def _set_owner(self, new_owner: "Advertiser"):
        self.owner = new_owner

    def set_owner(self, new_owner: "Advertiser"):
        if self.owner != new_owner:
            if self.owner is not None:
                self.owner.remove_account(self)
            if new_owner is not None:
                new_owner.add_account(self)


class Advertiser:
    def __init__(self, name: str):
        self.name = name
        self.accounts = set()

    def __repr__(self):
        return f'<Advertiser "{self.name}" accounts={self.accounts}>'

    def __contains__(self, item):
        return self.accounts.__contains__(item)

    def add_account(self, a):
        if a.owner is not None:
            a.owner.remove_account(a)
        self.accounts.add(a)
        a._set_owner(self)

    def remove_account(self, a):
        self.accounts.remove(a)
        a._set_owner(None)
