package com.example.iotmonitoring.controller;

import com.example.iotmonitoring.service.JwtService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/auth")
public class AuthController {

    @Autowired
    private JwtService jwtService;

    @PostMapping("/login")
    public ResponseEntity<String> login(@RequestParam String username, @RequestParam String password) {
        // Validate user credentials (this should be replaced with actual user validation)
        if (username.equals("admin") && password.equals("password")) {
            String token = jwtService.generateToken(username, "ROLE_ADMIN");
            return ResponseEntity.ok(token);
        }
        return ResponseEntity.status(401).body("Unauthorized");
    }
}
