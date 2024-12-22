package com.example.myapplication;

import android.app.Activity;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ArrayAdapter;
import android.widget.TextView;

import java.util.List;

public class ItemList extends ArrayAdapter<Item> {
    private Activity context;
    List<Item> items;
    public ItemList(Activity context,List<Item> items){
        super(context,R.layout.item_list,items);
        this.context=context;
        this.items=items;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent){
        View listViewItem = convertView;
        if (listViewItem == null) {
            LayoutInflater inflater = context.getLayoutInflater();
            listViewItem = inflater.inflate(R.layout.item_list, parent, false); // use parent for proper inflation
        }

        TextView name = (TextView) listViewItem.findViewById(R.id.textView7);
          TextView desc = (TextView) listViewItem.findViewById(R.id.textView14);
        TextView date = (TextView) listViewItem.findViewById(R.id.textView15);
        TextView fee = (TextView) listViewItem.findViewById(R.id.textView16);
         TextView category = (TextView) listViewItem.findViewById(R.id.textView17);
//
//
        Item item = items.get(position);
//
       name.setText("Name: " + item.getItemName());
        desc.setText("Description: " + item.getDescription());
       date.setText("Date: " + item.getStartDate()+" to "+item.getEndDate());
        fee.setText("Fee: " + item.getFee());
       category.setText("Category: " + item.getCategoryName());
        return listViewItem;
    }
}
