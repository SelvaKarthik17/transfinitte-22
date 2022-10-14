import React from "react";

const Header = () => {
  return (
    <>
      <div className='flex justify-between items-center bg-gray-100 p-4'>
        <div className='logo'>family tree</div>
        <div className='navs'>
          <ul className='flex flex-row items-center'>
            <li className='ml-3'>Home</li>
            <li className='ml-3'>Contact</li>
          </ul>
        </div>
      </div>
    </>
  );
};

export default Header;
