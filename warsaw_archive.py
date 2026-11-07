
import json
import os


# ==========================================
# BINARY SEARCH TREE
# ==========================================

class Node:
    def __init__(self, year):
        self.year = year
        self.records = []
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, record):
        self.root = self._insert_recursive(
            self.root, record
        )

    def _insert_recursive(self, node, record):
        if node is None:
            node = Node(record["year"])
            node.records.append(record)
            return node

        if record["year"] < node.year:
            node.left = self._insert_recursive(
                node.left, record
            )

        elif record["year"] > node.year:
            node.right = self._insert_recursive(
                node.right, record
            )

        else:
            node.records.append(record)

        return node

    def search(self, year):
        return self._search_recursive(self.root, year)

    def _search_recursive(self, node, year):
        if node is None:
            return None

        if year == node.year:
            return node.records

        if year < node.year:
            return self._search_recursive(node.left, year)

        return self._search_recursive(node.right, year)

    def inorder(self):
        records = []
        self._inorder_recursive(self.root, records)
        return records

    def _inorder_recursive(self, node, records):
        if node is not None:
            self._inorder_recursive(node.left, records)
            records.extend(node.records)
            self._inorder_recursive(node.right, records)


# ==========================================
# HISTORICAL ARCHIVE
# ==========================================

class HistoricalArchive:
    FILE_NAME = "warsaw_history.json"

    def __init__(self):
        self.tree = BST()
        self.records = []
        self.next_id = 1

        self.load()

    # --------------------------------------
    # ADD RECORD
    # --------------------------------------

    def add_record(self):
        print("\n=== ADD HISTORICAL RECORD ===")

        date = input("Date (YYYY or YYYY-MM-DD): ").strip()

        if len(date) not in (4, 10):
            print("Invalid date format.")
            return

        try:
            year = int(date[:4])

            if len(date) == 10:
                from datetime import date as Date
                Date.fromisoformat(date)

            elif not 1 <= year <= 9999:
                raise ValueError

        except ValueError:
            print("Invalid date.")
            return

        title = input("Title: ").strip()
        category = input("Category: ").strip()
        address = input("Address: ").strip()
        description = input("Description: ").strip()
        source = input("Source: ").strip()
        source_url = input("Source URL (optional): ").strip()
        confidence = input(
            "Evidence type (documented/photographic/unverified): "
        ).strip().lower()

        if not title:
            print("A title is required.")
            return

        record = {
            "id": self.next_id,
            "date": date,
            "year": year,
            "title": title,
            "category": category,
            "address": address,
            "description": description,
            "source": source,
            "source_url": source_url,
            "confidence": confidence,
            "notes": ""
        }

        self.records.append(record)
        self.tree.insert(record)

        self.next_id += 1

        self.save()

        print("\nHistorical record added successfully.")

    # --------------------------------------
    # DISPLAY RECORD
    # --------------------------------------

    def display_record(self, record):
        print("\n----------------------------------")
        print(f"ID: {record['id']}")
        print(f"Date: {record['date']}")
        print(f"Title: {record['title']}")
        print(f"Category: {record['category']}")
        print(f"Address: {record['address']}")
        print(f"Description: {record['description']}")
        print(f"Source: {record['source']}")
        print(f"Source URL: {record['source_url']}")
        print(f"Evidence: {record['confidence']}")
        print(f"Notes: {record['notes']}")
        print("----------------------------------")

    # --------------------------------------
    # CHRONOLOGICAL TIMELINE
    # --------------------------------------

    def show_timeline(self):
        print("\n=== HISTORICAL TIMELINE ===")

        records = self.tree.inorder()

        if not records:
            print("The archive is currently empty.")
            return

        for record in records:
            self.display_record(record)

    # --------------------------------------
    # SEARCH BY YEAR
    # --------------------------------------

    def search_year(self):
        print("\n=== SEARCH BY YEAR ===")

        try:
            year = int(input("Enter year: "))
        except ValueError:
            print("Please enter a valid year.")
            return

        results = self.tree.search(year)

        if results is None:
            print(f"No records found for {year}.")
            return

        for record in results:
            self.display_record(record)

    # --------------------------------------
    # SEARCH BY KEYWORD
    # --------------------------------------

    def search_keyword(self):
        print("\n=== SEARCH BY KEYWORD ===")

        keyword = input("Enter keyword: ").strip().lower()

        if not keyword:
            print("Please enter a keyword.")
            return

        results = []

        for record in self.records:
            searchable = " ".join([
                str(record["title"]),
                str(record["category"]),
                str(record["address"]),
                str(record["description"]),
                str(record["source"]),
                str(record["notes"])
            ]).lower()

            if keyword in searchable:
                results.append(record)

        if not results:
            print("No matching records found.")
            return

        for record in sorted(results, key=lambda r: (r["year"], r["id"])):
            self.display_record(record)

    # --------------------------------------
    # SAVE ARCHIVE
    # --------------------------------------

    def save(self):
        with open(self.FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(
                self.records,
                file,
                indent=4,
                ensure_ascii=False
            )

    # --------------------------------------
    # LOAD ARCHIVE
    # --------------------------------------

    def load(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r", encoding="utf-8") as file:
                self.records = json.load(file)

            # Reconstruct the BST from saved records.
            for record in self.records:
                self.tree.insert(record)

            if self.records:
                self.next_id = max(
                    record["id"] for record in self.records
                ) + 1

            print(f"Loaded {len(self.records)} historical records.")

        except (json.JSONDecodeError, KeyError, TypeError, ValueError):
            print("Could not load the historical archive.")
            self.records = []
            self.tree = BST()


# ==========================================
# MAIN APPLICATION
# ==========================================

def main():
    archive = HistoricalArchive()

    while True:
        print("\n====================================")
        print("       WARSAW HISTORICAL ARCHIVE")
        print("====================================")
        print("1. Add historical record")
        print("2. View chronological timeline")
        print("3. Search by year")
        print("4. Search by keyword")
        print("5. Exit")
        print("====================================")

        choice = input("Select an option: ").strip()

        if choice == "1":
            archive.add_record()

        elif choice == "2":
            archive.show_timeline()

        elif choice == "3":
            archive.search_year()

        elif choice == "4":
            archive.search_keyword()

        elif choice == "5":
            archive.save()
            print("Archive saved. Goodbye.")
            break

        else:
            print("Invalid selection. Try again.")


if __name__ == "__main__":
    main()
