import { useEffect, useState } from "react";
import axios from "axios";
import TipsCard from "./TipsCard";

function HomeTips(){
  const [tips, setTips] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {async function fetchTips() {
    try{
        setIsLoading(true)
        setError("")
        const token = localStorage.getItem("token")
        const response = await axios.get("http://127.0.0.1:8000/tips/home",{
            headers: {
                Authorization: `Bearer ${token}`,
            },
        })
        setTips(response.data)  
    }
    catch(error){
        console.error("Failed to load tips:", error)
        setError("Could not load your tips.")
    }
    finally{
        setIsLoading(false)

    }
}
    fetchTips()
  },[])
  if (isLoading) {
  return (
    <section className="home-tips">
      <p className="home-tips-message">
        Loading your personalized tips...
      </p>
    </section>
  );
}

    if (error) {
        return (
            <section className="home-tips">
            <p className="home-tips-message">{error}</p>
            </section>
        );
    }

    if (tips.length === 0) {
        return (
            <section className="home-tips">
            <p className="home-tips-message">No tips are available right now.</p>
            </section>
        );
    }
  return(
    <section className="home-tips">
        <div className="home-tips-header">
            <div>
                <h2 className="section-label">Today's Tips</h2>
            </div>
        </div>
        <div className="home-tips-grid">
            {tips.map((tip) => (
                <TipsCard key={tip.id} tip={tip} />))}
        </div>

    </section>
  )
}
export default HomeTips;