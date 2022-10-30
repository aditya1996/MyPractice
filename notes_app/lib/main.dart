import 'package:flutter/material.dart';
import 'package:notes_app/db/database_provider.dart';
import 'package:notes_app/model/note_model.dart';
import 'package:notes_app/screens/add_note.dart';
import 'package:notes_app/screens/display_note.dart';
import 'screens/add_note.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      // routes
      initialRoute: "/",
      routes: {
        "/": (context) => HomeScreen(),
        "/AddNote": (context) => AddNote(),
        "/ShowNote": (context) => ShowNote(),
      },
    );
  }
}

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  //getting all notes
  getNotes() async {
    final notes = await DatabaseProvider.db.getNotes();
    return notes;
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Your Notes"),
      ),
      body: FutureBuilder(
        future: getNotes(),
        builder: (context, noteData) {
          switch (noteData.connectionState) {
            case ConnectionState.waiting:
              {
                return const Center(
                  child: CircularProgressIndicator(),
                );
              }
              break;
            case ConnectionState.done:
              {
                if (!noteData.hasData) {
                  return const Center(
                    child: Text("You don't have any notes yet, create one!"),
                  );
                } else {
                  return Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: ListView.builder(
                      itemCount: noteData.data.length,
                      itemBuilder: (context, index) {
                        String title = noteData.data[index]['title'];
                        String body = noteData.data[index]['body'];
                        String creationDate =
                            noteData.data[index]['creationDate'];
                        int id = noteData.data[index]['id'];
                        return Card(
                          child: ListTile(
                            onTap: () {
                              Navigator.pushNamed(
                                context,
                                "/ShowNote",
                                arguments: NoteModel(
                                  title: title,
                                  body: body,
                                  creationDate: DateTime.parse(creationDate),
                                  id: id,
                                ),
                              );
                            },
                            title: Text(title),
                            subtitle: Text(body),
                          ),
                        );
                      },
                    ),
                  );
                }
              }
              break;
            default:
              {
                return const Center(
                  child: Text("You don't have any notes yet, create one!"),
                );
              }
          }
        },
      ),
      floatingActionButton: SizedBox(
        height: 70.0,
        width: 70.0,
        child: FittedBox(
          child: FloatingActionButton(
            onPressed: () {
              //Navigate to Note Creation Screen
              Navigator.pushNamed(context, "/AddNote");
            },
            child: const Icon(Icons.note_add),
          ),
        ),
      ),
    );
  }
}
