package com.example.myapplication;


import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;


import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;


import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.AuthResult;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.ktx.Firebase;
import android.widget.AdapterView;
import android.widget.Toast;


import java.util.*;


public class MainActivity extends AppCompatActivity {


    Spinner spinner;
    EditText name;
    EditText userName;
    EditText email;
    EditText password;
    EditText confirmPassword;
    Button button, loginRedirectbtn;
    FirebaseAuth auth;
    FirebaseDatabase database;
    DatabaseReference databaseReference;
    TextView textView;
    private String selectedValue;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        spinner = (Spinner) findViewById(R.id.spinner);
        name = (EditText) findViewById(R.id.editTextText);
        userName = (EditText) findViewById(R.id.editTextText2);
        email = (EditText) findViewById(R.id.editTextTextEmailAddress);
        password = (EditText) findViewById(R.id.editTextTextPassword);
        confirmPassword = (EditText) findViewById(R.id.editTextTextPassword2);
        button = (Button) findViewById(R.id.button);
        auth = FirebaseAuth.getInstance();
        database=FirebaseDatabase.getInstance();
        databaseReference = database.getReference().child("users");
        textView=findViewById(R.id.textView2);
        loginRedirectbtn = (Button) findViewById(R.id.loginRedirect);




        //Creates dropdown menu allowing users to choose either lessor or rentor;
        ArrayAdapter<String> arrayAdapter = new ArrayAdapter(this, androidx.appcompat.R.layout.support_simple_spinner_dropdown_item,new String[]{"Lessor","Rentor"});
        spinner.setAdapter(arrayAdapter);
        spinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener(){
            public void onItemSelected(AdapterView<?> parent, View v, int position, long id){
                selectedValue = parent.getItemAtPosition(position).toString();
            }

            public void onNothingSelected(AdapterView<?> parent){

            }
        });




    }

    public void createAccount(View v){

        if(validateFields()){
            Intent welcomePageIntent = new Intent(MainActivity.this,WelcomePage.class);
            auth.createUserWithEmailAndPassword(email.getText().toString(), password.getText().toString())
                    .addOnCompleteListener( new OnCompleteListener<AuthResult>() {
                        @Override
                        public void onComplete(@NonNull Task<AuthResult> task) {
                            if (task.isSuccessful()) {
                                // Sign in success, update UI with the signed-in user's information
                                FirebaseUser user = auth.getCurrentUser();
                                User user1 = new User(name.getText().toString(),userName.getText().toString(),email.getText().toString(), selectedValue,user.getUid().toString());
                                Map<String,Object> map = user1.toMap();
                                databaseReference.child(user.getUid()).setValue(map);

                                startActivity(welcomePageIntent);
                                //finish();
                            } else {
                                // If sign in fails, display a message to the user.
                                String errorMessage = task.getException().getMessage();

                                textView.setText(errorMessage);



                            }
                        }
                    });


        }

    }

    // Redirects to login page
    public void loginRedirect(View v) {
        startActivity(new Intent(MainActivity.this, Login_page.class));
    }






    //Validates user inputs
    private boolean validateFields(){
        boolean allFieldsValid = true;




        if(name.getText().toString().isEmpty()){
            name.setError("Name field can't be empty");
            allFieldsValid=false;
        }
        if(userName.getText().toString().isEmpty()){
            userName.setError("Username field can't be empty");
            allFieldsValid=false;
        }
        if(email.getText().toString().isEmpty()){
            email.setError("Email field can't be empty");
            allFieldsValid=false;
        }
        else if (!email.getText().toString().contains("@")){
            email.setError("Must be a valid email");
            allFieldsValid=false;
        }


        if(password.getText().toString().isEmpty()){
            password.setError("Password field can't be empty");
            allFieldsValid=false;
        }


        if(confirmPassword.getText().toString().isEmpty()){
            confirmPassword.setError("Confirm password field can't be empty");
            allFieldsValid=false;
        }
        else if(!confirmPassword.getText().toString().equals(password.getText().toString())){
            password.setError("Password and Confirm password are not equal");
            confirmPassword.setError("Password and Confirm password are not equal");
            allFieldsValid=false;
        }


        return allFieldsValid;


    }




}

