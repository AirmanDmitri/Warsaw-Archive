# Warsaw Historical Archive

A Python-based historical research archive for documenting the development of Warsaw, with a particular focus on neighbourhoods, buildings, streets, and their history from the late 19th century to the present.

## Overview

The Warsaw Historical Archive is a personal research project that combines historical research with data structures and programming.

The application stores historical records in a **Binary Search Tree (BST)**, organized by year. Multiple records can be associated with the same year, allowing different events, photographs, documents, and discoveries to be grouped chronologically.

The goal is to gradually build a searchable historical archive that connects individual buildings and neighbourhoods to the wider history of Warsaw.

## Features

- **Add historical records:** Store dates, titles, categories, addresses, descriptions, and sources.
- **Chronological timeline:** Display records in chronological order using an in-order BST traversal.
- **Search by year:** Retrieve all records associated with a particular year.
- **Keyword search:** Search titles, descriptions, addresses, categories, and sources.
- **Persistent storage:** Save records in a JSON file and reconstruct the BST when the application starts.
- **Multiple records per year:** Group several historical findings under the same year.

## Technologies

- Python
- Binary Search Trees
- Object-Oriented Programming
- JSON
- Git and GitHub

## Project Structure

```text
WarsawHistoricalArchive/
│
├── warsaw_archive.py
├── warsaw_history.json
├── README.md
└── .gitignore
```

`warsaw_history.json` is generated automatically when the first record is saved.

## Getting Started

### Requirements

- Python 3.10 or newer

### Running the application

Clone the repository:

```bash
git clone https://github.com/AirmanDmitri/WarsawHistoricalArchive.git
```

Navigate into the project directory:

```bash
cd WarsawHistoricalArchive
```

Run the application:

```bash
python warsaw_archive.py
```

## Data Structure

The archive uses a Binary Search Tree to organize historical records by year.

Each node contains:
- A year
- A list of historical records associated with that year
- A reference to its left child
- A reference to its right child

The tree follows the standard BST ordering:

- Years earlier than the current node are placed in the left subtree.
- Years later than the current node are placed in the right subtree.
- Records from the same year are stored together in the current node.

An in-order traversal visits the left subtree, the current node, and then the right subtree, producing a chronological timeline.

## Future Development

Planned improvements include:

- Editing and deleting existing records.
- Searching by address, street, and date range.
- Attaching photographs and historical maps.
- Supporting multiple sources and references per record.
- Creating dedicated profiles for individual buildings.
- Exporting historical timelines.
- Developing a graphical user interface.

## Purpose

This project is both a programming exercise and an ongoing historical research project. It is intended to document the changing urban landscape of Warsaw while providing a structured way to organize historical findings and their supporting evidence.