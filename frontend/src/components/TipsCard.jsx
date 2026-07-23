import "../styles/tipsCard.css"

function TipsCard({tip}){
    return(
        <article className="tip-card">
            <span>🌸</span>
            <h3>{tip.title}</h3>
            <p>{tip.content}</p>
        </article>
    )

}
export default TipsCard;