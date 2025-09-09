public class Main {
    public static void main(String[] args) {
        Database.createTable();

        Transaction transaction = new Transaction(1, 100.0, 1, "sale", "2022-01-01");
        Database.insertTransaction(transaction);

        Database.selectTransactions();
    }
}