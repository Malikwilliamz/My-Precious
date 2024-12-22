package com.example.myapplication;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.ListView;
import android.widget.SearchView;
import android.widget.Toast;

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

public class RentorPage extends AppCompatActivity {
    SearchView searchView;
    ListView listView;
    ListView listItems;
    SearchView itemView;
    Button rentedItems;
    Button browse;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_rentor_page);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;
        });
        searchView = findViewById(R.id.searchView);
        itemView = findViewById(R.id.itemSearch);

        listItems = findViewById(R.id.searchItems);
        listView=findViewById(R.id.searchCategories);
        rentedItems = findViewById(R.id.buttonRentedItems);
        browse = findViewById(R.id.browseButton);


        browse.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(RentorPage.this, ItemList_RecyclerView.class);
                startActivity(intent);
            }
        });
        rentedItems.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(RentorPage.this, RentedItems.class);
                startActivity(intent);
            }
        });

        searchView.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
            @Override
            public boolean onQueryTextSubmit(String query) {
                searchCategories(query); // Fetch results from Firebase
                return false;
            }

            @Override
            public boolean onQueryTextChange(String newText) {
                searchCategories(newText); // Dynamically update results
                return false;
            }
        });

        itemView.setOnQueryTextListener(new SearchView.OnQueryTextListener() {
            @Override
            public boolean onQueryTextSubmit(String query) {
                searchItems(query); // Fetch results from Firebase
                return false;
            }

            @Override
            public boolean onQueryTextChange(String newText) {
                searchItems(newText); // Dynamically update results
                return false;
            }
        });

        listItems.setOnItemClickListener(new AdapterView.OnItemClickListener(){
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {
                Item selectedItem = (Item) listItems.getItemAtPosition(i);
                if (selectedItem.isAvailable()) {
                    selectedItem.requestItem();
                    Toast.makeText(RentorPage.this, "Sent request for " + selectedItem.getItemName(), Toast.LENGTH_SHORT).show();
                }
                else {
                    Toast.makeText(RentorPage.this, selectedItem.getItemName() + " has already be requested", Toast.LENGTH_SHORT).show();
                }
            }
        });


    }
    public void searchCategories(String query) {
        if (query.equals("")){
            return;
        }
        DatabaseReference databaseReference = FirebaseDatabase.getInstance().getReference("categories");
        databaseReference.orderByChild("categoryName").startAt(query).endAt(query + "\uf8ff")
                .addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        List<Category> categories = new ArrayList<>();
                        for (DataSnapshot data : dataSnapshot.getChildren()) {
                            String name = data.child("categoryName").getValue(String.class);
                            String desc = data.child("description").getValue(String.class);
                            String id = data.child("id").getValue(String.class);
                            Category category = new Category(id,name,desc);
                            categories.add(category);
                        }
                        CategoryList categoryList = new CategoryList(RentorPage.this,categories);
                        listView.setAdapter(categoryList);
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {

                    }
                });
    }


    public void searchItems(String query) {
        if (query.equals("")){
            return;
        }
        DatabaseReference databaseReference = FirebaseDatabase.getInstance().getReference("items");
        databaseReference.orderByChild("itemName").startAt(query).endAt(query + "\uf8ff")
                .addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot dataSnapshot) {
                        List<Item> items = new ArrayList<>();
                        for (DataSnapshot data : dataSnapshot.getChildren()) {
                            String name = data.child("itemName").getValue(String.class);
                            String desc = data.child("description").getValue(String.class);
                            String id = data.child("id").getValue(String.class);
                            String category = data.child("categoryName").getValue(String.class);
                            String startDate = data.child("startDate").getValue(String.class);
                            String endDate = data.child("endDate").getValue(String.class);
                            String fee = data.child("fee").getValue(String.class);
                            String ownerID = data.child("ownerID").getValue(String.class);
                            Item item = new Item(id,name,desc,fee,startDate,endDate,category,ownerID);
                            items.add(item);
                        }
                        ItemList itemList = new ItemList(RentorPage.this,items);
                        listItems.setAdapter(itemList);
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError databaseError) {

                    }
                });
    }

}