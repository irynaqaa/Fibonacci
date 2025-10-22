const request = require('supertest');
const app = require('../index');

describe('Pet Controller', () => {
  it('should fetch pets', async () => {
    const res = await request(app).get('/pets');
    expect(res.statusCode).toEqual(200);
  });

  it('should create a pet', async () => {
    const res = await request(app)
      .post('/pets')
      .send({ name: 'Buddy', age: 3, type: 'Dog' });
    expect(res.statusCode).toEqual(201);
  });

  it('should fetch a pet by ID', async () => {
    const res = await request(app).get('/pets/1');
    expect(res.statusCode).toEqual(200);
  });
});
