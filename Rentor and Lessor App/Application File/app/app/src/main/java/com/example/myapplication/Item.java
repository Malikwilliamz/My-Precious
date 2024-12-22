package com.example.myapplication;

import java.util.HashMap;
import java.util.Map;
public class Item {
    private String _id;
    private String _itemName;
    private String _fee;
    private String _description;
    private String _startDate;
    private String _endDate;
    private String _category;
    private String _ownerID;

    public Item(String id, String itemName, String description, String category) {
        _id = id;
        _itemName = itemName;
        _description = description;
        _category = category;
    }

    public Item(String id, String itemName, String description, String fee, String startDate, String endDate, String selectedCategory, String ownerID) {
        _id = id;
        _itemName = itemName;
        _description = description;
        _fee = fee;
        _startDate = startDate;
        _endDate = endDate;
        _category = selectedCategory;
        _ownerID = ownerID;
    }



    public void setItemName(String itemName) {
        _itemName = itemName;
    }

    public String getItemName() {
        return _itemName;
    }

    public void setFee(String fee) {
        _fee = fee;
    }

    public String getFee() {
        return _fee;
    }

    public void setId(String id) {
        _id = id;
    }

    public String getId() {
        return _id;
    }

    public void setCategory(String category) {
        _category = category;
    }

    public String getCategoryName() {
        return _category ;
    }

    public void setDescription(String description) {
        _description = description;
    }

    public String getDescription() {
        return _description;
    }

    public void setStartDate(String newStartDate) {_startDate = newStartDate;}

    public String getStartDate() {return _startDate;}

    public void setEndDate(String newEndDate) {_endDate = newEndDate;}

    public String getEndDate() {return _endDate;}

    public String getOwnerID() {
        return _ownerID;
    }

    public void setOwnerId(String ownerId) {
        this._ownerID = ownerId;
    }

    public Map<String, Object> toMap() {
        HashMap<String, Object> result = new HashMap<>();
        result.put("itemName", getItemName());
        result.put("categoryName", getCategoryName());
        result.put("description", getDescription());
        result.put("startDate", getStartDate());
        result.put("endDate", getEndDate());
        result.put("fee", getFee());
        result.put("id", getId());
        result.put("ownerID", getOwnerID());
        return result;
    }


}