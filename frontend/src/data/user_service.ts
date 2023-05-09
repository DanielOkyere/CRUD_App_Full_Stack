import axios from "axios";
import { createUserInterface } from "../interfaces";

const SERVER = 'http://localhost:8000'

export async function getAllUsers() {
    const response = await axios.get(`${SERVER}/users`)
    return response.data
}

export async function createUser(data : createUserInterface){
    console.log(data);
    const response = await axios.post(`${SERVER}/users`, data)
    return response.data;
}

export async function deleteUser(id: Number){
    const response = await axios.delete(`${SERVER}/users/${id}`)
    return response.data
}