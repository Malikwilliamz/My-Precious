package com.example.myapplication;

import android.app.DatePickerDialog;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;
import android.widget.DatePicker;

import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;

import java.util.ArrayList;
import java.util.List;
import java.util.Calendar;
import java.util.Objects;

public class LessorPage extends AppCompatActivity {

    private Button viewCategories;
    private Button backToMainPage;
    private Spinner spinner2;
    List<String> categoriesList = new ArrayList<>();
    FirebaseDatabase database = FirebaseDatabase.getInstance();
    DatabaseReference databaseRef = database.getReference("categories");
    DatabaseReference databaseRef2 = database.getReference("items");
    DatabaseReference reference;
    Button buttonAddItem;
    EditText editTextName3;
    EditText editTextDescription;
    EditText editTextFee;
    EditText editStartDate;
    EditText editEndDate;
    Button buttonEditItem;
    Button checkRequest;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_lessor_main_page);
        ViewCompat.setOnApplyWindowInsetsListener(findViewById(R.id.main), (v, insets) -> {
            Insets systemBars = insets.getInsets(WindowInsetsCompat.Type.systemBars());
            v.setPadding(systemBars.left, systemBars.top, systemBars.right, systemBars.bottom);
            return insets;

        });
        viewCategories = findViewById(R.id.viewCategories);
        backToMainPage = findViewById(R.id.buttonDelete);
        spinner2 = findViewById(R.id.spinner2);
        buttonAddItem = findViewById(R.id.buttonUpdateItem);
        buttonEditItem = findViewById(R.id.buttonEditItem);
        editTextName3 = findViewById(R.id.editTextName3);
        editTextDescription = findViewById(R.id.editTextDescription);
        editTextFee = findViewById(R.id.editFee);
        editStartDate = findViewById(R.id.editTextDate1);
        editEndDate = findViewById(R.id.editTextDate2);
        checkRequest = findViewById(R.id.buttoncheckRequest);


        viewCategories.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(LessorPage.this, CategoryPage.class);
                startActivity(intent);
            }
        });

        backToMainPage.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(LessorPage.this, WelcomePage.class);
                startActivity(intent);
            }
        });

        buttonAddItem.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                addItem();
            }
        });

        buttonEditItem.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                if(!validateEntry()){
                    showToast("Enter the name of the desired item you wish to edit");
                    return;

                }
                else{

                    lessorEditor();
                }


            }
        });

        editStartDate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                pickDate(editStartDate);
            }
        });

        editEndDate.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                pickDate(editEndDate);
            }
        });

        checkRequest.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(LessorPage.this, RequestPage.class);
                startActivity(intent);
            }
        });

        loadCategory();
    }

    private void loadCategory() {
        databaseRef.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                categoriesList.clear();
                for (DataSnapshot dataSnapshot : snapshot.getChildren()) {
                    String categoryName = dataSnapshot.child("categoryName").getValue(String.class);
                    if (categoryName != null){
                    categoriesList.add(categoryName);}
                }
                ArrayList<String> adapter = new ArrayList<>(categoriesList);
                ArrayAdapter<String> adapter2 = new ArrayAdapter<>(LessorPage.this, android.R.layout.simple_spinner_item, adapter);
                adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
                spinner2.setAdapter(adapter2);
                Log.d("Firebase", "Categories: " + categoriesList);
            }



            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Log.e("Firebase", "Failed to read categories", error.toException());
            }
        });

    }


    private void addItem() {
        String selectedCategory = spinner2.getSelectedItem().toString();
        String name = editTextName3.getText().toString().trim();
        String description = editTextDescription.getText().toString().trim();
        String fee = editTextFee.getText().toString().trim();
        String startDate = editStartDate.getText().toString().trim();
        String endDate = editEndDate.getText().toString().trim();
        String ownerID = getOwnerID();
        if (name.isEmpty() || description.isEmpty() || fee.isEmpty() || startDate.isEmpty() || endDate.isEmpty()) {
            Toast.makeText(this, "Please fill in all fields", Toast.LENGTH_SHORT).show();
            return;
        }
        if (selectedCategory.isEmpty()) {
            Toast.makeText(this, "Please select a category", Toast.LENGTH_SHORT).show();
            return;
        }



        String id = databaseRef2.push().getKey();
        Item item = new Item(id, name, description, fee, startDate, endDate, selectedCategory, ownerID);
        databaseRef2.child(id).setValue(item);
        Toast.makeText(this, "Item added successfully", Toast.LENGTH_SHORT).show();
        editTextName3.setText("");
        editTextDescription.setText("");
        editTextFee.setText("");
        editStartDate.setText("");
        editEndDate.setText("");



    }

    private String getOwnerID() {
        return Objects.requireNonNull(FirebaseAuth.getInstance().getCurrentUser()).getUid();
    }


    private void pickDate(EditText dateField) {
        Calendar c = Calendar.getInstance();
        int year = c.get(Calendar.YEAR);
        int month = c.get(Calendar.MONTH);
        int day = c.get(Calendar.DAY_OF_MONTH);
        DatePickerDialog datePickerDialog = new DatePickerDialog(
            LessorPage.this, new DatePickerDialog.OnDateSetListener() {
                @Override public void onDateSet(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
                    dateField.setText(dayOfMonth + "-" + (monthOfYear + 1) + "-" + year);
                }
            }, year, month, day);
        datePickerDialog.show();
    }

    public boolean validateEntry(){
        String itemn = editTextName3.getText().toString();

        if(itemn.isEmpty()){
            editTextName3.setError("Field cannot be empty");
            return false;
        }
        else{
            editTextName3.setError(null);
            return true;
        }
    }
    private void lessorEditor(){
        String item_Entered = editTextName3.getText().toString().trim();

        reference = FirebaseDatabase.getInstance().getReference("items");
        Query checkItem = reference.orderByChild("itemName").equalTo(item_Entered);

        checkItem.addListenerForSingleValueEvent(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                if(snapshot.exists()){
                    editTextName3.setError(null);

                    for(DataSnapshot itemsnapshot:snapshot.getChildren()){
                        String itemName = itemsnapshot.child("itemName").getValue(String.class);
                        if(itemName!=null&&itemName.equals(item_Entered)){
                            editTextName3.setError(null);
                            String endDate= itemsnapshot.child("endDate").getValue(String.class);
                            String startDate=itemsnapshot.child("startDate").getValue(String.class);
                            String itemDescription=itemsnapshot.child("description").getValue(String.class);
                            String fee=itemsnapshot.child("fee").getValue(String.class);
                            String category=itemsnapshot.child("categoryName").getValue(String.class);

                            Intent intent = new Intent(LessorPage.this, LessorEditor.class);

                            intent.putExtra("itemName", itemName);
                            intent.putExtra("categoryName", category);
                            intent.putExtra("description", itemDescription);
                            intent.putExtra("endDate", endDate);
                            intent.putExtra("startDate", startDate);
                            intent.putExtra("fee", fee);

                            startActivity(intent);

                        }
                    }
                }
                else{
                    editTextName3.setError("No such item exists");
                    editTextName3.requestFocus();
                }
            }

            @Override
            public void onCancelled(@NonNull DatabaseError error) {

            }
        });

    }

    public void showToast(String message){
        Toast.makeText(LessorPage.this, message, Toast.LENGTH_SHORT).show();
    }

}