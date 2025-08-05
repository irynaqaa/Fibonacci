package com.personal.expense.tracker;

public class Transaction {
    private int id;
    private String date;
    private String category;
    private String type;
    private double amount;
    private String description;

    public Transaction(int id, String date, String category, String type, double amount, String description) {
        this.id = id;
        this.date = date;
        this.category = category;
        this.type = type;
        this.amount = amount;
        this.description = description;
    }

    public int getId() {
        return id;
    }

    public String getDate() {
        return date;
    }

    public String getCategory() {
        return category;
    }

    public String getType() {
        return type;
    }

    public double getAmount() {
        return amount;
    }

    public String getDescription() {
        return description;
    }
}
