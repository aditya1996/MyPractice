package com.internshala.activitylifecycle

import android.content.Context
import android.content.Intent
import android.content.SharedPreferences
import android.os.Bundle
import android.support.v7.app.AppCompatActivity
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast

class LoginActivity : AppCompatActivity() {

    lateinit var etMobileNumber: EditText
    lateinit var etPassword: EditText
    lateinit var btnLogin: Button
    lateinit var txtForgotPassword: TextView
    lateinit var txtRegisterYourself: TextView
    val validMobileNumber = "9876543210"
    val validPassword = arrayOf("tony", "steve", "bruce", "thanos")

    lateinit var sharedPreferences: SharedPreferences

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        sharedPreferences = getSharedPreferences(getString(R.string.preference_file_name), Context.MODE_PRIVATE)

        val isLoggedIn = sharedPreferences.getBoolean("isLoggedIn", false)

        setContentView(R.layout.activity_login)

        if (isLoggedIn) {
            val intent = Intent(this@LoginActivity, AvengersActivity::class.java)
            startActivity(intent)
            finish()
        }

        title = "Log In"

        etMobileNumber = findViewById(R.id.etMobileNumber)
        etPassword = findViewById(R.id.etPassword)
        btnLogin = findViewById(R.id.btnLogin)
        txtForgotPassword = findViewById(R.id.txtForgotPassword)
        txtRegisterYourself = findViewById(R.id.txtRegister)

        btnLogin.setOnClickListener {

            val mobileNumber = etMobileNumber.text.toString()

            val password = etPassword.text.toString()

            var nameOfAvenger = "Avenger"

            val intent = Intent(this@LoginActivity, AvengersActivity::class.java)

            if ((mobileNumber == validMobileNumber)) {

                when (password) {
                    validPassword[0] -> {

                        nameOfAvenger = "Iron Man"

                        savePreferences(nameOfAvenger)

                        startActivity(intent)

                    }
                    validPassword[1] -> {

                        nameOfAvenger = "Captain America"

                        savePreferences(nameOfAvenger)

                        startActivity(intent)

                    }
                    validPassword[2] -> {

                        nameOfAvenger = "The Hulk"

                        savePreferences(nameOfAvenger)

                        startActivity(intent)

                    }
                    validPassword[3] -> {

                        nameOfAvenger = "The Avengers"

                        savePreferences(nameOfAvenger)

                        startActivity(intent)

                    }
                    else -> Toast.makeText(this@LoginActivity, "Incorrect Password", Toast.LENGTH_LONG).show()
                }

            } else {

                Toast.makeText(this@LoginActivity, "Incorrect Credentials", Toast.LENGTH_LONG).show()

            }
        }


        txtForgotPassword.setOnClickListener {
            val intent = Intent(this@LoginActivity, ForgotPasswordActivity::class.java)
            startActivity(intent)
        }

        txtRegisterYourself.setOnClickListener {
            val intent = Intent(this@LoginActivity, RegisterActivity::class.java)
            startActivity(intent)
        }

    }

    override fun onPause() {
        super.onPause()
        finish()
    }

    fun savePreferences(title: String) {
        sharedPreferences.edit().putBoolean("isLoggedIn", true).apply()
        sharedPreferences.edit().putString("title", title).apply()
    }
}
