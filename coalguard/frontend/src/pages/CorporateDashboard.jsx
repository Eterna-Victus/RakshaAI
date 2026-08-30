import React, { useEffect, useState } from 'react';
import api from '../lib/api';

export default function CorporateDashboard() {
  const [summary, setSummary] = useState(null);
  const [riskRanking, setRiskRanking] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [sumRes, riskRes] = await Promise.all([
          api.get('/dashboard/summary'),
          api.get('/dashboard/risk/mines')
        ]);
        setSummary(sumRes.data);
        setRiskRanking(riskRes.data);
      } catch (err) {
        console.error(err);
      }
    };
    fetchData();
  }, []);

  return (
    <div className="container">
      <div className="flex-between mb-6">
        <h1 className="text-3xl">Enterprise Governance</h1>
        <div style={{ display: 'flex', gap: '1rem' }}>
          <a href="/khaan-netra/index.html" target="_blank" rel="noreferrer" className="btn-primary" style={{ background: '#3b82f6', color: 'white', textDecoration: 'none', display: 'flex', alignItems: 'center' }}>
            Open Khaan Netra (CV Scanner)
          </a>
          <button className="btn-danger" onClick={async () => {
            await api.post('/admin/reset-demo');
            window.location.reload();
          }}>
            Reset Demo
          </button>
        </div>
      </div>
      
      {summary && (
        <div className="dashboard-grid">
          <div className="card" style={{ borderLeft: '4px solid var(--primary)' }}>
            <h3 className="text-muted mb-2">Compliance Rate</h3>
            <p className="text-3xl">{summary.compliance_rate}%</p>
          </div>
          <div className="card" style={{ borderLeft: '4px solid var(--danger)' }}>
            <h3 className="text-muted mb-2">Open Violations (High/Crit)</h3>
            <p className="text-3xl">{summary.open_violations}</p>
          </div>
          <div className="card" style={{ borderLeft: '4px solid var(--warning)' }}>
            <h3 className="text-muted mb-2">Overdue Actions</h3>
            <p className="text-3xl">{summary.overdue_actions}</p>
          </div>
        </div>
      )}

      <div className="card mt-4">
        <h2 className="text-xl mb-4">Mine Risk Ranking</h2>
        <table className="data-table">
          <thead>
            <tr>
              <th>Mine</th>
              <th>Risk Score</th>
              <th>Primary Reasons</th>
            </tr>
          </thead>
          <tbody>
            {riskRanking.map((mine) => (
              <tr key={mine.mine_id}>
                <td style={{ fontWeight: 600 }}>{mine.mine_name}</td>
                <td>
                  <span className={`status-badge ${mine.score > 80 ? 'status-red' : mine.score > 40 ? 'status-orange' : 'status-green'}`}>
                    {mine.score}
                  </span>
                </td>
                <td className="text-muted" style={{ textTransform: 'none' }}>
                  {mine.reasons.join(', ')}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
