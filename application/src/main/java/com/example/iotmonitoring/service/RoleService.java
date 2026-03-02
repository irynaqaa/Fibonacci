package com.example.iotmonitoring.service;

import org.springframework.stereotype.Service;
import java.util.HashMap;
import java.util.Map;

@Service
public class RoleService {
    private final Map<String, String[]> rolePermissions = new HashMap<>();

    public RoleService() {
        // Define user roles and their permissions
        rolePermissions.put("ROLE_ADMIN", new String[]{"READ", "WRITE", "DELETE"});
        rolePermissions.put("ROLE_USER", new String[]{"READ"});
        rolePermissions.put("ROLE_GUEST", new String[]{"READ"});
    }

    public String[] getPermissions(String role) {
        return rolePermissions.getOrDefault(role, new String[]{});
    }
}