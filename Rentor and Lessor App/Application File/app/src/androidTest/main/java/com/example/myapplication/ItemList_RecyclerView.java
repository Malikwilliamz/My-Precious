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


        itemList = new ArrayList<>();
        myAdapter = new MyAdapter(this, itemList);
        recyclerView.setAdapter(myAdapter);

        databaseRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                for(DataSnapshot dataSnapshot: snapshot.getChildren()){
                    Item item = dataSnapshot.getValue(Item.class);
                    itemList.add(item);

                }

                myAdapter.notifyDataSetChanged();
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });


    }

}
