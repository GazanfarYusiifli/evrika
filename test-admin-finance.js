const data = [
  { id: 10, payload: { amount: "0.01 AZN", payment_status: "Ödənilib", epoint_amount: "0.01", epoint_date: "2026-06-12T07:00:00Z" } },
  { id: 11, payload: { amount: "0.01 AZN", payment_status: "Ödənilməyib" } }
];

const payments = data.map(item => ({ ...item.payload, _id: item.id }))
                     .filter(p => p.epoint_amount || (p.amount && p.payment_status === 'Ödənilib'))
                     .sort((a,b) => new Date(b.epoint_date || b.submissionDate || 0) - new Date(a.epoint_date || a.submissionDate || 0));

console.log("Payments length:", payments.length);
