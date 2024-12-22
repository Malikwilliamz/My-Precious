package com.example.myapplication;

import android.app.DatePickerDialog;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.os.Build;
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
import androidx.activity.result.ActivityResultLauncher;
import androidx.activity.result.contract.ActivityResultContracts;
import androidx.annotation.NonNull;
import androidx.core.content.ContextCompat;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

import com.google.firebase.database.DataSnapshot;
import com.google.firebase.database.DatabaseError;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.google.firebase.database.Query;
import com.google.firebase.database.ValueEventListener;
import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;

public class RentedItems extends AppCompatActivity {
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_rented_items_page);

        //equestPermission();
    }

//    private ActivityResultLauncher<String> resultLauncher = registerForActivityResult(
//            new ActivityResultContracts.RequestPermission(), isGranted -> {
//                if(isGranted){
//                    //permission Granted
//                }
//                else{
//                    //Permission denied
//                }
//            }
//    )
//
//    public void requestPermission(){
//        if(Build.VERSION.SDK_INT>=Build.VERSION_CODES.TIRAMISU){
//            if(ContextCompat.checkSelfPermission(this, Manifest.permission.POST_NOTIFICATIONS)==
//            PackageManager.PERMISSION_GRANTED){
//                //Permission Already Granted
//
//            }
//            else if(shouldShowRequestPermissionRationale(Manifest.permission.POST_NOTIFICATIONS)){
//
//            }
//            else{
//                resultLauncher.launch(Manifest.permission.POST_NOTIFICATIONS);
//            }
//
//        }
//    }

}
