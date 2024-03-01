import React from "react";

const ContactList = ({contacts}) => {

    return <div>

        <h1>Contacts</h1>

        <table>
            <thead> 
                <tr>
                    <th>First Name</th>
                    <th>Last Name</th>
                    <th>Email</th>
                    <th>Actions</th>

                </tr>
            </thead>
            <tbody>
          {contacts.map((contact) => (
            <tr key={contact.id}>
         
              <td>{contact.firstName}</td> {/* Assuming firstName property */}
              <td>{contact.lastName}</td> {/* Assuming lastName property */}
              <td>{contact.email}</td>
              <td>
                <button>Update</button>
                <button>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
           
        </table>

    </div>


}


export default ContactList