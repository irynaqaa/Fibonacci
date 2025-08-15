public class TransactionValidator {
    public boolean isValidTransaction(Transaction transaction) {
        // Check if the transaction is not null
        if (transaction == null) {
            return false;
        }
        // Check if the transaction type is valid
        if (!transaction.getType().equals("income") && !transaction.getType().equals("expense")) {
            return false;
        }
        // Check if the transaction amount is valid
        if (transaction.getAmount() <= 0) {
            return false;
        }
        return true;
    }
}