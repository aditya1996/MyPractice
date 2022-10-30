import 'package:notes_app/model/note_model.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

class DatabaseProvider {
  DatabaseProvider._();
  static final DatabaseProvider db = DatabaseProvider._();
  static Database _database;

  // creating the getter the database
  Future<Database> get database async {
    // first let's check that we don't already have a db

    if (_database != null) {
      return _database;
    }

    _database = await initDB();
    return _database;
  }

  initDB() async {
    return await openDatabase(
      join(await getDatabasesPath(), "notes_app.db"),
      onCreate: (db, version) async {
        await db.execute('''
        CREATE TABLE notes (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          title TEXT,
          body TEXT,
          creationDate DATE
        )
        ''');
        // make sure that the names are similar to our model variables
      },
      version: 1,
    );
  }

  // Function that will add a new note to our variable
  addNewNote(NoteModel note) async {
    final db = await database;
    db.insert("notes", note.toMap(),
        conflictAlgorithm: ConflictAlgorithm.replace);
  }

  //Function that will fetch our database and return all elements in notes table
  Future<dynamic> getNotes() async {
    final db = await database;
    var res = await db.query("notes");
    if (res.isEmpty) {
      return Null;
    } else {
      var resultMap = res.toList();
      return resultMap.isNotEmpty ? resultMap : Null;
    }
  }

  // Function to delete a note
  Future<int> deleteNote(int id) async {
    final db = await database;
    int count = await db.rawDelete("DELETE FROM notes WHERE id = ?", [id]);
    return count; // return the number of row deleted
  }
}
