package com.example.myapplication;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.List;

public class CategoryList extends ArrayAdapter<Category> {
    private Activity context;
    List<Category> categories;
    public CategoryList(Activity context,List<Category> categories){
        super(context,R.layout.user_list,categories);
        this.context=context;
        this.categories=categories;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent){
        View listViewItem = convertView;
        if (listViewItem == null) {
            LayoutInflater inflater = context.getLayoutInflater();
            listViewItem = inflater.inflate(R.layout.user_list, parent, false); // use parent for proper inflation
        }

        TextView name = (TextView) listViewItem.findViewById(R.id.textView10);
        TextView desc = (TextView) listViewItem.findViewById(R.id.textView11);

        Category category = categories.get(position);

        name.setText("Name: " + category.getCategoryName());
        desc.setText("Description: " + category.getDescription());
        return listViewItem;
    }
}
