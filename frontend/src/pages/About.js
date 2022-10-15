import React from "react";
import Footer from "../components/Footer";
import Header from "../components/Header";

const About = () => {
  return (
    <div className='h-98 w-98'>
      <Header />
      <div className='flex justify-center items-center h-1/5 intro'>
        We are a team of enthusiastic individuals united for a common cause.
        <br />
        The pursuit of our undying love for coding.
      </div>
      <div className='flex flex-col justify-center items-center w-full members'>
        Presenting to you, our team members
        <div className='w-full flex flex-col items-center'>
          <div className=' my-4 p-4 w-3/4 bg-gray-100 flex items-center justify-between'>
            <img
              src='https://i.ibb.co/whGTTsq/1586501225793.jpg'
              className='h-64 mr-8'
            />
            <div className='desc'>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc
              viverra metus eget turpis rutrum, sit amet ullamcorper leo
              efficitur. Fusce efficitur sapien ac erat dignissim, quis rutrum
              ligula porta. In semper nisi quam, in egestas leo ultrices quis.
              In consectetur ultrices aliquet. Nam posuere pulvinar lorem, in
              fringilla sapien volutpat at.
            </div>
          </div>
          <div className=' my-4 p-4 w-3/4 bg-gray-100 flex items-center justify-between'>
            <img
              src='https://i.ibb.co/whGTTsq/1586501225793.jpg'
              className='h-64 mr-8'
            />
            <div className='desc'>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc
              viverra metus eget turpis rutrum, sit amet ullamcorper leo
              efficitur. Fusce efficitur sapien ac erat dignissim, quis rutrum
              ligula porta. In semper nisi quam, in egestas leo ultrices quis.
              In consectetur ultrices aliquet. Nam posuere pulvinar lorem, in
              fringilla sapien volutpat at.
            </div>
          </div>
          <div className=' my-4 p-4 w-3/4 bg-gray-100 flex items-center justify-between'>
            <img
              src='https://i.ibb.co/whGTTsq/1586501225793.jpg'
              className='h-64 mr-8'
            />
            <div className='desc'>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc
              viverra metus eget turpis rutrum, sit amet ullamcorper leo
              efficitur. Fusce efficitur sapien ac erat dignissim, quis rutrum
              ligula porta. In semper nisi quam, in egestas leo ultrices quis.
              In consectetur ultrices aliquet. Nam posuere pulvinar lorem, in
              fringilla sapien volutpat at.
            </div>
          </div>
        </div>
      </div>
      <Footer />
    </div>
  );
};

export default About;
