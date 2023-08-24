class ILegacyDatabase:
    def retrieve_data(self):
        pass

class IModernDatabase:
    def get_data(self):
        pass

class LegacyDatabase(ILegacyDatabase):
    def retrieve_data(self):
        print("Legacy database: Retrieving data")

class ModernDatabase(IModernDatabase):
    def get_data(self):
        print("Modern database: Getting data")

class DatabaseAdapter(ILegacyDatabase, IModernDatabase):
    def __init__(self, database):
        self.database = database

    def retrieve_data(self):
        if isinstance(self.database, LegacyDatabase):
            self.database.retrieve_data()
        elif isinstance(self.database, ModernDatabase):
            self.database.get_data()

def main():
    legacy_db = LegacyDatabase()
    modern_db = ModernDatabase()

    legacy_adapter = DatabaseAdapter(legacy_db)
    modern_adapter = DatabaseAdapter(modern_db)

    print("Using Legacy Database via Adapter:")
    legacy_adapter.retrieve_data()

    print("\nUsing Modern Database via Adapter:")
    modern_adapter.retrieve_data()

if __name__ == "__main__":
    main()
