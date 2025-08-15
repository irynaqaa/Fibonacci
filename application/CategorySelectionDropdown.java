import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.layout.VBox;
import javafx.stage.Modality;
import javafx.stage.Stage;

public class CategorySelectionDropdown extends Application {
    @Override
    public void start(Stage primaryStage) {
        ChoiceBox<String> categoryChoiceBox = new ChoiceBox<>();
        categoryChoiceBox.getItems().addAll("Category 1", "Category 2", "Category 3");

        Button createCategoryButton = new Button("Create Custom Category");
        createCategoryButton.setOnAction(event -> {
            Stage customCategoryStage = new Stage();
            customCategoryStage.initModality(Modality.WINDOW_MODAL);
            customCategoryStage.initOwner(primaryStage);

            javafx.scene.control.TextField customCategoryName = new javafx.scene.control.TextField();
            Button saveCustomCategoryButton = new Button("Save");
            saveCustomCategoryButton.setOnAction(event1 -> {
                String customCategory = customCategoryName.getText();
                try {
                    java.sql.Connection conn = java.sql.DriverManager.getConnection("jdbc:mysql://localhost:3306/transactions", "root", "password");
                    java.sql.Statement stmt = conn.createStatement();
                    stmt.execute("INSERT INTO categories (name) VALUES ('" + customCategory + "')");
                    conn.close();
                } catch (java.sql.SQLException e) {
                    System.out.println(e.getMessage());
                }
                customCategoryStage.close();
            });

            VBox customCategoryLayout = new VBox(10);
            customCategoryLayout.getChildren().addAll(customCategoryName, saveCustomCategoryButton);
            Scene customCategoryScene = new Scene(customCategoryLayout, 200, 100);
            customCategoryStage.setScene(customCategoryScene);
            customCategoryStage.show();
        });

        VBox layout = new VBox(10);
        layout.getChildren().addAll(categoryChoiceBox, createCategoryButton);
        Scene scene = new Scene(layout, 200, 150);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}