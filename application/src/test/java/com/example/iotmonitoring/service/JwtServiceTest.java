package com.example.iotmonitoring.service;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;

import java.util.Date;

import static org.junit.jupiter.api.Assertions.*;

/**
 * Unit tests for the JwtService class, testing JWT generation and validation.
 */
class JwtServiceTest {

    private JwtService jwtService;

    @BeforeEach
    void setUp() {
        jwtService = new JwtService();
    }

    /**
     * Test the generation of JWT tokens with correct claims.
     */
    @Test
    void testGenerateToken() {
        String username = "testUser";
        String role = "ROLE_USER";
        String token = jwtService.generateToken(username, role);

        // Validate token structure
        assertNotNull(token);
        assertTrue(token.startsWith("eyJ")); // JWT tokens start with "eyJ"

        // Validate claims
        Claims claims = Jwts.parser()
                .setSigningKey(System.getenv("JWT_SECRET_KEY"))
                .parseClaimsJws(token)
                .getBody();
        assertEquals(username, claims.getSubject());
        assertEquals(role, claims.get("role"));
    }

    /**
     * Test the validation of a valid token.
     */
    @Test
    void testValidateToken_Valid() {
        String username = "testUser";
        String role = "ROLE_USER";
        String token = jwtService.generateToken(username, role);

        assertTrue(jwtService.validateToken(token, username));
    }

    /**
     * Test the validation of an invalid token.
     */
    @Test
    void testValidateToken_Invalid() {
        String username = "testUser";
        String token = "invalidToken";

        assertFalse(jwtService.validateToken(token, username));
    }

    /**
     * Test the validation of an expired token.
     */
    @Test
    void testValidateToken_Expired() throws InterruptedException {
        String username = "testUser";
        String role = "ROLE_USER";
        String token = jwtService.generateToken(username, role);

        // Simulate token expiration
        Thread.sleep(86400001); // Sleep for 1 day + 1 ms

        assertFalse(jwtService.validateToken(token, username));
    }

    /**
     * Test the extraction of username from token.
     */
    @Test
    void testExtractUsername() {
        String username = "testUser";
        String role = "ROLE_USER";
        String token = jwtService.generateToken(username, role);

        assertEquals(username, jwtService.extractUsername(token));
    }
}
