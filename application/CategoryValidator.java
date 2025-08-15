public class CategoryValidator {
    public boolean isValidCategory(String category) {
        // Check if the category is not empty and is a string
        if (category == null || category.isEmpty()) {
            return false;
        }
        return true;
    }
}