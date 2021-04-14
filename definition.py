from typing import Optional


class Account:
    def __init__(self, name: str):
        self.name = name
        self.owner: Optional["Advertiser"] = None

    def __repr__(self):
        return f'<Account "{self.name}" owner={"None" if self.owner is None else self.owner.name}>'

    def set_owner(self, new_owner: "Advertiser"):
        if self.owner != new_owner:
            old_owner: Optional["Advertiser"] = self.owner
            self.owner = new_owner
            if new_owner is not None:
                new_owner.add_account(self)
            if old_owner is not None:
                old_owner.remove_account(self)


class Advertiser:
    def __init__(self, name: str, accounts: Optional[set] = None):
        self.name = name
        if accounts is None:
            self.accounts = set()
        else:
            self.accounts = accounts

    def __repr__(self):
        return f'<Advertiser "{self.name}" accounts={self.accounts}>'

    def add_account(self, a):
        self.accounts.add(a)
        a.set_owner(self)

    def remove_account(self, a):
        self.accounts.remove(a)
        a.set_owner(None)