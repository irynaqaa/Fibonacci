import com.example.blockchain.Category;
import com.example.blockchain.CategoryRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class CategoryServiceImpl implements com.example.blockchain.CategoryService {
    @Autowired
    private CategoryRepository categoryRepository;
    @Override
    public void addCategory(Category category) {
        categoryRepository.save(category);
    }
    @Override
    public List<Category> getAllCategories() {
        return categoryRepository.findAll();
    }
    @Override
    public void editCategory(Category category) {
        categoryRepository.save(category);
    }
    @Override
    public void deleteCategory(Long id) {
        categoryRepository.deleteById(id);
    }
}