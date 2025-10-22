const express = require('express');
const router = express.Router();
const petController = require('../controllers/petController');

router.get('/pets', petController.getPets);
router.post('/pets', petController.createPet);
router.get('/pets/:petId', petController.getPetById);

module.exports = router;