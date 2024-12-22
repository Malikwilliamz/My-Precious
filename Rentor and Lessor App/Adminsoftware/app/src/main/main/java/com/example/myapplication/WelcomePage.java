package com.example.myapplication;


import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Spinner;
import android.widget.TextView;
import android.widget.Toast;


import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;


import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

public class WelcomePage extends AppCompatActivity {
    private TextView nameView;
    private TextView roleView;
    private Button adminButton;
    Spinner spinnerr;
    private Button lesserButton;
    private Button rentorButton;
    private FirebaseAuth myAuth;
    private FirebaseUser mUser;
    private DatabaseReference mDatabase;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_welcome_page);
            ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });


            myAuth=FirebaseAuth.getInstance();

            mUser = myAuth.getCurrentUser();
            nameView = findViewById(R.id.welcome);
            adminButton = findViewById(R.id.adminPageButton);
            lesserButton = findViewById(R.id.lessorPageButton);
            rentorButton = findViewById(R.id.button2);
            mDatabase = FirebaseDatabase.getInstance().getReference("users").child(mUser.getUid());
            mDatabase.addListenerForSingleValueEvent(new ValueEventListener() {
                @Override
                public void onDataChange(@NonNull DataSnapshot snapshot) {
                    String names = snapshot.child("name").getValue(String.class);
                    String roles = snapshot.child("role").getValue(String.class);
                    nameView.setText("Welcome "+names+"! "+"You are logged in as a " + roles+".");
                    if (roles != null && roles.equals("admin")) {
                        adminButton.setVisibility(View.VISIBLE);
                    }
                    else if (roles!=null&&roles.equals("Lessor")){
                        lesserButton.setVisibility(View.VISIBLE);
                    }
                    else if (roles!=null&&roles.equals("Rentor")){
                        rentorButton.setVisibility(View.VISIBLE);
                    }

                }
                @Override
                public void onCancelled(@NonNull DatabaseError error) {
                    Toast.makeText(WelcomePage.this, "Something Wrong Happened", Toast.LENGTH_LONG).show();
                }
            });
            adminButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    startActivity(new Intent(WelcomePage.this, AdminPage.class));
                }
            });
            lesserButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    Intent intent = new Intent(WelcomePage.this, LessorPage.class);
                    startActivity(intent);
                }
            });
            rentorButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    Intent intent = new Intent(WelcomePage.this,RentorPage.class);
                    startActivity(intent);
                }
            });
        }


}
