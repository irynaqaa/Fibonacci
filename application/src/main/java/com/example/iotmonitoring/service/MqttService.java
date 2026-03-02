package com.example.iotmonitoring.service;

import org.eclipse.paho.client.mqttv3.*;
import org.springframework.stereotype.Service;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

@Service
public class MqttService implements MqttCallback {
    private static final Logger logger = LoggerFactory.getLogger(MqttService.class);
    private MqttClient client;

    public MqttService() throws MqttException {
        client = new MqttClient("tcp://broker.hivemq.com:1883", MqttClient.generateClientId());
        client.setCallback(this);
        client.connect();
        client.subscribe("iot/data");
    }

    @Override
    public void connectionLost(Throwable cause) {
        logger.warn("Connection lost: {}", cause.getMessage());
    }

    @Override
    public void messageArrived(String topic, MqttMessage message) throws Exception {
        logger.info("Message received: {}", new String(message.getPayload()));
        // Process the message here
    }

    @Override
    public void deliveryComplete(IMqttDeliveryToken token) {
        // Handle delivery completion
    }
}