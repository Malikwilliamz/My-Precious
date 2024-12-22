package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ListView;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;


public class CategoryPage extends AppCompatActivity {

    ListView listView;
    List<Category> categories;
    FirebaseDatabase database;
    DatabaseReference databaseReference;
    Button backToLessorPage;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_lessor_item_page);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        categories= new ArrayList<>();
        listView=findViewById(R.id.listViewCategories);
        database = FirebaseDatabase.getInstance();
        databaseReference =database.getReference().child("categories");
        backToLessorPage = findViewById(R.id.backToLessorPage);

        backToLessorPage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(CategoryPage.this,LessorPage.class);
                startActivity(intent);
            }
        });

    }

    @Override
    protected void onStart(){

        super.onStart();
        databaseReference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                categories.clear();
                for(DataSnapshot data: snapshot.getChildren()){

                    String name = data.child("categoryName").getValue(String.class);
                    String desc = data.child("description").getValue(String.class);
                    String id = data.child("id").getValue(String.class);
                    Category category = new Category(id,name,desc);
                    categories.add(category);
                }
                showCategories();


            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });


    }

    public void showCategories(){
        CategoryList categoryList = new CategoryList(CategoryPage.this,categories);
        listView.setAdapter(categoryList);
    }

}