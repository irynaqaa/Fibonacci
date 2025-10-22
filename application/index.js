const express = require('express');
const petRoutes = require('./routes/petRoutes');

const app = express();
app.use(express.json());
app.use('/api', petRoutes);

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});