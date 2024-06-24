import { useState } from 'react';
import axios from "axios";
import Footer from './Footer';
import Navbar from './Navbar';
import Lottie from 'react-lottie';
import animationData from '../../public/job_lottie.json';
import { arrayOf } from 'prop-types';

const defaultOptions = {
  loop: true,
  autoplay: true,
  animationData: animationData,
  rendererSettings: {
    preserveAspectRatio: 'xMidYMid slice',
  },
};

function SignUp() {

  const [email, setEmail] = useState('');
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [data, setData] = useState([{}])


  const handleSubmit = (e:any) => {
    e.preventDefault()
    const postData = async () => {
      try{
        const Data = 
        {
          "username":username
        }
        const response = await axios.post("/signup",
          Data
        )
      }
      catch(error){
        console.log(error)
      }
      finally{
        console.log("ola")
      }
      postData()

    }

    
  }

  return (
    <>
      <Navbar />
      <div className="flex-col bg-gradient-to-tr from-[#000000]  to-[#1a2a47] ">
        <div className="grid grid-cols-2 ">
          {/* left_screen */}
          <div className="text-6xl  flex flex-col justify-center items-center my-4">
            <img
              className=" m-4 max-h-11"
              src="../public/logoipsum.svg"
              alt=""
            />
            <div className="text-4xl w-3/4 flex-col justify-center text-center m-4">
              <form onSubmit={handleSubmit}>
                <div className="text-3xl text-center flex flex-col items-center bg-[#52515f] p-4 m-4 rounded-3xl shadow-default ">
                  <h6 className="mb-4">Create an account</h6>

                  <label htmlFor="username" className="font-mono text-2xl">
                    select an username
                  </label>
                  <input type="text" id='userId' value={username} onChange={(e)=> setUsername(e.target.value)} placeholder=''  />

                  <label htmlFor="email" className="font-mono text-2xl">
                    your email
                  </label>
                  <input id="email" className="" type="email" value={email} onChange={(e) => setEmail(e.target.value)} />

                  <label htmlFor="password" className="font-mono text-2xl">
                    password
                  </label>
                  <input id="password" type="password" value={password} onChange={(e)=>setPassword(e.target.value)} />

                  <label htmlFor="confirmPassword" className="font-mono text-2xl">
                    confirm password
                  </label>
                  <input id="confirmPassword" type="password" value={confirmPassword} onChange={(e)=>setConfirmPassword(e.target.value)} />

                  <button className="">Sign up</button>
                </div>
              </form>
            </div>
          </div>
          {/* right_screen */}
          <div className="">
            {/* <div className="h-screen flex items-center justify-center">
              <img
                src="../public/logoipsum.svg"
                alt="Logo"
                style={{ height: "150px", width:"150px"}} 
              />
            </div> */}
            <div className=" h-screen flex justify-center items-center mt-35 ">
              <div className="max-w-4xl h-3/5">
                <h1 className="animate-typing overflow-hidden whitespace-nowrap border-r-4 border-r-white p-4 m-4 text-5xl text-white font-bold">
                  okay!! let's get started.. rn!
                </h1>
                <div>
                  <Lottie options={defaultOptions} height={500} width={500} />
                </div>
              </div>
            </div>
          </div>
        </div>
        <Footer />
      </div>
    </>
  );
}
export default SignUp;
