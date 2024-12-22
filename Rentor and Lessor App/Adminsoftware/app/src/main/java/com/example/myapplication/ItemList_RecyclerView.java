package com.example.myapplication;

import android.os.Bundle;


import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;

public class ItemList_RecyclerView extends AppCompatActivity {
    RecyclerView recyclerView;
    DatabaseReference databaseRef;
    MyAdapter myAdapter;
    ArrayList<Item> itemList;
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_recyclerview);


        recyclerView = findViewById(R.id.itemlist);
        databaseRef = FirebaseDatabase.getInstance().getReference("items");
        recyclerView.setHasFixedSize(true);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));






        databaseRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                itemList = new ArrayList<>();
                for(DataSnapshot data: snapshot.getChildren()){
                    String itemname = data.child("itemName").getValue(String.class);
                    String description = data.child("description").getValue(String.class);
                    String id = data.child("id").getValue(String.class);
                    String startd = data.child("startDate").getValue(String.class);
                    String endd = data.child("endDate").getValue(String.class);
                    String categoryName = data.child("categoryName").getValue(String.class);
                    String fee = data.child("fee").getValue(String.class);

                    Item item = new Item(id,itemname, description, fee, startd, endd, categoryName);
                    itemList.add(item);

                }
                myAdapter = new MyAdapter(ItemList_RecyclerView.this, itemList);
                recyclerView.setAdapter(myAdapter);


            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });


    }

}
