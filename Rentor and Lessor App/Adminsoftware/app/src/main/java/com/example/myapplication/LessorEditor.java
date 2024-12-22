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
import java.util.List;
import java.util.Calendar;
import java.util.Objects;

public class LessorEditor extends AppCompatActivity{
    EditText editStartDate;
    EditText editEndDate;
    Button update;
    Button delete;
    FirebaseDatabase database;
    DatabaseReference databaseReference;
    List<String> categoriesList = new ArrayList<>();
    Button backToLessorPage;
    EditText editName;
    EditText editDescription;
    EditText editFee;
    Spinner category_spin;
    ArrayAdapter<String> adapter2;


    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.lessor_edit);


        database = FirebaseDatabase.getInstance();
        databaseReference = database.getReference().child("items");
        editStartDate = findViewById(R.id.editTextDate1);
        editEndDate = findViewById(R.id.editTextDate2);
        update = findViewById(R.id.buttonUpdateItem);
        delete = findViewById(R.id.buttonDelete);
        editName = findViewById(R.id.editTextName3);
        editDescription = findViewById(R.id.editTextDescription);
        editFee = findViewById(R.id.editFee);
        category_spin = findViewById(R.id.spinner2);

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

        delete.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String itemEntered = editName.getText().toString();
                Query query = databaseReference.orderByChild("itemName").equalTo(itemEntered);

                query.addListenerForSingleValueEvent(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot snapshot) {
                        if(snapshot.exists()){
                            for(DataSnapshot itemSnapshot:snapshot.getChildren()){
                                String id = itemSnapshot.getKey();
                                deleteItem(id);
                                editName.setText("");
                                //category_spin.setSelection(5);
                                editFee.setText("");
                                editDescription.setText("");
                                editStartDate.setText("");
                                editEndDate.setText("");

                            }
                        }
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError error) {

                    }
                });
            }
        });

        update.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                String itemEntered = editName.getText().toString();
                Query query = databaseReference.orderByChild("itemName").equalTo(itemEntered);

                query.addValueEventListener(new ValueEventListener() {
                    @Override
                    public void onDataChange(@NonNull DataSnapshot snapshot) {
                        if(snapshot.exists()){
                            for(DataSnapshot itemSnapshot: snapshot.getChildren()){
                                String id = itemSnapshot.getKey();
                                String newitemName = editName.getText().toString();
                                String newendDate= editEndDate.getText().toString();
                                String newstartDate=editStartDate.getText().toString();
                                String newitemDescription=editDescription.getText().toString();
                                String newfee=editFee.getText().toString();
                                String newcategory=category_spin.getSelectedItem().toString();

                                saveData(id, newitemName,newendDate, newstartDate, newitemDescription,
                                        newfee, newcategory);
                            }
                        }
                        else {
                            showToast("Enter valid name");
                        }
                        startActivity(new Intent(LessorEditor.this, LessorPage.class));
                    }

                    @Override
                    public void onCancelled(@NonNull DatabaseError error) {

                    }
                });
            }
        });

        loadCategory();
        showItem();



    }

    private void pickDate(EditText dateField) {
        Calendar c = Calendar.getInstance();
        int year = c.get(Calendar.YEAR);
        int month = c.get(Calendar.MONTH);
        int day = c.get(Calendar.DAY_OF_MONTH);
        DatePickerDialog datePickerDialog = new DatePickerDialog(
                LessorEditor.this, new DatePickerDialog.OnDateSetListener() {
            @Override public void onDateSet(DatePicker view, int year, int monthOfYear, int dayOfMonth) {
                dateField.setText(new StringBuilder().append(dayOfMonth).append("-").append(monthOfYear + 1).append("-").append(year).toString());
            }
        }, year, month, day);
        datePickerDialog.show();
    }

    private void deleteItem(String id){
        databaseReference = FirebaseDatabase.getInstance().getReference("items").child(id);
        Task<Void> mTask = databaseReference.removeValue();
        mTask.addOnSuccessListener(new OnSuccessListener<Void>() {
            @Override
            public void onSuccess(Void unused) {
                showToast("Deleted");
            }
        });
    }

    public void showToast(String message){
        Toast.makeText(LessorEditor.this, message, Toast.LENGTH_SHORT).show();
    }


public void showItem(){
        Intent intent = getIntent();

        String endDate= intent.getStringExtra("endDate");
        String startDate=intent.getStringExtra("startDate");
        String itemDescription=intent.getStringExtra("description");
        String fee=intent.getStringExtra("fee");
        String category=intent.getStringExtra("categoryName");
        String itemName= intent.getStringExtra("itemName");

        //int selected = getIndex(category_spin,category);

        editName.setText(itemName);
        //category_spin.setSelection(5);
        editFee.setText(fee);
        editDescription.setText(itemDescription);
        editStartDate.setText(startDate);
        editEndDate.setText(endDate);



    }


    public int getIndex(Spinner spin, String spinVal){
        for(int i=0;i<spin.getCount();i++){
            if(spin.getItemAtPosition(i).toString().equals(spinVal)){
                return i;
            }
        }
        return 2;

    }

    public void loadCategory(){
        //spinner functionality
        databaseReference = database.getReference("categories");
        databaseReference.addValueEventListener(new ValueEventListener() {
            @Override
            public void onDataChange(@NonNull DataSnapshot snapshot) {
                categoriesList.clear();
                for (DataSnapshot dataSnapshot : snapshot.getChildren()) {
                    String categoryName = dataSnapshot.child("categoryName").getValue(String.class);
                    if (categoryName != null){
                        categoriesList.add(categoryName);}
                }
                ArrayList<String> adapter = new ArrayList<>(categoriesList);
                adapter2 = new ArrayAdapter<>(LessorEditor.this, android.R.layout.simple_spinner_item, adapter);
                category_spin.setAdapter(adapter2);
                Log.d("Firebase", "Categories: " + categoriesList);
            }



            @Override
            public void onCancelled(@NonNull DatabaseError error) {
                Log.e("Firebase", "Failed to read categories", error.toException());
            }
        });

    }

    public void saveData(String id, String newitemName,String newendDate, String newstartDate, String newitemDescription,
                         String newfee, String newcategory){

        String ownerId = Objects.requireNonNull(FirebaseAuth.getInstance().getCurrentUser()).getUid();
        DatabaseReference ref = FirebaseDatabase.getInstance().getReference("items").child(id);
        Item item = new Item(id, newitemName, newitemDescription, newfee, newstartDate, newendDate, newcategory,ownerId);
        ref.setValue(item.toMap());
        showToast("ITEM UPDATED");

    }



}
