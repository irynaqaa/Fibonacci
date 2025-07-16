package com.example;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Personal Expense Tracker Application.
 */
@SpringBootApplication
public final class PersonalExpenseTrackerApplication {

    private PersonalExpenseTrackerApplication() {
        // Utility class constructor
    }

    /**
     * Main method to run the application.
     * @param args command line arguments
     */
    public static void main(final String[] args) {
        SpringApplication.run(PersonalExpenseTrackerApplication.class, args);
    }
}
