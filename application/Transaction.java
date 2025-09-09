public class Transaction {
    private int id;
    private double amount;
    private int customerID;
    private String transactionType;
    private String transactionDate;

    public Transaction(int id, double amount, int customerID, String transactionType, String transactionDate) {
        this.id = id;
        this.amount = amount;
        this.customerID = customerID;
        this.transactionType = transactionType;
        this.transactionDate = transactionDate;
    }

    // Getters and setters
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public double getAmount() {
        return amount;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public int getCustomerID() {
        return customerID;
    }

    public void setCustomerID(int customerID) {
        this.customerID = customerID;
    }

    public String getTransactionType() {
        return transactionType;
    }

    public void setTransactionType(String transactionType) {
        this.transactionType = transactionType;
    }

    public String getTransactionDate() {
        return transactionDate;
    }

    public void setTransactionDate(String transactionDate) {
        this.transactionDate = transactionDate;
    }
}