import React, {useState, useEffect} from "react";
import axios from 'axios'
import { Link } from "react-router-dom";

const HomePage = () =>{
    const [data, setData] = useState(null)
    const [error , setError] = useState(null)
    const [showMicronutrients, setShowMicronutrients] = useState(false);
    const [loading, setLoading] = useState(true);
    useEffect(() => {
        const fetchData = async () => {
            try {
                const token = localStorage.getItem("token");

                const response = await axios.get("http://localhost:8000/target/me",
                {
                    headers: {
                    Authorization: `Bearer ${token}`,
                    },
                }
            );

                setData(response.data);
            } catch (error) {
                console.log("Error:", error);

                setError(error.response?.data?.detail || "Could not load your nutrition targets");
            } finally {
                setLoading(false);
            }
        };

        fetchData();
    }, []);

        if (loading) {
            return <div>Loading...</div>;
        }

        if (error) {
            return <div>{error}</div>;
        }

        if (!data) {
            return <div>No target data was found.</div>;
        }

        
         return (
            <div>
                <h1>Hello {data.full_name}, welcome to your fitness journey</h1>
                <h2>Here are your goals for today</h2>
                <Link to = "/protein">Protein <br /> {data.protein} g</Link><br/>
                <Link to = "/fats">Fats <br /> {data.fat} g</Link><br/>
                <Link to = "/carbohydrates">Carbohydrates <br /> {data.carbohydrates} g</Link><br/>
                <Link to = "/fiber">Fiber <br /> {data.fiber} g</Link><br/>
                <section>
                    <button onClick={() => setShowMicronutrients((prev) => !prev)}
                     aria-expanded={showMicronutrients}> 
                     {showMicronutrients? "▲ Hide vitamins & minerals": "▼ View vitamins & minerals"  }</button>

                     {showMicronutrients && (<div>
                        <p>Iron : {data.iron} mg</p>
                        <p>Calcium : {data.calcium} mg </p>
                        <p>Magnesium : {data.magnesium} mg</p>
                        <p>Potassium : {data.potassium} mg </p>
                        <p>Sodium : {data.sodium} mg</p>
                        <p>Vitamin A : {data.vitamin_a} mcg</p>
                        <p>Vitamin C : {data.vitamin_c} mg</p>
                        <p>Vitamin D : {data.vitamin_d} mcg</p>
                        <p>Vitamin B12 : {data.vitamin_b12} mcg</p>
                     </div>)}
                </section>
                
                
            </div>
            )
        }

        
        
export default HomePage
