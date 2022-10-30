import 'package:flutter/material.dart';
import 'package:notes_app/db/database_provider.dart';
import 'package:notes_app/model/note_model.dart';

class ShowNote extends StatelessWidget {
  const ShowNote({Key key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final NoteModel note =
        ModalRoute.of(context).settings.arguments as NoteModel;
    return Scaffold(
        appBar: AppBar(
          title: Text("Your Note"),
          actions: [
            IconButton(
                onPressed: () {
                  DatabaseProvider.db.deleteNote(note.id);
                  Navigator.pushNamedAndRemoveUntil(
                      context, "/", (route) => false);
                },
                icon: Icon(Icons.delete))
          ],
        ),
        body: Padding(
          padding: const EdgeInsets.all(20.0),
          child: Card(
            elevation: 10.0,
            child: Container(
              height: 180,
              width: MediaQuery.of(context).size.width,
              child: Column(
                children: [
                  SizedBox(
                    height: 20,
                  ),
                  Text(
                    note.title,
                    style: TextStyle(fontSize: 30.0),
                  ),
                  SizedBox(
                    height: 20,
                  ),
                  Text(
                    note.body,
                    style: TextStyle(fontSize: 20.0),
                  ),
                ],
              ),
            ),
          ),
        ));
  }
}
