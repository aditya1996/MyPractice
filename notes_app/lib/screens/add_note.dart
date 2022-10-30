import 'package:flutter/material.dart';
import 'package:notes_app/db/database_provider.dart';
import '/model/note_model.dart';

class AddNote extends StatefulWidget {
  @override
  _AddNoteState createState() => _AddNoteState();
}

class _AddNoteState extends State<AddNote> {
  String title;
  String body;
  DateTime date;

  // Addnote function and Input Controller
  TextEditingController titleController = TextEditingController();
  TextEditingController bodyController = TextEditingController();

  addNote(NoteModel note) {
    DatabaseProvider.db.addNewNote(note);
    print("note added sucessfully");
    print(note.title);
    print(note.body);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Add new Note"),
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(vertical: 8.0, horizontal: 12.0),
        child: Column(
          children: [
            SizedBox(
              //Use of SizedBox
              height: 30,
            ),
            TextField(
              controller: titleController,
              decoration: InputDecoration(
                // border: InputBorder.none,
                hintText: "Note Title",
              ),
              style: TextStyle(
                fontSize: 28.0,
                fontWeight: FontWeight.bold,
              ),
            ),
            SizedBox(
              //Use of SizedBox
              height: 30,
            ),
            Expanded(
              child: TextField(
                controller: bodyController,
                keyboardType: TextInputType.multiline,
                maxLines: null,
                decoration: InputDecoration(
                  // border: InputBorder.none,
                  hintText: "Your Note",
                ),
              ),
            )
          ],
        ),
      ),
      floatingActionButton: Container(
        height: 100.0,
        width: 150.0,
        child: FittedBox(
          child: FloatingActionButton.extended(
            onPressed: () {
              setState(() {
                title = titleController.text;
                body = bodyController.text;
                date = DateTime.now();
              });
              NoteModel note =
                  NoteModel(title: title, body: body, creationDate: date);
              addNote(note);

              Navigator.pushNamedAndRemoveUntil(context, "/", (route) => false);
            },
            label: const Text("Save Note"),
            icon: const Icon(Icons.save),
          ),
        ),
      ),
    );
  }
}
