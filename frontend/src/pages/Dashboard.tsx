const Dashboard = () => {
  return (
    <div>
      <h1>Dashboard</h1>
      <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr 1fr", gap: "1rem" }}>
        {/* 5 small cards placeholders */}
        <div style={{ border: "1px solid grey", padding: "1rem" }}>Total Users</div>
        <div style={{ border: "1px solid grey", padding: "1rem" }}>Licenses</div>
        <div style={{ border: "1px solid grey", padding: "1rem" }}>MFA Disabled</div>
        <div style={{ border: "1px solid grey", padding: "1rem" }}>Teams Active</div>
        <div style={{ border: "1px solid grey", padding: "1rem" }}>Mailbox Usage</div>
      </div>
    </div>
  )
}

export default Dashboard
