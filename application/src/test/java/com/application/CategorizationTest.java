package com.application;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import static org.junit.Assert.assertNotNull;

@RunWith(SpringRunner.class)
@SpringBootTest
public class CategorizationTest {

    @Autowired
    private CategoryService categoryService;

    @Test
    public void testCreateCategory() {
        Category category = new Category();
        category.setName("Food");
        category.setDescription("Food expenses");
        Category createdCategory = categoryService.createCategory(category);
        assertNotNull(createdCategory);
    }

    @Test
    public void testGetCategory() {
        Category category = new Category();
        category.setName("Food");
        category.setDescription("Food expenses");
        Category createdCategory = categoryService.createCategory(category);
        assertNotNull(createdCategory);
        Category retrievedCategory = categoryService.getCategory(createdCategory.getId());
        assertNotNull(retrievedCategory);
    }
}
