import React from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";

const About = () => {
  return (
    <div className='h-98 w-98'>
      <Header />
      <div className='flex justify-center items-center h-1/5 my-8 intro'>
        We are a team of enthusiastic individuals united for a common cause.
        <br />
        The pursuit of our undying love for coding.
      </div>
      <div className='flex flex-col justify-center items-center w-full members'>
        Presenting to you, <b>Our Team Members</b>
        <div className='w-3/5 grid grid-cols-3 items-center mt-4 mb-16'>

          <div className=' m-4 p-4 bg-gray-100  items-center justify-between font-semibold flex flex-col'>
              <img
                src='./1586501225793.jpg'
                className='h-64 mb-2 justify-center'
                alt='profile' 
              />
              <p>Ashwath Niranjh</p>
          </div>

          <div className=' m-4 p-4 bg-gray-100  items-center justify-between font-semibold flex flex-col'>
              <img
                src='./arnpic.jpeg'
                className='h-64 mb-2 justify-center'
                alt='profile' 
              />
              <p>Arnav Menon</p>
          </div>

          <div className=' m-4 p-4 bg-gray-100  items-center justify-between font-semibold flex flex-col'>
              <img
                src='./babypic.jpeg'
                className='h-64 mb-2 justify-center'
                alt='profile' 
              />
              <p>Hari Rahul</p>
          </div>

          <div className=' m-4 p-4 bg-gray-100  items-center justify-between font-semibold flex flex-col'>
              <img
                src='./pradpic.jpg'
                className='h-64 mb-2 justify-center'
                alt='profile' 
              />
              <p>Pradeep S</p>
          </div>

          <div className=' m-4 p-4 bg-gray-100  items-center justify-between font-semibold flex flex-col'>
              <img
                src='./selpic.jpeg'
                className='h-64 mb-2 justify-center'
                alt='profile' 
              />
              <p>Selva Karthik</p>
          </div>

          <div className=' m-4 p-4 bg-gray-100  items-center justify-between font-semibold flex flex-col'>
              <img
                src='./tharpic.jpeg'
                className='h-64 mb-2 justify-center'
                alt='profile' 
              />
              <p>Tharun A</p>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default About;
