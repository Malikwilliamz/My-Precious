package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;


import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.google.android.gms.tasks.OnSuccessListener;
import com.google.android.gms.tasks.Task;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.List;

public class EditCategory  extends AppCompatActivity{
    FirebaseAuth auth;
    FirebaseDatabase database;
    DatabaseReference databaseReference;
    EditText descriptionEdit;
    EditText categoryEdit;
    EditText categoryToDelete;
    EditText descriptionToDelete;
    Button saveButton;
    DatabaseReference mDatabase;
    List<Category> categoryList;
    Button deleteCategory;

    @Override
    protected void onCreate(Bundle savedInstanceState){
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.edit_category);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });

        databaseReference = FirebaseDatabase.getInstance().getReference().child("categories");
        categoryEdit = findViewById(R.id.editTextName29);
        descriptionEdit = findViewById(R.id.editTextDescription20);
        deleteCategory = findViewById(R.id.buttonAddcategory39);
        saveButton = findViewById(R.id.buttonAddcategory58);
        saveButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String categoryEntered = categoryEdit.getText().toString();

                Query query2 = databaseReference.orderByChild("categoryName").equalTo(categoryEntered);
                query2.addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot snapshot) {
                        if(snapshot.exists()){
                            for(DataSnapshot categorySnapshot: snapshot.getChildren()){
                                String id2 = categorySnapshot.getKey();
                                String newCategoryName = categoryEdit.getText().toString();
                                String newCategoryDescription = descriptionEdit.getText().toString();

                                saveData(id2, newCategoryName, newCategoryDescription);
                                showToast("CATEGORY DATA UPDATED");
                            }
                        }

                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError error) {

                    }
                });

            }
        });


        deleteCategory.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String categoryEntered = categoryEdit.getText().toString();
                Query query = databaseReference.orderByChild("categoryName").equalTo(categoryEntered);

                query.addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot snapshot) {
                        if(snapshot.exists()){
                            for(DataSnapshot categorySnapshot: snapshot.getChildren()){
                                String id = categorySnapshot.getKey();
                                deleteCategory(id);
                                categoryEdit.setText("");
                                descriptionEdit.setText("");
                            }
                        }
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError error) {

                    }
                });

            }
        });



        showCategory();


    }
    public void showToast(String message){
        Toast.makeText(EditCategory.this, message, Toast.LENGTH_SHORT).show();
    }
    public void deleteCategory(String id){
        databaseReference = FirebaseDatabase.getInstance().getReference("categories").child(id);
        Task<Void> mTask = databaseReference.removeValue();
        mTask.addOnSuccessListener(new OnSuccessListener<Void>() {
            @Override
            public void onSuccess(Void unused) {
                showToast("Deleted");
            }
        });

    }

    public void showCategory(){
        Intent intent = getIntent();

        String categoryName = intent.getStringExtra("categoryName");
        String categoryDescription = intent.getStringExtra("description");

        categoryEdit.setText(categoryName);
        descriptionEdit.setText(categoryDescription);


    }
    public void saveData(String id, String newCategoryName, String newCategoryDescription){
        DatabaseReference ref = FirebaseDatabase.getInstance().getReference("categories").child(id);
        Category category = new Category(id, newCategoryName, newCategoryDescription);
        ref.setValue(category.toMap());
    }

}

