import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import javax.transaction.Transactional;

/**
 * Service class for managing products in the inventory.
 */
@Service
public class ProductService {

    @Autowired
    private ProductRepository productRepository;

    /**
     * Adds a new product to the inventory.
     * @param product the product to add
     * @return confirmation message
     */
    @Transactional
    public String addProduct(Product product) {
        productRepository.save(product);
        return "Product added successfully!";
    }
}