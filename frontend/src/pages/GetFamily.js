import React, { Component } from 'react';
import Footer from '../components/Footer';
import Header from '../components/Header';
import { LockClosedIcon } from '@heroicons/react/solid'
export default function GetFamily() {

    const [states, setStates] = React.useState(["Tamil Nadu"]);

    return (
            <div>
                <form className='flex flex-col items-center justify-center m-2'>
                <div className='w-3/5 m-2 flex justify-around items-center'>
                <label for="name">Enter your name:</label>
                    <input required name='name' type="text" placeholder="Enter name" className='p-2 border  border-3 rounded-md' />
                    </div>
                    <div className='w-3/5 m-2 flex justify-around items-center'>
                <label for="fatherName">Enter your Father's name:</label>
                    <input required name = 'fatherName' type="text" placeholder="Enter name" className='p-2 border  border-3 rounded-md' />
                    </div><div className='w-3/5 m-2 flex justify-around items-center'>
                <label for="">Enter your state:</label>
                    <input required name = 'state' type="text" placeholder="Enter name" className='p-2 border  border-3 rounded-md' />
                    </div><div className='w-3/5 m-2 flex justify-around items-center'>
                <label for="age">Enter your age:</label>
                    <input required type="text" placeholder="Enter name" className='p-2 border  border-3 rounded-md' />
                    </div>
                    <div className='w-3/5 m-2 flex justify-around items-center'>
                <label for="">Enter your voter ID:</label>
                    <input name = 'voterId' type="text" placeholder="Enter name" className='p-2 border  border-3 rounded-md' />
                    </div>
                    <div className='w-3/5 m-2 flex justify-around items-center'>
                <label for="gender">Enter your gender:</label>
                <select className='p-2 border border-1 w-1/5'>
                    <option value="male">male</option>
                    <option value="female">female</option>
                </select>
                    </div>
                    
                    <input type="submit" value="Submit" className='py-3 px-4 rounded-md bg-blue-500 text-gray-50 hover:bg-blue-700' />  
                </form>
            </div>
    );
}