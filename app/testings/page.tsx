import React from 'react'
import styles from '@/app/testings/testings.module.css'
import DarkMode from '../darkmode'



export default function Testings() {
  return (
    <div>
      <DarkMode />
      <br />
      <br />
      <br />
      <hr />
      <h1 className={styles.header}>Testing Here</h1> 
      <p className="text-blue-500 text-center">I'm a Blue Paragraph</p>
    </div>
    
  )
}
