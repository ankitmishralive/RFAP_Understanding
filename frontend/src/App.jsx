import { useState,useEffect } from 'react'
import './App.css'

import ContactList from './ContactList'
import ContactForm from './contactForm'

function App() {

  const [contacts,setContacts] = useState([{"firstName":"yo","lastName":"yes","email":"email","id":1}])
  const [isModalOpen,setIsModalOpen] = useState(false)

  useEffect(()=>{
    fetchContacts()
  },[])

  const fetchContacts = async () =>{
      const response = await fetch("http://127.0.0.1:5000/contacts")
      const data = await response.json() 
      setContacts(data.Contacts)
      console.log("Data here :",data.Contacts)
  }

  const openModal =()=>{
  if(!isModalOpen)  setIsModalOpen(true)

  }

  const closeModal =()=>{
       setIsModalOpen(false)
  }



  return (



    <>
    <ContactList contacts={contacts} />
    <button onClick={openModal}>Create New Contact</button>
    {isModalOpen&& <div className='modal'>
      
      <div className='modal-content'>
             
       <span className='close' onClick={closeModal}> &times;</span>
       <ContactForm />
      </div>
      </div>
      

      
      }
</>

  )
}

export default App
