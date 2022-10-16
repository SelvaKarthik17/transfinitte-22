import React from "react";
import { Link } from "react-router-dom";
const Header = () => {
  return (
    <>
      <div className='flex justify-between items-center bg-gray-100 p-4'>
        <div className='logo'>
          <Link to='/'><p className="text-xl">Family Ties</p></Link>
        </div>
        <div className='navs'>
          <ul className='flex flex-row items-center'>
            <li className='ml-3'>
              <Link to='/about'><p className="text-xl">About Us</p></Link>
            </li>
          </ul>
        </div>
      </div>
    </>
  );
};

export default Header;
