import javax.persistence.*;
import javax.validation.constraints.*;
import java.math.BigDecimal;

/**
 * Represents a product in the inventory.
 */
@Entity
@Table(name = "products")
public class Product {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotNull(message = "Name is required")
    @Size(min = 1, message = "Name must not be empty")
    private String name;

    @NotNull(message = "Description is required")
    @Size(min = 1, message = "Description must not be empty")
    private String description;

    @NotNull(message = "Price is required")
    private BigDecimal price;

    // Getters and Setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public BigDecimal getPrice() {
        return price;
    }

    public void setPrice(BigDecimal price) {
        this.price = price;
    }
}