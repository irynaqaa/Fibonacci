import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.ComboBox;
import javafx.scene.control.DatePicker;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.FontPosture;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.time.LocalDate;

public class AddTransactionForm extends Application {
    @Override
    public void start(Stage primaryStage) {
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        Text scenetitle = new Text("Add Transaction");
        scenetitle.setFont(Font.font("Tahoma", FontWeight.NORMAL, FontPosture.REGULAR, 20));
        grid.add(scenetitle, 0, 0, 2, 1);

        Label amountLabel = new Label("Amount:");
        grid.add(amountLabel, 0, 1);

        TextField amountField = new TextField();
        grid.add(amountField, 1, 1);

        Label categoryLabel = new Label("Category:");
        grid.add(categoryLabel, 0, 2);

        ComboBox<String> categoryField = new ComboBox<>();
        categoryField.getItems().addAll("Food", "Transportation", "Housing");
        grid.add(categoryField, 1, 2);

        Label dateLabel = new Label("Date:");
        grid.add(dateLabel, 0, 3);

        DatePicker dateField = new DatePicker();
        grid.add(dateField, 1, 3);

        Label descriptionLabel = new Label("Description:");
        grid.add(descriptionLabel, 0, 4);

        TextField descriptionField = new TextField();
        grid.add(descriptionField, 1, 4);

        Label typeLabel = new Label("Type:");
        grid.add(typeLabel, 0, 5);

        ComboBox<String> typeField = new ComboBox<>();
        typeField.getItems().addAll("Income", "Expense");
        grid.add(typeField, 1, 5);

        Button addButton = new Button("Add");
        HBox hbBtn = new HBox(10);
        hbBtn.setAlignment(Pos.BOTTOM_RIGHT);
        hbBtn.getChildren().add(addButton);
        grid.add(hbBtn, 1, 6);

        addButton.setOnAction(event -> {
            try {
                Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/transactions", "root", "password");
                PreparedStatement stmt = conn.prepareStatement("INSERT INTO transactions (amount, category, date, description, type) VALUES (?, ?, ?, ?, ?)");
                stmt.setDouble(1, Double.parseDouble(amountField.getText()));
                stmt.setString(2, categoryField.getValue());
                stmt.setString(3, dateField.getValue().toString());
                stmt.setString(4, descriptionField.getText());
                stmt.setString(5, typeField.getValue());
                stmt.executeUpdate();
                conn.close();
            } catch (SQLException ex) {
                System.out.println(ex.getMessage());
            }
        });

        Scene scene = new Scene(grid, 300, 275);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}