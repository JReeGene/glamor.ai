import Link from 'next/link'
import styles from '@/app/subscriptions/subscriptions.module.css'
export default function Subcription() {
  return (
    <>
    <div className={styles.centered}>
      <small className={styles['small']}>Starting at..</small>
        <div className={styles.cost}>
          <span className={styles['cost-currency']}>$</span>
          <span className={styles['cost-dollars']}>19</span>
          <span className={styles['cost-cents']}>.99</span>
          <span className='text-blue-500'>ONLY</span>
        </div>
      <Link href="/subscriptions" className={styles["cta-button"]}>Subscribe</Link>
    </div>
    </>
    
  )
}
