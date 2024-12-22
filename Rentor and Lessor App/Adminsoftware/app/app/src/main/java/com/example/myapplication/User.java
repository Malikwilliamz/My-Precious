package com.example.myapplication;

import java.util.*;

public class User {

    private String name;
    private String userName;
    private String email;
    private String role;
    private String id;
    private boolean isDisabled;


    public User(String name, String userName, String email, String role,String id){
        this.name = name;
        this.userName=userName;
        this.email=email;
        this.role=role;
        this.id = id;
        isDisabled=false;

    }

    public Map<String, Object> toMap() {
        HashMap<String, Object> result = new HashMap<>();
        result.put("name", name);
        result.put("username", userName);
        result.put("email", email);
        result.put("role", role);
        result.put("id",id);
        result.put("disabled",isDisabled);
        return result;
    }

    public void setisDisabled(boolean bool){
        isDisabled=bool;
    }
    public String getName(){
        return name;
    }
    public String getuserName(){
        return userName;
    }
    public String getemail(){
        return email;
    }

    public String getRole() {
        return role;
    }

    public String getId() {
        return id;
    }
    public boolean getisDisabled(){
        return isDisabled;
    }
}
