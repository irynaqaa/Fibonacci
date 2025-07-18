package com.example.personalexpensetracker;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * Personal Expense Tracker Application. This is the main application class.
 */
@SpringBootApplication
public final class PersonalExpenseTrackerApplication {

    /**
     * Main method to run the application. This method is used to
     * start the application.
     * @param args command line arguments.
     */
    public static void main(final String[] args) {
        SpringApplication.run(PersonalExpenseTrackerApplication.class, args);
    }

    // Private constructor to prevent instantiation
    private PersonalExpenseTrackerApplication() {
    }
}