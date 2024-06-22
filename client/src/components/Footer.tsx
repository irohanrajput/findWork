import { FaInstagram, FaTwitterSquare, FaLinkedin } from "react-icons/fa";

const Footer = () => {
  return (
    <div className="max-w-[1240px] mx-auto py-16 px-4 grid lg:grid-cols-3 gap-8 text-gray-300">
      <div>
        <h1 className="w-full text-3xl font-bold text-[#00df9a]">findWork</h1>
        <p className="py-4">Put your skills into use rn. </p>

        <div className="flex justify-between md:w-[50%] my-6">
          <a
            href="https://www.instagram.com//"
            className="transition duration-300 ease-in-out hover:scale-125"
            target="blank"
          >
            <FaInstagram size={30} />
          </a>
          <a
            href="https://twitter.com/"
            className="transition duration-300 ease-in-out hover:scale-125"
            target="blank"
          >
            <FaTwitterSquare size={30} />
          </a>
          <a
            href="https://github.com//"
            className="transition duration-300 ease-in-out hover:scale-125"
            target="blank"
          >
            <FaLinkedin size={30} />
          </a>
        </div>
      </div>

      <div className="col-span-2 flex justify-between mt-6 text-2xl">
        <div>
          <a href="#">About Us</a>
          <p className=" text-lg">
            <ul>
              <li>founders</li>
              <li>our team</li>
            </ul>
          </p>
        </div>
        <div>
          <a href="#">Contact</a>
          <p className=" text-lg">
            <ul>
              <li>support</li>
              <li>sales</li>
            </ul>
          </p>
        </div>
        <div>
          <a href="#">Legal</a>
          <p className=" text-lg">
            <ul>
              <li>privacy</li>
              <li>terms</li>
            </ul>
          </p>
        </div>

        <div>
          <a href="#">Resources</a>
          <p className=" text-lg">
            <ul>
              <li>blog</li>
              <li>faq</li>
            </ul>
          </p>
          </div>
      </div>
    </div>
  );
};

export default Footer;
