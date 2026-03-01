import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

/**
 * Controller for handling product-related requests.
 */
@RestController
@RequestMapping("/api/products")
@Validated
public class ProductController {

    @Autowired
    private ProductService productService;

    /**
     * Endpoint to add a new product.
     * @param product the product to add
     * @return response entity with status and message
     */
    @PostMapping
    public ResponseEntity<String> addProduct(@Valid @RequestBody Product product) {
        String message = productService.addProduct(product);
        return new ResponseEntity<>(message, HttpStatus.CREATED);
    }
}