package com.example.myapplication;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.List;

public class UserList extends ArrayAdapter<User> {
    private Activity context;
    List<User> users;
    public UserList(Activity context,List<User> users){
        super(context,R.layout.user_list,users);
        this.context=context;
        this.users=users;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent){
        View listViewItem = convertView;
        if (listViewItem == null) {
            LayoutInflater inflater = context.getLayoutInflater();
            listViewItem = inflater.inflate(R.layout.user_list, parent, false); // use parent for proper inflation
        }

        TextView name = (TextView) listViewItem.findViewById(R.id.textView10);
        TextView role = (TextView) listViewItem.findViewById(R.id.textView11);

        User user = users.get(position);

        name.setText("Name: "+user.getName());
        role.setText("Role: "+user.getRole());
        return listViewItem;
    }
}

