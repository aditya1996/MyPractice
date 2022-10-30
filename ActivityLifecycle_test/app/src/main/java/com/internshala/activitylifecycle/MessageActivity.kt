package com.internshala.activitylifecycle

import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.TextView

class MessageActivity : AppCompatActivity() {

    lateinit var txtMessage: TextView
    var message = "Custom Message"
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_message)

        txtMessage = findViewById(R.id.txtMessage)

        if (intent != null) {
            message = intent.getStringExtra("Message")
            txtMessage.text = message
        }

    }
}
