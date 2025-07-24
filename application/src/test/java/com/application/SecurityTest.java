package com.application;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.security.test.context.support.WithMockUser;
import org.springframework.test.context.junit4.SpringRunner;

import static org.junit.Assert.assertNotNull;

@RunWith(SpringRunner.class)
@SpringBootTest
public class SecurityTest {

    @Autowired
    private SecurityConfig securityConfig;

    @Test
    @WithMockUser(username = "user", roles = "USER")
    public void testSecurityConfig() {
        assertNotNull(securityConfig);
    }
}
